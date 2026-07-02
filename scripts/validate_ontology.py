#!/usr/bin/env python3
from __future__ import annotations

import argparse
import posixpath
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, exceptions
from markdown_it import MarkdownIt


EXPECTED_TYPES = {
    "projection",
    "corollary",
    "composition",
    "dual",
    "isomorphism",
    "enables",
    "kin",
}
RELATION_LABELS = {
    "composition",
    "composed-of",
    "dual",
    "dual (tension)",
    "isomorphism",
    "enables",
    "enabled-by",
    "kin",
}
SYMMETRIC_TYPES = {"dual", "isomorphism", "kin"}
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
RELATION_START_RE = re.compile(r"^- \*\*(?P<label>[^*]+)\*\*")
H1_RE = re.compile(r"^# (?P<title>.+)$", re.MULTILINE)


class ValidationFailure(Exception):
    pass


@dataclass(frozen=True)
class RelationEntry:
    source: str
    relation_type: str
    label: str
    targets: tuple[str, ...]
    annotation: str | None = None
    name: str | None = None

    def comparable(self) -> tuple[str, str, str, str | None, tuple[str, ...]]:
        return (self.source, self.relation_type, self.label, self.annotation, self.targets)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the principles ontology graph.")
    parser.add_argument("--root", default=".", help="Corpus checkout root")
    args = parser.parse_args()
    root = Path(args.root)

    try:
        graph = load_yaml(root / "ontology.yaml")
        schema = load_yaml(root / "ontology.schema.yaml")
        validate_schema(graph, schema)
        validate_graph(root, graph)
    except ValidationFailure as error:
        print(str(error), file=sys.stderr)
        return 1
    print("ontology validation passed")
    return 0


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ValidationFailure(f"required file missing: {path}")
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as error:
        raise ValidationFailure(f"YAML parse failed for {path}: {error}") from error
    if not isinstance(data, dict):
        raise ValidationFailure(f"{path} must contain a YAML mapping")
    return data


def validate_schema(graph: dict[str, Any], schema: dict[str, Any]) -> None:
    try:
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(graph)
    except exceptions.ValidationError as error:
        path = ".".join(str(part) for part in error.absolute_path)
        location = f" at {path}" if path else ""
        raise ValidationFailure(f"schema validation failed{location}: {error.message}") from error
    except exceptions.SchemaError as error:
        raise ValidationFailure(f"ontology schema is invalid: {error.message}") from error


def validate_graph(root: Path, graph: dict[str, Any]) -> None:
    MarkdownIt("commonmark").enable("table").parse((root / "ONTOLOGY.md").read_text(encoding="utf-8"))
    relation_types = graph["relation_types"]
    folds = graph["folds"]
    nodes = graph["nodes"]
    relations = [relation_from_graph(item) for item in graph["relations"]]

    type_names = {item["name"] for item in relation_types}
    if type_names != EXPECTED_TYPES:
        raise ValidationFailure(f"type-set closure failed: expected {sorted(EXPECTED_TYPES)}, got {sorted(type_names)}")

    # The identity rule: a label matching a declared type folds to itself.
    # Declared folds carry the non-identity labels (and may override with a
    # recorded reason).
    fold_by_label = {
        item["name"]: {"label": item["name"], "canonical_type": item["name"]}
        for item in relation_types
    }
    fold_by_label.update({item["label"]: item for item in folds})
    missing_labels = RELATION_LABELS - set(fold_by_label)
    if missing_labels:
        raise ValidationFailure(f"type-set closure failed: missing fold dispositions for {sorted(missing_labels)}")

    annotations = annotation_hosts(relation_types)
    for fold in folds:
        annotation = fold.get("annotation")
        if annotation and annotations.get(annotation) != fold["canonical_type"]:
            raise ValidationFailure(f"annotation legality failed: {annotation} is not sanctioned on {fold['canonical_type']}")
    for relation in relations:
        expected_type = fold_by_label[relation.label]["canonical_type"]
        if relation.relation_type != expected_type:
            raise ValidationFailure(f"type-set closure failed: {relation.label} must encode as {expected_type}")
        if relation.annotation and annotations.get(relation.annotation) != relation.relation_type:
            raise ValidationFailure(f"annotation legality failed: {relation.annotation} is not sanctioned on {relation.relation_type}")

    node_by_id = validate_nodes(root, nodes)
    validate_topology(root, graph["topology"], node_by_id)
    validate_relation_endpoints(relations, node_by_id)
    validate_reciprocity(relations, node_by_id)
    validate_relation_coverage(root, relations, node_by_id, fold_by_label)
    validate_tables(root, relation_types, folds)
    validate_orphans(relations, graph["topology"], node_by_id)


