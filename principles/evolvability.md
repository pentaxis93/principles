# Evolvability

**Movement:** II — Shape · [Index](../README.md)

> **Invariant:** Build so the next change is cheap, and never choose what
> makes it dearer: debt does not flow forward.

## The universal

Whatever exists is scaffolding for what comes next — provisional by
default, never a completed thing to be protected. An asset is therefore
built so its own revision is cheap: a templated slot rather than fixed
text, a named seam where the next hand will want to cut, a back-link from
the asset to its own pending changes. Permission to change is not
enablement; an asset can be *permitted* to change and still be *built* to
resist it. The structure should invite the next change, not merely allow
it.

The same invariant governs choice. When weighing a solution that stays
honest and maintainable as the system grows against a cheaper present
shortcut, the deciding axis is the *direction of debt*: a shortcut that
saves effort today by transferring maintenance debt forward compounds
against a larger future surface and more future hands. This is not
license to gold-plate for imagined features — that is
[Parsimony](parsimony.md)'s to forbid. Evolvability forbids the opposite
error: under-building what is genuinely needed with a corner-cut that
erodes.

**Recognition:** You are encoding a current answer as if it were
permanent, with nothing in the structure inviting the next hand to
reshape it. Or you are reaching for an implicit, hand-policed solution
over an explicit, machine-checkable one because it saves effort now —
while knowing the explicit one stays correct as the system multiplies.
Or pressure is building to declare something mature so it can stop
changing.

**Corrective:** Ask what is most likely to change, and build the seam
there. Price choices in the future's terms — the debt a shortcut sends
forward is part of its real cost, weighed at today's decision — and
dose the response: take the easy and elegant gains in durability
freely; reach for the extreme or costly ones only with a compelling
reason. What may never win is the corner-cut that erodes as the system
grows.

## Corollaries

### Decision weight matches reversibility

A decision that can be undone needs forward motion and willingness to
correct, not consensus or certainty. Irreversible or high-blast-radius
decisions are a separate category where slower discipline applies. The
cheapness of changing a decision is the evolvability of that decision —
spend deliberation where change is expensive.
— *Source: commons ADR-0007, "High-velocity decisions on reversible
work."*

### Scale honesty

When the scale ahead will exceed what can be pictured, a convention
policed by hand is a debt instrument: it stays cheap only while the
surface stays small. The goal at that scale is durable compliance, not
maximal enforcement — structural enforcement is one lever toward it,
dosed as [Dosed Compliance](../compositions/dosed-compliance.md)
prescribes, up to the worthwhile frontier: the rung where the next
increment of enforcement costs more than it returns. What the debt
forbids is under-building below that frontier — leaving hand-policed
what visibly erodes as the surface multiplies. And make wrong
assumptions fail at the surface that creates them, so scale cannot
hide them.
— *Source: with-claude `_shared/principles.md` §10 (Scale-Honest
Design); reframed from the maximum gate to the dosed frontier per
[#7](https://github.com/pentaxis93/principles/issues/7).*

## Projections

### Replace brittle with robust *(engineering)*

When you find a solution that works today but will break under pressure,
at scale, or when assumptions change, replace it with a robust one. Do
not accommodate brittleness with workarounds, documentation, or process.
— *Source: commons `DESIGN-PRINCIPLES.md` §1.*

### Design the seam *(asset authoring)*

Lower the activation energy of the next change: a template slot rather
than fixed wording, an explicit reshape marker, a back-link from the
asset to its own change-vectors so the next session need not trust
memory to find them.
— *Source: with-claude `_shared/principles.md` §9 (Design For
Evolvability).*

### Provisionality as default *(stance)*

Nothing is final; nothing is completed to the point where it stops being
available for revision. Proposals to refine or restructure are evaluated
against whether they strengthen the foundation, not against whether they
leave working artifacts alone. Resist declarations of maturity — "done"
as a mode change is stasis wearing a milestone. Constant churn is not the
point: the test is whether a movement strengthens the foundation; if
yes, welcome it; if no, nothing demands it.
— *Source: commons ADR-0007 (Day-One Stance), principle-shaped and
ascended here.*

## Relations

- **dual** — [Recursive Improvement](recursive-improvement.md): border
  derived once at A2, standing ↔ moving
  ([derived-relations register](../ONTOLOGY.md#the-derived-relations-register)).
- **composition** —
  [Dosed Compliance](../compositions/dosed-compliance.md): evolvability
  supplies the floor — the dose rises to the worthwhile frontier
  because under-built conventions erode at scale and the debt flows
  forward. The *scale honesty* corollary was the corpus's first
  instance of the maximized-gate shape; it now states the dosed
  frontier.
- **dual (tension)** — [Parsimony](parsimony.md): parsimony forbids
  speculative weight; evolvability forbids forward debt. Together they
  define "enough": every real constraint met, including the constraint
  that the thing must keep changing.

## Sources

- `pentaxis93/with-claude` [`_shared/principles.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/principles.md) §9 (Design For Evolvability), §10 (Scale-Honest Design) — merged as the design-time and choice-time faces of one invariant, as the register itself names them duals
- `tesserine/commons` [`DESIGN-PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/DESIGN-PRINCIPLES.md) §1
- `tesserine/commons` [ADR-0007](https://github.com/tesserine/commons/blob/main/adr/0007-day-one-stance.md) (principle-shaped; its provisionality and reversibility content ascends here, its proxy and consumer content to [Grounding](grounding.md) and [Transmission](transmission.md))
