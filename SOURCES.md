# Source Coverage Map

Every item in the five source registers — the four named by
[pentaxis93/principles#1](https://github.com/pentaxis93/principles/issues/1)
and a fifth discovered after the synthesis
([pentaxis93/principles#2](https://github.com/pentaxis93/principles/issues/2)) —
classified as exactly one of:

- **ascended** — its content was raised to its universal level and lives
  in a canonical principle (possibly merged with sibling statements of
  the same invariant);
- **projection** — attached as a domain projection or corollary inside
  the named universal's document;
- **retained** — a genuine decision or design artifact; it stays in its
  home and is not a principle (it may still *instantiate* principles,
  noted where true);
- **out of scope** — not corpus material, with the reason stated.

The reverse traversal lives in the principle documents themselves: each
universal's **Sources** section links back to every register item that
shaped it.

Invariants that recurred across the registers and consumer methodology
and ascended after the founding synthesis are classified in their own
**post-synthesis ascent** sections below, with the same vocabulary.

## Register 1 — `tesserine/commons/PRINCIPLES.md` (7 principles + topology)

| Item | Classification | Destination |
|---|---|---|
| 1. Sovereignty | ascended | [Sovereignty](principles/sovereignty.md) |
| 2. Sequence | ascended | [Sequence](principles/sequence.md) |
| 3. Grounding | ascended | [Grounding](principles/grounding.md) |
| 4. Obligation to Dissent | ascended | [Obligation to Dissent](principles/obligation-to-dissent.md) |
| 5. Recursive Improvement | ascended | [Recursive Improvement](principles/recursive-improvement.md) |
| 6. Transmission | ascended | [Transmission](principles/transmission.md) |
| 7. Verifiable Completion | ascended | [Verifiable Completion](principles/verifiable-completion.md) |
| Compass topology (N/E/S/W + center) | ascended | The four-movement topology supersedes the compass arrangement ([form contract](ONTOLOGY.md#derivation) states why); the compass's named-failure diagnostic and its center claim (the spiral) are retained in the topology section |

## Register 2 — `tesserine/commons/DESIGN-PRINCIPLES.md` (21 design principles)

| Item | Classification | Destination |
|---|---|---|
| 1. Relentlessly replace brittle with robust | projection | [Evolvability](principles/evolvability.md) |
| 2. One mechanism, not two | projection | [Single Home](principles/single-home.md) |
| 3. Eliminate the class, not the instance | projection | [Source Repair](principles/source-repair.md) |
| 4. Computed over stored for derived state | projection | [Single Home](principles/single-home.md) |
| 5. Policy over status tracking | projection | [Parsimony](principles/parsimony.md) |
| 6. Silent code teaches louder than docs | projection | [Honest Signal](principles/honest-signal.md) |
| 7. Trace assumptions to their origin | projection | [Source Repair](principles/source-repair.md) |
| 8. Fixes belong at discovery, not deferred | projection | [Obligation to Dissent](principles/obligation-to-dissent.md) |
| 9. Name what it is, not what you wish it were | projection | [Honest Signal](principles/honest-signal.md) |
| 10. Fail explicitly, never silently | projection | [Honest Signal](principles/honest-signal.md) |
| 11. Ship correct, then optimize | projection | [Honest Signal](principles/honest-signal.md) (corollary *prefer absence to wrongness*) |
| 12. Omit rather than half-implement | projection | [Honest Signal](principles/honest-signal.md) (corollary *prefer absence to wrongness*) |
| 13. Self-maintaining over maintainer-dependent | projection | [Single Home](principles/single-home.md) |
| 14. Spec and implementation are separate scopes | projection | [Sovereignty](principles/sovereignty.md) |
| 15. Ground to needs, not to code | projection | [Grounding](principles/grounding.md) |
| 16. Fix is the default disposition | projection | [Obligation to Dissent](principles/obligation-to-dissent.md) |
| 17. Interfaces describe themselves | projection | [Transmission](principles/transmission.md) |
| 18. Schema is the source; documentation is derived | projection | [Single Home](principles/single-home.md) |
| 19. Uniform patterns across surfaces | projection | [Transmission](principles/transmission.md) |
| 20. Verify before act | projection | [Verifiable Completion](principles/verifiable-completion.md) |
| 21. Mode is a property of the session, not the operation | projection | [Sovereignty](principles/sovereignty.md) |

## Register 3 — `tesserine/commons/adr/` (15 ADRs)

The discriminator (from #1): a **principle** is a domain-neutral
invariant reasoned *from*; a genuine **ADR** records a concrete decision
that *applies* a principle. Consult the Decision's shape, not the label.

| Item | Classification | Destination / reason |
|---|---|---|
| ADR-0001 Sovereignty | ascended | [Sovereignty](principles/sovereignty.md) — its Decision states a durable truth ("every interface has a clean ownership boundary"), not a choice among alternatives |
| ADR-0002 Everything Earns Its Place | ascended | Split as the ADR itself directs ("two disciplines combine here"): entry discipline to [Grounding](principles/grounding.md), removal discipline to [Parsimony](principles/parsimony.md); its present-system/test fragment to [Positive Form](principles/positive-form.md) ([#11](https://github.com/pentaxis93/principles/issues/11)) |
| ADR-0003 Unconditional Responsibility | ascended | [Obligation to Dissent](principles/obligation-to-dissent.md) (projection *unconditional responsibility*) |
| ADR-0004 Compound Improvement | ascended | [Recursive Improvement](principles/recursive-improvement.md) |
| ADR-0005 System Conventions for Cross-Component Artifacts | retained | Genuine decision: commons as spec authority, canonical pair form, versioning and vendoring mechanics. Instantiates [Single Home](principles/single-home.md) and [Sovereignty](principles/sovereignty.md) |
| ADR-0006 Release Discipline for Cargo-Workspace Repos | retained | Genuine decision: cargo-release as canonical tool, the workspace-version invariant. Instantiates [Honest Signal](principles/honest-signal.md) and [Verifiable Completion](principles/verifiable-completion.md) |
| ADR-0007 Day-One Stance | ascended | Distributed at its joints: provisionality and reversible-decision velocity to [Evolvability](principles/evolvability.md); resist-proxies to [Grounding](principles/grounding.md); customer-obsession to [Grounding](principles/grounding.md)/[Transmission](principles/transmission.md). Its Decision states an orientation, not a choice |
| ADR-0008 Component Orthogonality in Session Composition | retained | Genuine decision: the agentd/runa/agent-declaration composition architecture. Its general-principle consequence shaped a [Sovereignty](principles/sovereignty.md) projection |
| ADR-0009 Operator Metrics Convention | retained | Genuine decision: listener separation, exposition format, naming and cardinality policy |
| ADR-0010 Deployment Release Candidates | retained | Genuine decision: immutable RC tags, image-label identity |
| ADR-0011 Ecosystem Release Identity and Ceremony | retained | Genuine decision: the release manifest as canonical identity artifact |
| ADR-0012 Ecosystem Release Version Grammar | retained | Genuine decision: SemVer grammar and the canonical tag regex |
| ADR-0013 Procedure Substrate Discipline | projection | [Source Repair](principles/source-repair.md) (projection *procedure substrate discipline*) — a meta-discipline by its own statement; its Decision is a durable behavioral invariant, not a tool or convention choice |
| ADR-0014 Component-Independent Versioning | retained | Genuine decision: curatorial ecosystem versioning, BOM pattern |
| ADR-0015 Mode Is a Property of the Session | retained | Genuine decision: it binds the runtime's dual-mode contracts. Its principle content enters the corpus via Design Principle 21 → [Sovereignty](principles/sovereignty.md) |

## Register 4 — `pentaxis93/with-claude/_shared/principles.md` (13 principles + topology)

| Item | Classification | Destination |
|---|---|---|
| 1. Grounding | ascended | [Grounding](principles/grounding.md) |
| 2. Read The Manual | projection | [Grounding](principles/grounding.md) (projection *read the manual*; isomorphic to Single Home's *consult, don't model*) |
| 3. Sovereignty | ascended | [Sovereignty](principles/sovereignty.md) |
| 4. Sequence | ascended | [Sequence](principles/sequence.md) |
| 5. Parsimony | ascended | [Parsimony](principles/parsimony.md) — except its "one mechanism" clause, whose invariant ascends to [Single Home](principles/single-home.md) |
| 6. Source Repair | ascended | [Source Repair](principles/source-repair.md); its honest-surfaces clause to [Honest Signal](principles/honest-signal.md) |
| 7. Obligation To Dissent | ascended | [Obligation to Dissent](principles/obligation-to-dissent.md) |
| 8. Recursive Improvement | ascended | [Recursive Improvement](principles/recursive-improvement.md) |
| 9. Design For Evolvability | ascended | [Evolvability](principles/evolvability.md) (merged with §10, the register's own named dual) |
| 10. Scale-Honest Design | ascended | [Evolvability](principles/evolvability.md) (corollary *scale honesty*) |
| 11. Transmission | ascended | [Transmission](principles/transmission.md) |
| 12. Verifiable Completion | ascended | [Verifiable Completion](principles/verifiable-completion.md) |
| 13. Consult, Don't Reimplement | projection | [Single Home](principles/single-home.md) (corollary *consult, don't model*), carrying its soundness-condition edge to [Verifiable Completion](principles/verifiable-completion.md) |
| Four-movement topology (Ground/Shape/Protect/Land) | ascended | Adopted as the corpus topology ([form contract](ONTOLOGY.md#derivation) states why), extended with the compass's failure diagnostics |
| Feedback-loop footer (`asset:principles` route) | ascended | Relocated: future corpus friction is filed against this repository ([README](README.md#evolving-this-corpus)) |

## Register 5 — `tesserine/groundwork` `skills/reckon/SKILL.md` §Navigational Principles (5 principles + preamble)

Discovered after the synthesis
([#2](https://github.com/pentaxis93/principles/issues/2)): reckon names
five "first principles you reason FROM during reconstruction" —
principle-shaped by this corpus's own discriminator. The downstream
repair (reckon consults this corpus instead of carrying a second
editable register) is
[tesserine/groundwork#387](https://github.com/tesserine/groundwork/issues/387),
gated on this classification landing.

| Item | Classification | Destination / reason |
|---|---|---|
| Preamble ("select during Orient... fire during Reconstruct") | retained | Skill deployment mechanics — reasoned *with*, not *from*; its "constants that govern, not goals to optimize" clause restates this corpus's own discriminator |
| 1. Parsimony | ascended | [Parsimony](principles/parsimony.md) — the razor: among rival explanations or designs meeting the same constraints, fewer moving parts wins until a constraint demands more. Its "one mechanism over two" wording is a homonym of [Single Home](principles/single-home.md)'s *one mechanism, not two* (two loci that must agree); reckon's statement carries no agreement obligation — its corrective is removal, not unification — so Parsimony owns it (border derived once in [ONTOLOGY.md §The derived-relations register](ONTOLOGY.md#the-derived-relations-register)) |
| 2. Elegance | projection (split) | Derivation clause ("structure arises from the problem, not the designer's habits or adjacent examples") → [Grounding](principles/grounding.md), projection *form follows the problem*; isomorphism clause ("nothing is imposed") → [Parsimony](principles/parsimony.md)'s existing *elegance* face |
| 3. Sufficiency | ascended | [Parsimony](principles/parsimony.md) — a sibling statement of the universal's disciplined-completeness clause ("disciplined completeness" appears verbatim in both); its "each unjustified element is a carrying cost" sharpening absorbed |
| 4. Traceability | ascended | [Traceability](principles/traceability.md) — **new universal** (Movement I, dual with [Grounding](principles/grounding.md)). Not attachable as a corollary because not derivable: reckon's *grounded-then-analogical* corruption mode documents reasoning that satisfied Grounding fully and still failed ("correct position, analogical momentum"), and no existing universal's recognition catches mid-chain drift |
| 5. Independence | ascended | [Grounding](principles/grounding.md) — the invariant generalized laterally: an adjacent problem's solution is evidence about another need's attempt, not a template for this one; re-derivation is the validation test |

## Post-synthesis ascent — Positive Form ([#11](https://github.com/pentaxis93/principles/issues/11))

One invariant recurred as fragments across the registers and the
consumer methodology documents; it ascended as the fourteenth universal,
[Positive Form](principles/positive-form.md). The items that carried it:

| Item | Classification | Destination / reason |
|---|---|---|
| commons ADR-0002, present-system/test fragment ("documents and comments describe the present system; tests verify what the system does") | ascended | [Positive Form](principles/positive-form.md) — moved home from [Parsimony](principles/parsimony.md)'s "No speculative abstraction" projection, where it first landed; lives there now as the *present-system documentation* projection |
| with-claude [`_shared/methodology/document-register.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/methodology/document-register.md), the restate-forwards move | projection | [Positive Form](principles/positive-form.md) (projection *restate forwards*); the methodology document comes to reference the universal (follow-on filed in with-claude) |
| work-unit-craft (groundwork [`skills/work-unit-craft/SKILL.md`](https://github.com/tesserine/groundwork/blob/main/skills/work-unit-craft/SKILL.md), consumed by with-claude's local issue-craft station layer), *negative-criteria* and *governance-narrative* corruption modes | projection | [Positive Form](principles/positive-form.md) (projection *positive acceptance criteria*); the methodology documents come to reference the universal through the canonical craft home |
| with-claude [#103](https://github.com/pentaxis93/with-claude/issues/103) / [#104](https://github.com/pentaxis93/with-claude/issues/104), the negative-exception-framing audit | ascended | [Positive Form](principles/positive-form.md) — the audits' invariant (carve-outs stated as exceptions restate as positive firing conditions) is absorbed into the universal's boundary clause |
| babbie-ops [#54](https://github.com/pentaxis93/babbie-ops/issues/54), the contract test positively asserting the corrected boundary | projection | [Positive Form](principles/positive-form.md) (projection *assert the corrected boundary*) |

## Post-synthesis ascent — Play to Learn ([#5](https://github.com/pentaxis93/principles/issues/5))

A game stance inspired by E.J. Gold's game-as-practice teaching was
surfaced as a candidate
principle and was already load-bearing in consumer methodology
(with-claude `agent-governance.md`'s regeneration-count vow) but had no
corpus home. The reckon's disposition is recorded here.

| Item | Classification | Destination / reason |
|---|---|---|
| Win-or-learn game stance, distilled from E.J. Gold's game-as-practice teaching (to win, or to learn — not both at once) | projection | [Grounding](principles/grounding.md) (projection *play to learn, not to win*). **Not a universal.** The bare mutual-exclusivity claim is a fork with no chosen tine — it states a tension without binding a stance, so it carries no normative content for an agent; and as a hard law ("never both") it is a vivid heuristic, not a domain-neutral invariant (deliberate practice blends the two). The agent-relevant content is the *bias toward the learn-frame where the work needs a grounded diagnosis*: the outcome-metric is a proxy and is not an input to the play. That bias is [Grounding](principles/grounding.md)'s *resist proxies* family applied to attentional stance, so it attaches as a projection rather than ascending. Consumer instance: with-claude `agent-governance.md`'s regeneration-count vow (the count is the win-surface). A second consumer is queued — with-claude [#100](https://github.com/pentaxis93/with-claude/issues/100), a gamified compliance lever, which is the win-frame turned into a design tool and carries this projection's caution |

## Post-synthesis ascent — Contract-First ([#23](https://github.com/pentaxis93/principles/issues/23))

The contract — the explicit, checkable seam between two parts, declared in
the substrate and verified against — is homed as a named composition
document, [Contract-First](compositions/contract-first.md): a discipline of
four existing universals carrying composition-level content no constituent
edge holds (the contract as the unit of agentic composition, and the
force-and-time to energy-state isomorphism). The form was reckoned as a
composition rather than a new universal — its invariant decomposes into
existing universals acting together. It introduces no new register item;
each item it assembles is already classified above. Its coverage, by role in
the composition:

| Already-classified item | Home (per above) | Role in Contract-First |
|---|---|---|
| commons ADR-0001 Sovereignty; DESIGN-PRINCIPLES §14 (spec/impl separate scopes) | [Sovereignty](principles/sovereignty.md) | constituent — the declared WHAT/HOW boundary the contract realizes |
| commons DESIGN-PRINCIPLES §18 (schema is the source) | [Single Home](principles/single-home.md) | constituent — the declaration as the one authoritative locus of the seam |
| commons DESIGN-PRINCIPLES §20 (verify before act) | [Verifiable Completion](principles/verifiable-completion.md) | constituent — each side verified against the declaration, not its own report |
| commons PRINCIPLES §2 (behavior before implementation — BDD) | [Sequence](principles/sequence.md) | constituent — built to the declaration; BDD is its behavioral form |
| commons DESIGN-PRINCIPLES §17 (interfaces describe themselves) | [Transmission](principles/transmission.md) | related — the self-describing surface is the contract told truthfully; kin via [Honest Signal](principles/honest-signal.md) |
| commons ADR-0015 Mode Is a Property of the Session | retained (Register 3) | the dual-mode session contracts instantiate this composition; its principle content already reaches the corpus via Design Principle 21 → Sovereignty |

## Inbound change-vectors resolved natively

Two open with-claude reckons were resolved by this synthesis rather than
left as later enrichment, per #110's direction:

| Item | Resolution |
|---|---|
| [with-claude#91](https://github.com/pentaxis93/with-claude/issues/91) — principle interrelationships want a curated, evolving structure | The corpus's typed relationship taxonomy ([form contract](ONTOLOGY.md#relationship-taxonomy)) and per-principle **Relations** sections are that structure: present-tense, curated, not ADR-shaped |
| [with-claude#96](https://github.com/pentaxis93/with-claude/issues/96) — single home as the evolvability boundary | Its open question ("new principle or enrichment edge?") resolves as: the evolvability-boundary argument is the second rationale of the ascended universal [Single Home](principles/single-home.md), and its bridge to the spiral is the **enables** edge to [Recursive Improvement](principles/recursive-improvement.md) |