def relation_from_graph(item: dict[str, Any]) -> RelationEntry:
    return RelationEntry(
        source=item["source"],
        relation_type=item["type"],
        label=item["label"],
        annotation=item.get("annotation"),
        name=item.get("name"),
        targets=tuple(item["targets"]),
    )


def annotation_hosts(relation_types: list[dict[str, Any]]) -> dict[str, str]:
    hosts: dict[str, str] = {}
    for relation_type in relation_types:
        for annotation in relation_type.get("annotations", []):
            hosts[annotation["label"]] = relation_type["name"]
    return hosts


def validate_nodes(root: Path, nodes: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    node_by_id: dict[str, dict[str, Any]] = {}
    for node in nodes:
        if node["id"] in node_by_id:
            raise ValidationFailure(f"duplicate node id: {node['id']}")
        node_by_id[node["id"]] = node

    prose_paths = {
        path.relative_to(root).as_posix()
        for directory in ("principles", "compositions")
        for path in sorted((root / directory).glob("*.md"))
    }
    graph_paths = {node["path"] for node in nodes}

    for node in nodes:
        path = root / node["path"]
        if not path.is_file():
            raise ValidationFailure(f"node home file missing: {node['id']} -> {node['path']}")
        title = first_h1(path)
        if title != node["title"]:
            raise ValidationFailure(f"node title mismatch: {node['id']} graph={node['title']!r} prose={title!r}")

    for path in sorted(prose_paths - graph_paths):
        raise ValidationFailure(f"prose document has no node: {path}")
    for path in sorted(graph_paths - prose_paths):
        raise ValidationFailure(f"node home file missing: {path}")

    return node_by_id


def first_h1(path: Path) -> str:
    match = H1_RE.search(path.read_text(encoding="utf-8"))
    if not match:
        raise ValidationFailure(f"node home file has no title: {path}")
    return match.group("title").strip()


def validate_topology(root: Path, topology: dict[str, Any], node_by_id: dict[str, dict[str, Any]]) -> None:
    assigned: list[str] = []
    for movement in topology["movements"]:
        for node_id in movement["principles"]:
            if node_id not in node_by_id:
                raise ValidationFailure(f"topology mismatch: movement {movement['label']} references unknown node {node_id}")
            if node_by_id[node_id]["kind"] != "principle":
                raise ValidationFailure(f"topology mismatch: movement {movement['label']} contains non-principle node {node_id}")
            assigned.append(node_id)
    if len(assigned) != len(set(assigned)):
        raise ValidationFailure("topology mismatch: principle assigned to more than one movement")

    table = table_after_heading((root / "ONTOLOGY.md").read_text(encoding="utf-8"), "Topology", 0)
    prose: dict[str, tuple[str, list[str]]] = {}
    for row in table:
        movement = strip_formatting(row["Movement"])
        prose[movement] = (row["Question it answers"], linked_node_ids(row["Principles"]))

    for movement in topology["movements"]:
        if movement["label"] not in prose:
            raise ValidationFailure(f"topology mismatch: missing prose row for {movement['label']}")
        question, principles = prose[movement["label"]]
        if question != movement["question"] or principles != movement["principles"]:
            raise ValidationFailure(f"topology mismatch: {movement['label']}")


def validate_relation_endpoints(
    relations: list[RelationEntry],
    node_by_id: dict[str, dict[str, Any]],
) -> None:
    allowed = set(node_by_id)
    for relation in relations:
        if relation.source not in node_by_id:
            raise ValidationFailure(f"dangling endpoint: relation source {relation.source} is not a node")
        for target in relation.targets:
            if target not in allowed:
                raise ValidationFailure(f"dangling endpoint: {relation.source} -> {target}")


def validate_relation_coverage(
    root: Path,
    graph_relations: list[RelationEntry],
    node_by_id: dict[str, dict[str, Any]],
    fold_by_label: dict[str, dict[str, Any]],
) -> None:
    prose_relations = parse_prose_relations(root, node_by_id, fold_by_label)
    graph_set = {relation.comparable() for relation in graph_relations}
    prose_set = {relation.comparable() for relation in prose_relations}
    missing_from_prose = sorted(graph_set - prose_set)
    missing_from_graph = sorted(prose_set - graph_set)
    if missing_from_prose or missing_from_graph:
        details = []
        if missing_from_prose:
            details.append(f"graph-only={missing_from_prose[:3]}")
        if missing_from_graph:
            details.append(f"prose-only={missing_from_graph[:3]}")
        raise ValidationFailure(f"prose relation mismatch: {'; '.join(details)}")


def validate_reciprocity(relations: list[RelationEntry], node_by_id: dict[str, dict[str, Any]]) -> None:
    by_source = {}
    for relation in relations:
        by_source.setdefault(relation.source, []).append(relation)

    for relation in relations:
        for target in relation.targets:
            if target not in node_by_id or target == relation.source:
                continue
            if relation.relation_type in SYMMETRIC_TYPES:
                if not has_relation(by_source, target, relation.relation_type, {relation.source}, annotation=relation.annotation):
                    raise ValidationFailure(f"missing reciprocal: {relation.source} {relation.label} {target}")
            elif relation.relation_type == "enables":
                expected_label = "enabled-by" if relation.label == "enables" else "enables"
                if not has_relation(by_source, target, "enables", {relation.source}, label=expected_label):
                    raise ValidationFailure(f"missing reciprocal: {relation.source} {relation.label} {target}")
            elif relation.relation_type == "composition":
                if node_by_id[target]["kind"] == "composition":
                    if not has_relation(by_source, target, "composition", {relation.source}):
                        raise ValidationFailure(f"missing reciprocal: {relation.source} composition {target}")
                elif node_by_id[relation.source]["kind"] == "composition":
                    if not has_relation(by_source, target, "composition", {relation.source}):
                        raise ValidationFailure(f"missing reciprocal: {relation.source} composition {target}")
                elif relation.name:
                    if not has_relation(by_source, target, "composition", {relation.source}, name=relation.name):
                        raise ValidationFailure(f"missing reciprocal: {relation.source} composition {target}")


def has_relation(
    by_source: dict[str, list[RelationEntry]],
    source: str,
    relation_type: str,
    required_targets: set[str],
    *,
    label: str | None = None,
    annotation: str | None = None,
    name: str | None = None,
) -> bool:
    for candidate in by_source.get(source, []):
        if candidate.relation_type != relation_type:
            continue
        if label is not None and candidate.label != label:
            continue
        if annotation is not None and candidate.annotation != annotation:
            continue
        if name is not None and candidate.name != name:
            continue
        if required_targets.issubset(set(candidate.targets)):
            return True
    return False


def validate_tables(
    root: Path,
    relation_types: list[dict[str, Any]],
    folds: list[dict[str, Any]],
) -> None:
    text = (root / "ONTOLOGY.md").read_text(encoding="utf-8")
    taxonomy_rows = table_after_heading(text, "Relationship taxonomy", 0)
    taxonomy = {strip_formatting(row["Type"]): row for row in taxonomy_rows}
    for relation_type in relation_types:
        row = taxonomy.get(relation_type["name"])
        if row is None:
            raise ValidationFailure(f"prose table mismatch: missing relation type {relation_type['name']}")
        checks = {
            "Meaning": relation_type["meaning"],
            "Placement": relation_type["placement"],
            "Directionality": relation_type["directionality"],
            "Reciprocity": relation_type["reciprocity"],
            "Rendering": relation_type["rendering"],
        }
        for column, expected in checks.items():
            if row[column] != expected:
                raise ValidationFailure(f"prose table mismatch: {relation_type['name']} {column}")

    fold_rows = table_after_heading(text, "Relationship taxonomy", 1)
    prose_folds = {strip_formatting(row["Label"]): row["Disposition"] for row in fold_rows}
    for fold in folds:
        if prose_folds.get(fold["label"]) != fold["disposition"]:
            raise ValidationFailure(f"prose table mismatch: fold {fold['label']}")


def validate_orphans(
    relations: list[RelationEntry],
    topology: dict[str, Any],
    node_by_id: dict[str, dict[str, Any]],
) -> None:
    touched = {relation.source for relation in relations}
    for relation in relations:
        touched.update(target for target in relation.targets if target in node_by_id)
    assigned = {node for movement in topology["movements"] for node in movement["principles"]}
    for node_id in sorted(set(node_by_id) - touched - assigned):
        raise ValidationFailure(f"orphan node: {node_id}")


def parse_prose_relations(
    root: Path,
    node_by_id: dict[str, dict[str, Any]],
    fold_by_label: dict[str, dict[str, Any]],
) -> list[RelationEntry]:
    relations: list[RelationEntry] = []
    path_to_id = {node["path"]: node_id for node_id, node in node_by_id.items()}
    for source, node in node_by_id.items():
        section = relations_section(root / node["path"])
        for block in relation_blocks(section):
            match = RELATION_START_RE.match(block)
            if not match:
                continue
            label = match.group("label").strip()
            if label not in fold_by_label:
                raise ValidationFailure(f"type-set closure failed: in-use label {label!r} has no disposition")
            targets = relation_targets(block, node["path"], path_to_id)
            if not targets:
                raise ValidationFailure(f"prose relation mismatch: {source} {label} has no resolvable target")
            fold = fold_by_label[label]
            relations.append(
                RelationEntry(
                    source=source,
                    relation_type=fold["canonical_type"],
                    label=label,
                    annotation=fold.get("annotation"),
                    name=composition_name(block, label),
                    targets=tuple(targets),
                )
            )
    return relations


def relations_section(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if "\n## Relations\n" not in text:
        raise ValidationFailure(f"prose document has no Relations section: {path}")
    after = text.split("\n## Relations\n", 1)[1]
    return after.split("\n## Sources\n", 1)[0]


def relation_blocks(section: str) -> list[str]:
    blocks: list[str] = []
    current: list[str] = []
    for line in section.splitlines():
        if line.startswith("- **"):
            if current:
                blocks.append("\n".join(current).strip())
            current = [line]
        elif current:
            current.append(line)
    if current:
        blocks.append("\n".join(current).strip())
    return blocks


def relation_targets(block: str, source_path: str, path_to_id: dict[str, str]) -> list[str]:
    targets: list[str] = []
    structural_sentence = re.split(r"\.(?:\s|$)", block, maxsplit=1)[0]
    for _text, href in LINK_RE.findall(structural_sentence):
        clean = href.split("#", 1)[0]
        if not clean:
            continue
        normalized = posixpath.normpath(posixpath.join(posixpath.dirname(source_path), clean))
        if normalized in path_to_id:
            targets.append(path_to_id[normalized])
    return targets


def composition_name(block: str, label: str) -> str | None:
    if label not in {"composition", "composed-of"}:
        return None
    first_line = block.splitlines()[0]
    match = re.match(r"^- \*\*(?:composition|composed-of)\*\* \u2014 (?P<name>[^:\n]+) :", first_line)
    if not match:
        return None
    return re.sub(r"\s+", " ", match.group("name")).strip()


def table_after_heading(text: str, heading: str, table_index: int) -> list[dict[str, str]]:
    marker = f"## {heading}"
    if marker not in text:
        raise ValidationFailure(f"prose table mismatch: missing heading {heading}")
    after = text.split(marker, 1)[1]
    tables: list[list[str]] = []
    current: list[str] = []
    for line in after.splitlines():
        if line.startswith("## ") and current:
            break
        if line.startswith("|"):
            current.append(line)
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)
    if table_index >= len(tables):
        raise ValidationFailure(f"prose table mismatch: missing table {table_index} under {heading}")
    return parse_table(tables[table_index])


def parse_table(lines: list[str]) -> list[dict[str, str]]:
    headers = [cell.strip() for cell in lines[0].strip("|").split("|")]
    rows = []
    for line in lines[2:]:
        values = [cell.strip() for cell in line.strip("|").split("|")]
        rows.append(dict(zip(headers, values, strict=True)))
    return rows


def strip_formatting(value: str) -> str:
    return value.replace("**", "").replace("`", "").strip()


def linked_node_ids(markdown: str) -> list[str]:
    ids: list[str] = []
    for _text, href in LINK_RE.findall(markdown):
        clean = href.split("#", 1)[0]
        if clean.startswith("principles/"):
            ids.append(Path(clean).stem)
    return ids


if __name__ == "__main__":
    raise SystemExit(main())
