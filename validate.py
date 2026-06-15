#!/usr/bin/env python3
"""Validate the corpus ontology contract.

Run from the repository root:

    python3 validate.py

Exit 0 is conformance. The validator does two things the prose contract
cannot do for itself:

  1. Schema validation. It loads `ontology.yaml` and checks it against
     `ontology.schema.json` using a real JSON Schema validator — shape,
     required fields, and type-set closure (no edge type outside the
     declared set).

  2. Cross-cutting invariants the schema cannot express: referential
     integrity, reciprocity consistency, orphan nodes, every node's home
     file exists, every prose file has a node, and topology coverage.

Dependencies: `pyyaml`, `jsonschema` (`pip install pyyaml jsonschema`).
No runtime service; plain text, git-native.
"""

from __future__ import annotations

import json
import pathlib
import sys

import yaml

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover
    sys.stderr.write(
        "validate.py requires jsonschema: pip install jsonschema pyyaml\n"
    )
    sys.exit(2)

ROOT = pathlib.Path(__file__).resolve().parent
ONTOLOGY = ROOT / "ontology.yaml"
SCHEMA = ROOT / "ontology.schema.json"
PRINCIPLES_DIR = ROOT / "principles"
COMPOSITIONS_DIR = ROOT / "compositions"

failures: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def main() -> int:
    data = yaml.safe_load(ONTOLOGY.read_text())
    schema = json.loads(SCHEMA.read_text())

    # 1 — Schema validation (shape + type-set closure) ----------------------
    validator = Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: e.path):
        loc = "/".join(str(p) for p in err.path) or "<root>"
        fail(f"schema: {loc}: {err.message}")

    # Build lookups (best-effort even if schema failed, to surface more).
    nodes = {n["id"]: n for n in data.get("nodes", []) if isinstance(n, dict)}
    node_ids = set(nodes)
    rel_types = set(data.get("relation_types", {}))
    center_id = (data.get("topology", {}).get("center", {}) or {}).get("id")
    # Edge targets may resolve to a node or to the topology center.
    edge_targets = node_ids | ({center_id} if center_id else set())

    edges = [e for e in data.get("edges", []) if isinstance(e, dict)]
    comps = [c for c in data.get("compositions", []) if isinstance(c, dict)]

    # 2 — Type-set closure beyond the schema enum ---------------------------
    # Every edge type and every fold target is a declared relation_type.
    for e in edges:
        if e.get("type") not in rel_types:
            fail(f"closure: edge type '{e.get('type')}' is not a declared relation_type")
    for f in data.get("folds", []):
        if isinstance(f, dict) and f.get("into") not in rel_types:
            fail(f"closure: fold '{f.get('label')}' folds into undeclared type '{f.get('into')}'")

    # 3 — Referential integrity ---------------------------------------------
    for e in edges:
        if e.get("from") not in node_ids:
            fail(f"ref: edge from '{e.get('from')}' does not resolve to a node")
        if e.get("to") not in edge_targets:
            fail(f"ref: edge to '{e.get('to')}' does not resolve to a node or the center")
    for c in comps:
        for m in c.get("members", []):
            if m not in node_ids:
                fail(f"ref: composition '{c.get('name')}' member '{m}' does not resolve to a node")
        if c.get("documented") and c.get("node") not in node_ids:
            fail(f"ref: composition '{c.get('name')}' node '{c.get('node')}' does not resolve")
        if c.get("documented"):
            n = nodes.get(c.get("node"))
            if n and n.get("type") != "composition":
                fail(f"ref: composition '{c.get('name')}' node '{c.get('node')}' is not type composition")

    # 4 — Reciprocity consistency -------------------------------------------
    # Symmetric edges are stored once; a reverse duplicate is a contract error.
    symmetric = {
        t for t, d in data.get("relation_types", {}).items()
        if isinstance(d, dict) and d.get("directionality") == "symmetric"
    }
    seen: dict[tuple, tuple] = {}
    for e in edges:
        a, b, t = e.get("from"), e.get("to"), e.get("type")
        if t in symmetric:
            key = (t, frozenset((a, b)))
            if key in seen:
                fail(f"reciprocity: symmetric {t} edge {a}<->{b} is stored more than once")
            seen[key] = (a, b)
    # `enabled-by` is a rendering, never a stored edge.
    if any(e.get("type") == "enabled-by" for e in edges):
        fail("reciprocity: 'enabled-by' is a rendering of 'enables', not a stored edge")

    # 5 — Orphan nodes ------------------------------------------------------
    touched = set()
    for e in edges:
        touched.add(e.get("from"))
        if e.get("to") in node_ids:
            touched.add(e.get("to"))
    for c in comps:
        touched.update(c.get("members", []))
    for nid in node_ids:
        if nid not in touched:
            fail(f"orphan: node '{nid}' participates in no edge or composition")

    # 6 — Every node's home file exists; every prose file has a node --------
    for nid, n in nodes.items():
        fp = ROOT / n.get("file", "")
        if not fp.is_file():
            fail(f"file: node '{nid}' home file '{n.get('file')}' does not exist")

    prose = sorted(PRINCIPLES_DIR.glob("*.md")) + sorted(COMPOSITIONS_DIR.glob("*.md"))
    homed = {str((ROOT / n["file"]).resolve()) for n in nodes.values() if n.get("file")}
    for fp in prose:
        if str(fp.resolve()) not in homed:
            fail(f"coverage: prose file '{fp.relative_to(ROOT)}' has no node")
    if len(prose) != len(nodes):
        fail(f"coverage: node count {len(nodes)} != prose file count {len(prose)}")

    # 7 — Topology coverage -------------------------------------------------
    principle_ids = {nid for nid, n in nodes.items() if n.get("type") == "principle"}
    in_movements: dict[str, int] = {}
    for mv in data.get("topology", {}).get("movements", []):
        for pid in mv.get("principles", []):
            if pid not in principle_ids:
                fail(f"topology: movement '{mv.get('id')}' lists '{pid}', not a principle node")
            in_movements[pid] = in_movements.get(pid, 0) + 1
            # node.movement agrees with topology placement
            if pid in nodes and nodes[pid].get("movement") != mv.get("id"):
                fail(f"topology: '{pid}' movement '{nodes[pid].get('movement')}' != placement '{mv.get('id')}'")
    for pid in principle_ids:
        c = in_movements.get(pid, 0)
        if c == 0:
            fail(f"topology: principle '{pid}' is in no movement")
        elif c > 1:
            fail(f"topology: principle '{pid}' is in {c} movements")

    # Report ----------------------------------------------------------------
    if failures:
        print(f"FAIL — {len(failures)} problem(s):")
        for m in failures:
            print(f"  - {m}")
        return 1

    edge_counts: dict[str, int] = {}
    for e in edges:
        edge_counts[e["type"]] = edge_counts.get(e["type"], 0) + 1
    by_type = ", ".join(f"{t}:{edge_counts[t]}" for t in sorted(edge_counts))
    n_principles = sum(1 for n in nodes.values() if n["type"] == "principle")
    n_compositions = sum(1 for n in nodes.values() if n["type"] == "composition")
    n_documented = sum(1 for c in comps if c.get("documented"))

    print(
        "OK — ontology contract conforms.\n"
        f"  nodes: {len(nodes)} ({n_principles} principles, {n_compositions} compositions)\n"
        f"  compositions: {len(comps)} ({n_documented} documented, {len(comps) - n_documented} edge-form)\n"
        f"  edges: {len(edges)} ({by_type})\n"
        f"  declared relation types: {len(rel_types)}; folds: {len(data.get('folds', []))}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
