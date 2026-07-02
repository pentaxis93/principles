from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_ontology.py"


def copy_corpus(tmp_path: Path) -> Path:
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    for name in ("README.md", "ONTOLOGY.md", "SOURCES.md", "ontology.yaml", "ontology.schema.yaml"):
        shutil.copy2(ROOT / name, corpus / name)
    for directory in ("principles", "compositions"):
        shutil.copytree(ROOT / directory, corpus / directory)
    return corpus


def run_validator(corpus: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), "--root", str(corpus)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def assert_validator_fails_with(corpus: Path, expected: str) -> None:
    result = run_validator(corpus)
    assert result.returncode != 0
    assert expected in result.stderr


def replace_text(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    assert old in text
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def test_conformed_corpus_validates(tmp_path: Path) -> None:
    corpus = copy_corpus(tmp_path)
    result = run_validator(corpus)
    assert result.returncode == 0, result.stderr
    assert "ontology validation passed" in result.stdout


def test_rejects_undeclared_edge_type(tmp_path: Path) -> None:
    corpus = copy_corpus(tmp_path)
    replace_text(corpus / "ontology.yaml", "type: kin\n", "type: affinity\n")
    assert_validator_fails_with(corpus, "schema validation failed")


def test_schema_rejects_annotation_on_wrong_host_type(tmp_path: Path) -> None:
    corpus = copy_corpus(tmp_path)
    replace_text(
        corpus / "ontology.yaml",
        "  - source: honest-signal\n    type: kin\n    label: kin\n    targets:\n      - verifiable-completion\n",
        "  - source: honest-signal\n    type: kin\n    label: kin\n    annotation: tension\n    targets:\n      - verifiable-completion\n",
    )
    assert_validator_fails_with(corpus, "schema validation failed")


def test_rejects_dangling_endpoint(tmp_path: Path) -> None:
    corpus = copy_corpus(tmp_path)
    replace_text(
        corpus / "ontology.yaml",
        "  - source: verifiable-completion\n    type: kin\n    label: kin\n    targets:\n      - honest-signal\n",
        "  - source: verifiable-completion\n    type: kin\n    label: kin\n    targets:\n      - missing-node\n",
    )
    assert_validator_fails_with(corpus, "dangling endpoint")


def test_rejects_missing_reciprocal(tmp_path: Path) -> None:
    corpus = copy_corpus(tmp_path)
    replace_text(
        corpus / "ontology.yaml",
        "  - source: honest-signal\n    type: kin\n    label: kin\n    targets:\n      - verifiable-completion\n",
        "",
    )
    assert_validator_fails_with(corpus, "missing reciprocal")


def test_rejects_orphan_node(tmp_path: Path) -> None:
    corpus = copy_corpus(tmp_path)
    (corpus / "principles" / "orphan.md").write_text(
        "# Orphan\n\n**Movement:** I - Ground - [Index](../README.md)\n\n> Placeholder.\n\n## The universal\n\nPlaceholder.\n\n## Relations\n\n## Sources\n",
        encoding="utf-8",
    )
    replace_text(corpus / "ontology.yaml", "    path: principles/parsimony.md\n", "    path: principles/parsimony.md\n  - id: orphan\n    title: Orphan\n    kind: principle\n    path: principles/orphan.md\n")
    assert_validator_fails_with(corpus, "orphan node")


def test_rejects_node_with_no_home_file(tmp_path: Path) -> None:
    corpus = copy_corpus(tmp_path)
    replace_text(corpus / "ontology.yaml", "path: principles/grounding.md", "path: principles/missing.md")
    assert_validator_fails_with(corpus, "node home file missing")


def test_rejects_prose_document_with_no_node(tmp_path: Path) -> None:
    corpus = copy_corpus(tmp_path)
    replace_text(
        corpus / "ontology.yaml",
        "  - id: grounding\n    title: Grounding\n    kind: principle\n    path: principles/grounding.md\n",
        "",
    )
    assert_validator_fails_with(corpus, "prose document has no node")


def test_rejects_topology_mismatch(tmp_path: Path) -> None:
    corpus = copy_corpus(tmp_path)
    replace_text(corpus / "ontology.yaml", "    - grounding\n", "    - parsimony\n",)
    assert_validator_fails_with(corpus, "topology mismatch")


def test_rejects_prose_rendering_mismatch(tmp_path: Path) -> None:
    corpus = copy_corpus(tmp_path)
    replace_text(
        corpus / "principles" / "verifiable-completion.md",
        "**kin** \u2014 [Honest Signal](honest-signal.md)",
        "**kin** \u2014 [Parsimony](parsimony.md)",
    )
    assert_validator_fails_with(corpus, "prose relation mismatch")
