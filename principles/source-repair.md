# Source Repair

**Movement:** III — Protect · [Index](../README.md)

> **Invariant:** Repair the artifact that produced the defect, not the
> place where it surfaced — the class, not the instance.

## The universal

A defect observed somewhere was usually produced somewhere else: a wrong
assumption traces to the artifact that taught it; a recurring bug traces
to the design that admits it; an improvised step traces to the procedure
that omitted it. A local workaround can make the immediate task pass
while leaving the producing substrate unchanged — that is not repair, it
is debt transfer to the next reader. Contamination in a seed propagates
through everything grown from it with perfect fidelity.

The repair therefore lands at the origin, and at the level of the class.
When each fix makes a subsystem smarter about one more edge case without
eliminating the class of defect, the question is whether the subsystem
should exist at all. And once the source is repaired, work derived from
the defective substrate is re-derived — a local artifact built on a
known-broken source is not carried forward as authority.

**Recognition:** You are about to patch around a stale document, mirror
logic in a second place, document a caveat instead of fixing the false
signal, solve one instance while leaving the class intact, or convert
missing substrate knowledge into private memory.

**Corrective:** Trace the assumption to the artifact that taught it.
Repair that artifact, then regenerate any downstream work shaped by the
defect.

## Projections

### Trace assumptions to their origin *(review and diagnosis)*

When a reader makes a wrong assumption, trace it back to the code or
artifact that created it. The surface correction is documentation; the
real fix is at the source.
— *Source: commons `DESIGN-PRINCIPLES.md` §7.*

### Eliminate the class, not the instance *(software design)*

When a fix makes a subsystem smarter about one more edge case, ask
whether the subsystem should exist. If the pattern is visible by the
third round, name it — don't wait for the tenth.
— *Source: commons `DESIGN-PRINCIPLES.md` §3. Edge to
[Parsimony](parsimony.md): the strongest class-elimination removes the
mechanism entirely.*

### Procedure substrate discipline *(operations)*

When executing a documented procedure, a gap in that documentation is
substrate work, never a local obstacle to route around. Mid-procedure,
halt and repair the substrate, then resume from artifacts re-derived
from the repaired documentation; post-procedure, file the gap forward as
substrate work. In both cases the invariant holds: future executions
follow the repaired substrate, not informal memory.
— *Source: commons ADR-0013, principle-shaped and attached here as the
projection of Source Repair onto procedure-following work; composed
with [Obligation to Dissent](obligation-to-dissent.md) (the duty to act
on the gap now).*

## Relations

- **composition** — Source Repair ∘
  [Obligation to Dissent](obligation-to-dissent.md): dissent supplies
  the obligation to act on a seen defect; source repair supplies the
  locus where the action lands.
- **composition** — with [Honest Signal](honest-signal.md): the false
  signal is fixed at the artifact that emits it, not annotated where it
  is noticed.
- **enables** — [Recursive Improvement](recursive-improvement.md):
  repairing the producer rather than the product is the move that turns
  object-work into process-work.

## Sources

- `pentaxis93/with-claude` [`_shared/principles.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/principles.md) §6 (Source Repair)
- `tesserine/commons` [`DESIGN-PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/DESIGN-PRINCIPLES.md) §3, §7
- `tesserine/commons` [ADR-0013](https://github.com/tesserine/commons/blob/main/adr/0013-procedure-substrate-discipline.md) (principle-shaped; attached as a projection here)
