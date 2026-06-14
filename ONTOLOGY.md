# Ontology

This is the corpus's form contract. Every principle document,
composition document, source classification, and graph edge consults or
derives from this document; the README orients readers to the corpus, but
this document owns the corpus's form.

## Relationship taxonomy

Relations have two placement classes.

**In-document relations** describe a universal's relation to its own
instantiations and consequences.

**Relations edges** describe typed edges between principles, and appear
in each document's **Relations** section.

| Type | Meaning | Placement | Directionality | Reciprocity | Rendering |
|---|---|---|---|---|---|
| **projection** | A universal instantiated in a domain form. | in-document | directional: universal -> domain form | none; intra-document | listed under **Projections**, each projection naming its source register item |
| **corollary** | A same-level consequence derivable from a universal. | in-document | directional: universal -> consequence | none; intra-document | stated under **Corollaries** as a named same-level consequence |
| **composition** | Two or more universals acting together as one discipline. | Relations | symmetric among constituents | reciprocal: every constituent carries the edge | `<Name> : <this document's face>`, with the name linked iff a `compositions/` document exists |
| **dual** | One invariant seen from two aspects. | Relations | symmetric | reciprocal: both endpoints carry it | `dual` - or `dual (tension)` - [Other](...): the one invariant seen as two aspects |
| **isomorphism** | The same move recurring in different domains. | Relations | symmetric | reciprocal: both endpoints carry it | `isomorphism` - [Other](...): the shared move, named in each domain |
| **enables** | One principle is the precondition of another's existence or sound operation. | Relations | directional: A enables B | reciprocal: target B carries `enabled-by` back to A | on A: `enables` - [B](...): B's precondition; on B: `enabled-by` - [A](...) |
| **kin** | Distinct invariants share a family resemblance, or make the same demand at two sites, without one deriving from the other. | Relations | symmetric | reciprocal: both endpoints carry it | `kin` - [Other](...): the shared demand or family resemblance |

Every relation label in use is either declared or folded:

| Label | Disposition |
|---|---|
| **projection** | declared as `projection` |
| **corollary** | declared as `corollary` |
| **composition** | declared as `composition` |
| **dual** | declared as `dual` |
| **isomorphism** | declared as `isomorphism` |
| **enables** | declared as `enables` |
| **kin** | declared as `kin` |
| **enabled-by** | reciprocal rendering of `enables` |
| **dual (tension)** | sanctioned annotation on `dual` when the two aspects bound an axis from opposite sides |
| **soundness condition** | folded into `enables`; the type is the precondition class, and the edge prose carries the soundness flavor |
| **fed-by** | folded into `enables`; the type is the precondition class, and the edge prose carries the supply-of-input flavor |
| **composed-of** | folded into `composition` as the composition-document-side rendering of its constituents |

The taxonomy uses the smallest set the material requires. A relation type
is declared when it carries structure no existing type can hold. It folds
when the existing type already carries the structure and the edge prose
can preserve the local flavor without losing meaning.

## Document schema

A principle document carries one universal. Its form is:

- title: the universal's canonical name;
- movement line: the topology movement and a link back to the index;
- invariant block: the universal stated in one durable sentence or short
  paragraph;
- **The universal**: the domain-neutral exposition, including
  **Recognition** and **Corrective** claims;
- **Corollaries**, when the universal has named same-level
  consequences;
- **Projections**, when the universal has domain forms, each projection
  naming its source register item;
- **Relations**: typed edges to other principles or compositions using
  this taxonomy;
- **Sources**: links to every source register item that shaped the
  universal, corollary, or projection.

A composition document carries a named discipline made of several
universals acting together. Its form is:

- title: the composition's Title Case name;
- named-composition line and index link;
- invariant block: the composition's own invariant;
- body sections that state the content no constituent edge can hold,
  especially the composition's own invariant, cycle, ownership claim, or
  failure modes;
- **Relations**, including the constituent list and reciprocal edges;
- **Sources**.

## Composition rules

A composition lives as an edge in its constituents' **Relations** by
default. It earns a `compositions/` document only when it carries content
no edge can hold: its own invariant, its own failure modes, or another
claim that belongs to the composition rather than to any constituent.

