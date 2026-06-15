# Principles

My canonical, domain-neutral principles corpus — the single source
of truth I carry into every project. Any project may link here; none
keep a local copy. Each
principle is stated at its universal level: the invariant that holds
across any domain. The familiar domain forms — DRY, "one mechanism, not
two," "fail explicitly" — remain traversable through the form defined in
[ONTOLOGY.md](ONTOLOGY.md).

This corpus is **consumed, never duplicated**: projects refer to it; no
project keeps an editable second copy or a separately-maintained
distillation. (That rule is itself one of these principles:
[Single Home](principles/single-home.md).)

## The corpus

The corpus contains principle documents under [`principles/`](principles/),
named composition documents under [`compositions/`](compositions/) —
[Completed Noticing](compositions/completed-noticing.md),
[Dosed Compliance](compositions/dosed-compliance.md), and
[Contract-First](compositions/contract-first.md) — and the source
coverage map in [SOURCES.md](SOURCES.md). Its machine-checkable
structural spine lives in [ontology.yaml](ontology.yaml); the reader-facing
form contract is rendered in [ONTOLOGY.md](ONTOLOGY.md).

## The topology

The principles are read through the corpus topology, which lives in the
form contract: [ONTOLOGY.md#topology](ONTOLOGY.md#topology).

## The relationship taxonomy

The typed relation system lives in the form contract:
[ONTOLOGY.md#relationship-taxonomy](ONTOLOGY.md#relationship-taxonomy).

## How to traverse

- **From a universal to its practice:** open the principle document and
  follow the form defined in [ONTOLOGY.md](ONTOLOGY.md).
- **From a familiar maxim to its universal:** look it up in
  [SOURCES.md](SOURCES.md).
- **Across the graph:** follow the **Relations** section in any
  principle document; the edge forms are defined in
  [ONTOLOGY.md](ONTOLOGY.md).
- **From a principle to its origins:** follow the source links carried
  by the document.

Reading order for a first pass: follow the topology in
[ONTOLOGY.md#topology](ONTOLOGY.md#topology).

## Evolving this corpus

Friction with any principle, projection, or with the corpus structure
itself is filed as an issue on **this repository** — this is the
relocated feedback route formerly carried by with-claude's
`asset:principles` label. A principle change enters the recursive
spiral the way the corpus itself prescribes: friction accumulates here
(its [Single Home](principles/single-home.md)), important change-vectors
are claimed, and the corpus evolves as a unit by pull request — object
and process both, per
[Recursive Improvement](principles/recursive-improvement.md). Consumers
re-read; none patch local copies.

## Provenance

Synthesized 2026-06-10 from four source registers —
`tesserine/commons` `PRINCIPLES.md`, `DESIGN-PRINCIPLES.md`, and
`adr/`; `pentaxis93/with-claude` `_shared/principles.md` — per the
epic [pentaxis93/principles#1](https://github.com/pentaxis93/principles/issues/1).
A fifth register — `tesserine/groundwork` `skills/reckon/SKILL.md`
§Navigational Principles — was discovered after the synthesis and
classified 2026-06-11 per
[#2](https://github.com/pentaxis93/principles/issues/2).
The synthesis operation was Ascent: deriving each universal from its
fragmented instantiations, then attaching the source material in the
form defined by [ONTOLOGY.md](ONTOLOGY.md). The full per-item sort,
including which commons ADRs are principle-shaped and which are genuine
decisions, is in [SOURCES.md](SOURCES.md).
