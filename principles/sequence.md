# Sequence

**Movement:** I — Ground · [Index](../README.md)

> **Invariant:** Order carries meaning: each stage's output is the next
> stage's required input, and a step earns its place by the failure its
> absence causes.

## The universal

Some moves produce the ground that later moves require: principles before
methodology, reckoning before planning, behavior before implementation,
verification before completion claims. An ordered process is not a menu.
Skipping a stage is not efficiency — the downstream stage receives
malformed input and produces structurally valid but wrongly grounded
output, which is harder to detect than honest failure.

Sequence is not ceremony. A step earns its position because its absence
has a specific failure mode at that boundary; interventions are placed
where their corresponding failures occur. The same discipline that
defends necessary steps removes unnecessary ones: a step that no longer
protects a boundary is deleted or reshaped, not kept out of familiarity.

**Recognition:** You are treating an ordered procedure as a menu, using
later-stage facts to justify earlier-stage framing, or keeping a step
because it is familiar rather than because it protects a boundary.

**Corrective:** Ask what the next move needs as input. Supply that input
before moving on, and remove any step that no longer has a boundary to
protect.

## Projections

### Interventions sit at their failure sites *(process design)*

Each stage of a pipeline exists at a specific position because that
position is where its absence causes damage: grounding fires before
design because inherited framing is the failure mode at that boundary;
behavior specification fires before implementation because vague
specification is the failure mode at that boundary.
— *Source: commons `PRINCIPLES.md` §2.*

### Behavior before implementation *(software construction)*

A failing specification of the desired behavior precedes the code that
satisfies it. Code written first has no ground to be verified against;
the test written after passes immediately and proves nothing.
— *Source: commons `PRINCIPLES.md` §2 (BDD-before-implementation as the
named stage ordering).*

## Relations

- **enables** — [Verifiable Completion](verifiable-completion.md):
  verification-before-claim is sequence applied to the final boundary of
  a unit of work.
- **enabled-by** — [Grounding](grounding.md): grounding supplies the
  input sequence requires at the design boundary; inherited framing is
  the failure mode there.
- **composition** — Contract-First : contract-first face of
  [Sovereignty](sovereignty.md) ∘ [Sequence](sequence.md) ∘
  [Single Home](single-home.md); the contract is the prior stage whose
  output each layer requires.
- **composition** —
  [Completed Noticing](../compositions/completed-noticing.md): the
  cycle's ordering — each move produces the ground the next requires —
  is owned by Sequence.

## Sources

- `tesserine/commons` [`PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/PRINCIPLES.md) §2 (Sequence)
- `pentaxis93/with-claude` [`_shared/principles.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/principles.md) §4 (Sequence)
