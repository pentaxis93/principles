# Ontology

This renders the corpus's form contract for readers. The
machine-checkable structural spine lives in [ontology.yaml](ontology.yaml);
the prose renderings here are checked against it. The README orients
readers to the corpus.

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
| **dual** | One invariant seen from two aspects. | Relations | symmetric | reciprocal: both endpoints carry it | `dual` - or `dual (tension)` - `[Other](...)`: the one invariant seen as two aspects |
| **isomorphism** | The same move recurring in different domains. | Relations | symmetric | reciprocal: both endpoints carry it | `isomorphism` - `[Other](...)`: the shared move, named in each domain |
| **enables** | One principle is the precondition of another's existence or sound operation. | Relations | directional: A enables B | reciprocal: target B carries `enabled-by` back to A | on A: `enables` - `[B](...)`: B's precondition; on B: `enabled-by` - `[A](...)` |
| **kin** | Distinct invariants share a family resemblance, or make the same demand at two sites, without one deriving from the other. | Relations | symmetric | reciprocal: both endpoints carry it | `kin` - or `kin (boundary)` - `[Other](...)`: the shared demand or family resemblance |

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
| **kin (boundary)** | sanctioned annotation on `kin` when a relation marks the boundary between a dosed lever and an undosed constitutive demand |
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

**Contract-First** — Sovereignty ∘ Single Home ∘ Verifiable Completion ∘
Sequence — receives a [`compositions/` document](compositions/contract-first.md).
It meets the bar above for a document of its own: it carries
composition-level content no constituent edge holds — the contract as the
unit of agentic composition, and the force-and-time to energy-state
isomorphism that makes that composition tractable.

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

The named compositions are read against the movements that supply their
constituents rather than placed inside them. Among them,
[Contract-First](compositions/contract-first.md) is foundational: it
composes universals from across the movements into the seam discipline the
agentic-work layer is built on, so it is read early — as the discipline the
later work assumes.

## Derivation

This section is the single home of the corpus's derivation: one
governing fact, four axes, and the topology, the derived-relations
register, and the center as consequences — each with its chain and its
citations into the corpus. It derives and links [§Topology](#topology);
the topology table remains the single home of the movement and member
listing.

### The governing fact

> **Every work passes onward: those who receive it — to verify it,
> build on it, or change it — hold only what the work itself carries.**

The corpus states this fact member by member; the derivation names it
once. Its roots: a claim "must keep telling the truth after its
author's context is gone" (`principles/positive-form.md` §The
universal); the recipient enumerated as "a future instance of the maker
crossing a context boundary" and "an external contributor landing
cold" (`principles/transmission.md` §The universal); "Durable work survives its maker's absence"
(`compositions/completed-noticing.md` §What the composition itself
owns); "any system with minimal supervision" and "Leave no known
defect depending on private memory"
(`principles/obligation-to-dissent.md` §The universal, §Corrective);
"A copy is a promise of synchronization that nothing enforces"
(`principles/single-home.md` §The universal); "Participants cannot
self-organize, reviewers cannot evaluate, and a system cannot enforce
its own contracts" when done is an assertion
(`principles/verifiable-completion.md` §The universal); "Readers,
human and machine, build on what the surface signals"
(`principles/honest-signal.md` §The universal); debt that "compounds
against a larger future surface and more future hands"
(`principles/evolvability.md` §The universal).

**The master demand** — the fact's first consequence. If the receiver
holds only what the work carries, then every warrant — for a claim, an
element, a boundary, an order, a completion — must be carried by the
work's substrate, checkably, or it does not exist for the receiver.
Nothing sound may rest on what only the maker holds. The corpus states
the demand locally: the Traceability ↔ Verifiable Completion kin gloss
carries it verbatim — "nothing asserted beyond what can be audited"
(`principles/traceability.md` §Relations).

### The four axes

The master demand differentiates along four axes. Parsimony governs
the set: each axis earns its place by the consequences below that
require it, and nothing beyond what the fact entails is introduced.