Every constituent of a composition carries the edge, naming the
composition and that constituent's face. A `compositions/` document
additionally lists its constituents; each constituent carries the
reciprocal `composition` edge back.

Composition names are Title Case noun phrases. The rendering form is
`<Name> : <this document's face>`, with the name linked iff a
`compositions/` document exists. A composition previously written as
"yields *maxim*" adopts the maxim as its Title Case name: **Everything
Earns Its Place** for Grounding ∘ Parsimony, and **History Lives in
Version Control** for Positive Form ∘ Single Home.

Three previously unnamed compositions are named here:

- **Safe Delegation**: Sovereignty ∘ Verifiable Completion.
- **Repair at the Emitter**: Honest Signal ∘ Source Repair.
- **Act at the Source**: Obligation to Dissent ∘ Source Repair.

Grounding ↔ Sequence resolves to a single consistent `enables` edge:
Grounding enables Sequence because grounding supplies the input that
sequence requires at the design boundary. Document conformance is applied
separately.

## SOURCES schema

`SOURCES.md` is the coverage map for the five source registers:

- Register 1: `tesserine/commons/PRINCIPLES.md`;
- Register 2: `tesserine/commons/DESIGN-PRINCIPLES.md`;
- Register 3: `tesserine/commons/adr/`;
- Register 4: `pentaxis93/with-claude/_shared/principles.md`;
- Register 5: `tesserine/groundwork` `skills/reckon/SKILL.md`
  §Navigational Principles.

Every item in those registers is classified as exactly one of:

- **ascended**: its content was raised to its universal level and lives in
  a canonical principle;
- **projection**: it is attached as a domain projection or corollary
  inside the named universal's document;
- **retained**: it is a genuine decision or design artifact, stays in its
  home, and is not a principle, though it may instantiate principles;
- **out of scope**: it is not corpus material, with the reason stated.

The reverse traversal lives in the principle documents themselves: each
universal's **Sources** section links back to every register item that
shaped it. Invariants that recur across the registers and consumer
methodology after the founding synthesis are classified in
post-synthesis ascent sections with the same vocabulary.

## Topology

The principles compose as four movements with a center. The movements
move in order: each produces the ground the next requires.

| Movement | Question it answers | Principles |
|---|---|---|
| **I - Ground** | What is true, and who owns what? | [Grounding](principles/grounding.md) · [Traceability](principles/traceability.md) · [Sovereignty](principles/sovereignty.md) · [Sequence](principles/sequence.md) |
| **II - Shape** | Is the answer earned, single, stated as itself, and durable? | [Parsimony](principles/parsimony.md) · [Single Home](principles/single-home.md) · [Positive Form](principles/positive-form.md) · [Evolvability](principles/evolvability.md) |
| **III - Protect** | Does the system tell the truth and repair itself? | [Honest Signal](principles/honest-signal.md) · [Source Repair](principles/source-repair.md) · [Obligation to Dissent](principles/obligation-to-dissent.md) · [Recursive Improvement](principles/recursive-improvement.md) |
| **IV - Land** | Can the recipient act, and is completion a fact? | [Transmission](principles/transmission.md) · [Verifiable Completion](principles/verifiable-completion.md) |

The center is the spiral: refinement plus propulsion. Work grounds, takes
shape, is protected, lands, and the friction of landing feeds the next
turn. Remove a movement and the rest deform in a named way:

- *No Ground:* elegant fiction - sovereignty confusion, inherited
  framing, untraceable chains, arbitrary order. The system cannot see.
- *No Shape:* sprawl - unearned weight, duplicated truth, forward debt.
  The system calcifies.
- *No Protect:* decay - silent surfaces, patched symptoms, swallowed
  problems, object-only work. The system rots.
- *No Land:* waste - work that never ships, or ships as assertion instead
  of fact. The system produces but does not deliver.

This topology adopts the four-movement form from the source material
because it carries meaning in its order. It retains what the compass
topology carried better: the named-failure diagnostic and the explicit
center.
