# Principles

My canonical, domain-neutral principles corpus — the single source
of truth I carry into every project. Any project may link here; none
keep a local copy. Each
principle is stated at its universal level: the invariant that holds
across any domain. The familiar domain forms — DRY, "one mechanism, not
two," "fail explicitly" — attach to their universals as **projections**,
so a reader can traverse from the invariant to its practical
instantiations and back.

This corpus is **consumed, never duplicated**: projects refer to it; no
project keeps an editable second copy or a separately-maintained
distillation. (That rule is itself one of these principles:
[Single Home](principles/single-home.md).)

## The structure

- **Universal core** — thirteen principles, one document each, under
  [`principles/`](principles/). Each document carries the invariant, its
  exposition, recognition and corrective signals, its corollaries and
  projections, and its typed relations to other principles.
- **Projections** — domain instantiations, held *inside* the document of
  the universal they project (one home per principle: the universal and
  its projections evolve as a unit). Every projection names its source
  register item.
- **Relations** — typed edges between principles, in each document's
  **Relations** section.
- **Named compositions** — disciplines made of several universals acting
  together, under [`compositions/`](compositions/). A composition earns
  a document only when it carries content no edge can hold (its own
  invariant, its own failure modes); otherwise it lives as a
  **composition** edge in its constituents' Relations. Each document's
  constituents carry reciprocal edges back to it. Instances:
  [Completed Noticing](compositions/completed-noticing.md) ·
  [Dosed Compliance](compositions/dosed-compliance.md).
- **[SOURCES.md](SOURCES.md)** — the coverage map: every item of the
  five source registers and its classification. This is the reverse
  index, from a familiar domain form to its universal.

## The topology

The principles compose as four movements with a center. The movements
move in order — the corpus obeys its own
[Sequence](principles/sequence.md):

| Movement | Question it answers | Principles |
|---|---|---|
| **I — Ground** | What is true, and who owns what? | [Grounding](principles/grounding.md) · [Traceability](principles/traceability.md) · [Sovereignty](principles/sovereignty.md) · [Sequence](principles/sequence.md) |
| **II — Shape** | Is the answer earned, single, and durable? | [Parsimony](principles/parsimony.md) · [Single Home](principles/single-home.md) · [Evolvability](principles/evolvability.md) |
| **III — Protect** | Does the system tell the truth and repair itself? | [Honest Signal](principles/honest-signal.md) · [Source Repair](principles/source-repair.md) · [Obligation to Dissent](principles/obligation-to-dissent.md) · [Recursive Improvement](principles/recursive-improvement.md) |
| **IV — Land** | Can the recipient act, and is completion a fact? | [Transmission](principles/transmission.md) · [Verifiable Completion](principles/verifiable-completion.md) |

**The center is the spiral.** The movements are not a checklist but a
cycle that advances: refinement plus propulsion. Work grounds, takes
shape, is protected, lands — and the friction of landing feeds the next
turn. Remove a movement and the rest deform, each in a named way:

- *No Ground:* elegant fiction — sovereignty confusion, inherited
  framing, untraceable chains, arbitrary order. The system cannot see.
- *No Shape:* sprawl — unearned weight, duplicated truth, forward debt.
  The system calcifies.
- *No Protect:* decay — silent surfaces, patched symptoms, swallowed
  problems, object-only work. The system rots.
- *No Land:* waste — work that never ships, or ships as assertion
  instead of fact. The system produces but does not deliver.

**Why this topology.** The four sources answered the topology question
two ways: a compass (commons, 7 principles) and four movements
(with-claude, 13). The four-movement form is the one that had already
survived contact with the larger register, and it carries meaning in its
order — each movement produces the ground the next requires — where the
compass arrangement is positional only. It was therefore adopted and
enriched with what the compass did better: the named-failure diagnostic
(above) and the explicit center. Thirteen universals is what the actual
material ascended to — twelve from the four synthesis registers, the
thirteenth ([Traceability](principles/traceability.md)) when the fifth
register was classified
([#2](https://github.com/pentaxis93/principles/issues/2)); no source
count was ever a target.

## The relationship taxonomy

Six edge types, each earned by at least one concrete edge in this
corpus — the smallest set the material required, not a speculative
ontology:

| Type | Meaning | Example edge |
|---|---|---|
| **projection** | A universal instantiated in a domain | Single Home → *computed over stored* (state management) |
| **corollary** | A same-level consequence derivable from a universal | Honest Signal → *prefer absence to wrongness* |
| **composition** | A discipline made of two or more universals acting together; one that carries content no edge can hold gets its own document under [`compositions/`](compositions/) | *Everything earns its place* = Grounding ∘ Parsimony; [Completed Noticing](compositions/completed-noticing.md) (documented) |
| **dual** | One invariant seen from two aspects (design-time/runtime, object/process) | Evolvability ↔ Recursive Improvement |
| **isomorphism** | The same move recurring in different domains | *Read the manual* (cognition) ≅ *consult, don't model* (enforcement) |
| **enables** | One principle is the precondition of another | Single Home → Recursive Improvement (the spiral needs a bounded asset) |

## How to traverse

- **From a universal to its practice:** open the principle document;
  its projections are inside.
- **From a familiar maxim to its universal:** look it up in
  [SOURCES.md](SOURCES.md).
- **Across the graph:** follow the **Relations** section in any
  principle document.
- **From a principle to its origins:** every document's **Sources**
  section links the register items that shaped it.

Reading order for a first pass: the table above, top to bottom — the
movements are ordered, and so are the principles within them.

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
fragmented instantiations, then re-attaching the instantiations as
projections. The full per-item sort, including which commons ADRs are
principle-shaped and which are genuine decisions, is in
[SOURCES.md](SOURCES.md).