**A1 · Crossing direction (intake ↔ delivery).** The fact places every
work between the reality it answers to and the reality it lands in;
the receiving reality therefore appears at both ends of the crossing —
as authority and as destination. *Roots:*
`principles/grounding.md` §Projections, *the recipient is ground
truth* ("The humans and systems that consume the work are the
authoritative signal"); `principles/transmission.md` invariant ("Work
completes when the recipient can act on it"); §Topology ("each
produces the ground the next requires").

**A2 · Standing ↔ moving (the artifact and the act).** Every demand
has a standing face — what the substrate holds — and a moving face —
the act that produces or uses it. The receiver meets only the standing
face, but soundness is made in motion, so both faces carry the demand.
*Roots:* `principles/traceability.md` §The universal ("Reasoning has a
static face and a dynamic face") and §Relations ("The pair parallels
Evolvability ↔ Recursive Improvement: one invariant seen from two
aspects"); `principles/grounding.md` §Relations ("position and
momentum… Two faces of one act");
`principles/recursive-improvement.md` §Relations ("the same loop seen
from its two sides").

**A3 · Present ↔ forward (whose cost).** The work's weight is paid
twice: by the present, which carries every element now, and by the
future hands the fact installs — who inherit every shortcut without
the maker's context, which is exactly why forward debt is dear.
*Roots:* `principles/parsimony.md` §Relations ("bounds the same axis
from opposite sides — the shape is demanded by the need, including the
need to keep changing"); `principles/evolvability.md` invariant ("debt
does not flow forward") and §The universal ("more future hands").

**A4 · Site of assertion.** The master demand lands wherever something
is asserted: a surface asserts an identity or capability; a completion
claim asserts done-ness; an inference chain asserts a conclusion; a
consultation asserts the authority's content. One demand × N sites.
*Roots:* `principles/honest-signal.md` §Relations ("the same
truth-telling demand at two sites");
`principles/verifiable-completion.md` §Relations ("nothing asserted
beyond what can be audited, at two sites");
`principles/single-home.md` §Relations ("the same move in two
domains").

### The topology as consequence

The four movements are the master demand differentiated along **A1**,
read across one crossing:

- **Intake — Movement I.** The authorities the work answers to exist
  outside the maker: the need (Grounding), the chain to ground
  (Traceability), the owner (Sovereignty), the prior stage (Sequence).
  The movement's question names exactly this: "What is true, and who
  owns what?"
- **Encoding — Movement II.** The answer's warrant is carried by the
  artifact itself. The movement's question lists its members 1:1 —
  *earned* (Parsimony), *single* (Single Home), *stated as itself*
  (Positive Form), *durable* (Evolvability).
- **Between crossings — Movement III.** The carried warrant stays true
  without supervision: surfaces true (Honest Signal), producers
  repaired (Source Repair), seen problems owned rather than held
  privately (Obligation to Dissent), the producing process itself
  improving (Recursive Improvement).
- **Delivery — Movement IV.** The crossing completes as a fact on the
  receiver's side. The movement's question maps 1:1 — *the recipient
  can act* (Transmission), *completion is a fact* (Verifiable
  Completion).

**The order.** I→II→III→IV is derived, not arranged: an answer cannot
be encoded before what it answers to exists; only a truth-carrying
form can be kept true; what is handed over is the kept-true artifact.
The order-carries-meaning claim is Sequence's own invariant applied to
the corpus itself — the topology self-exemplifies the principle it
contains (`principles/sequence.md` invariant; §Topology, "each
produces the ground the next requires").

**The diagnostics as corollaries.** §Topology's remove-a-movement
diagnostics follow from this derivation, one per leg: no intake →
locally coherent, unanchored ("elegant fiction… The system cannot
see"); no encoding → the warrant is not carried by the artifact
("sprawl - unearned weight, duplicated truth, forward debt"); no
keeping-true → the carried warrant decays unsupervised ("decay… The
system rots"); no delivery → the crossing never completes ("waste - work
that never ships, or ships as assertion instead of fact"). Each
named failure matches its leg's removal 1:1 (§Topology, diagnostic
list).

**The adopted form, validated.** §Topology adopts the four-movement
form from the source registers (`SOURCES.md` §Register 4). This
derivation re-derives the form from the fact, and the same four
movements in the same order emerge — the import is validated exactly
per Grounding's corrective: "if the same answer emerges, the import is
validated" (`principles/grounding.md` §Corrective). Derive-then-diff
is the validation move of record.

### The derived-relations register

The register documents the corpus's live derived edges at this head:
each edge derived once, at its axis — or, for the loop-closure row,
from the fact directly. Cluster dispositions move member documents and
this register together.

| Edge | Axis | Chain | Citations |
|---|---|---|---|
| **dual** — Grounding ↔ Traceability | A2 | The ground-truth demand's two faces: standing = position established, what is true and needed, fixed before reasoning departs; moving = every subsequent inference keeps its anchor to that position. The edge prose states the axis itself. | `principles/grounding.md` §Relations ("position and momentum… Two faces of one act"); `principles/traceability.md` §The universal, §Relations |
| **dual** — Evolvability ↔ Recursive Improvement | A2 | The cheap-next-change demand's two faces: standing = the seams built into the artifact (design-time); moving = the loop that uses them (runtime). The corpus itself declares the two duals parallel — one axis, two instances. | `principles/evolvability.md` §Relations; `principles/recursive-improvement.md` §Relations; `principles/traceability.md` §Relations ("The pair parallels…") |
| **dual (tension)** — Parsimony ↔ Evolvability | A3 | One axis — on whom the weight falls — bounded from opposite ends: weight unearned by a present verified need (Parsimony forbids) and weight transferred forward as debt (Evolvability forbids); "enough" is the bounded interior. The `tension` annotation itself is derived here: "the two aspects bound an axis from opposite sides" is generated by A3. | `principles/parsimony.md` §Relations; `principles/evolvability.md` §Relations; §Relationship taxonomy, `dual (tension)` fold |
| **kin** — Honest Signal ↔ Verifiable Completion | A4 | The master demand at two sites: what a surface *says* answers to its substance; what a claim *asserts* answers to evidence run first. The gloss states it: "the same truth-telling demand at two sites." | `principles/honest-signal.md` §Relations; `principles/verifiable-completion.md` §Relations |
| **kin** — Traceability ↔ Verifiable Completion | A4 | Two sites: the reasoning chain; the completion claim. The gloss carries the master demand verbatim — "nothing asserted beyond what can be audited." | `principles/traceability.md` §Relations; `principles/verifiable-completion.md` §Relations |
| **isomorphism** — Grounding (*read the manual*) ↔ Single Home (*consult, don't model*) | A4 | Two sites: cognition's intake of an authority; enforcement's consultation of an authority — in both, assert only what the consulted authority warrants. | `principles/grounding.md` §Projections, §Relations; `principles/single-home.md` §Corollaries, §Relations |
| **kin** — Grounding ↔ Transmission | A1 | The receiving reality appears at both ends of the crossing: as the authority that decides what to make (Grounding's *recipient is ground truth*) and as the destination the artifact must land in (Transmission). One reality, intake and delivery readings; the projection already carries the cross-edge. | `principles/grounding.md` §Projections ("Edge to Transmission"), §Relations; `principles/transmission.md` §Relations |
| **kin** — Grounding ↔ Contract-First | the fact (loop-closure) | A warrant the substrate carries checkably is, for the next party, *territory*: the delivered contract is the successor's ground. This edge is the seam where one turn's Land becomes the next turn's Ground. The gloss states it: "a contract in the substrate is reality, not residue — a consumer grounds in it as territory." | `principles/grounding.md` §Relations; `compositions/contract-first.md` §Relations |

Two taxonomy consequences of the register are recorded here and
decided elsewhere: the `tension` annotation is now derived (row 3)
rather than sanctioned ad hoc, and A4 generates kin ("same demand, two
sites") and isomorphism ("same move, two domains") by one mechanism —
whether the two labels stay separately earned is a taxonomy call homed
at the epic's C5 unit.

### The center

The fact holds at every crossing, so the receiver of one turn is the
maker of the next: the four movements close into a loop. Recursive
Improvement converts cycle into gain — "refinement plus propulsion, a
circle that moves forward" (`principles/recursive-improvement.md` §The
universal) — and the loop is the spiral §Topology names as the center.
The center is a **consequence** of the fact, not a member.

Completed Noticing is the loop's **per-act projection**. Its
constituent set — Grounding, Verifiable Completion, Obligation to
Dissent, Transmission, Recursive Improvement, Sequence — spans
Movements I, III, and IV and contains no Movement II member, so it is
not the four-movement traversal itself; its own kin edge states the
true relation — "the four movements traversed as one turn of this
cycle" — the loop read at the scale of a single act
(`compositions/completed-noticing.md` §The cycle, §Relations;
§Topology, center text; `ontology.yaml` `topology.center`).

The `topology:center` pseudo-node's mechanical disposition is homed at
the epic's C5 unit.
