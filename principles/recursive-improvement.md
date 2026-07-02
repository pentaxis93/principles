# Recursive Improvement

**Movement:** III — Protect · [Index](../README.md)

> **Invariant:** Every operation improves both the object and the process
> that produced it.

## The universal

Work acts on two levels. The object is the immediate artifact; the
process is the machinery — workflows, designs, documents, habits — that
produced it. Single-level work, improving only the object, lets process
defects compound under the surface: the same class of bug recurs, the
next artifact is equally painful to make. Work that only studies the
process never lands. The system gets better at getting better, or it
decays; there is no steady state.

The engine is the recursive spiral — refinement plus propulsion, a
circle that moves forward. Friction with an asset becomes recorded
change material; the important changes are claimed; the asset evolves as
a unit. This principle operates on all the others, including itself: it
is the corpus's immune system against its own stagnation.

**Recognition:** You finish the immediate artifact while preserving the
workflow, document structure, or substrate defect that made the work
harder or less honest.

**Corrective:** After any unit of work, ask: did this address both the
immediate thing and the process that produced it? Capture process
friction at the level that can fix it; if it blocks honest progress,
repair before continuing; if not, record it so the spiral can promote
it.

## Projections

### Fix the bug and what admitted it *(software maintenance)*

The bug is the object; the gap in testing, validation, or design that
admitted it is the process. A bug fix without a process improvement is
half the work. The same doubling applies to capabilities: if adding one
was painful, the pain is signal — improve the extension mechanism too.
— *Source: commons ADR-0004 (Compound Improvement), principle-shaped and
ascended here.*

### Refactoring is the process half *(craft)*

Refactoring is not extra work; it is the process-level half of every
task. If the code you touched is cleaner than when you found it, you did
both levels.
— *Source: commons ADR-0004.*

## Relations

- **dual** — [Evolvability](evolvability.md): border derived once at
  A2, standing ↔ moving
  ([derived-relations register](../ONTOLOGY.md#the-derived-relations-register)).
- **enabled-by** — [Single Home](single-home.md): the spiral acts on a
  bounded asset; a thing without a single home cannot accumulate
  friction in one place and so cannot evolve as a unit.
- **enabled-by** — [Obligation to Dissent](obligation-to-dissent.md):
  surfaced friction supplies the spiral's raw material; swallowed
  friction starves it.
- **enabled-by** — [Source Repair](source-repair.md): directed repair at
  the producer turns object-work into process-work, giving the spiral
  process material to compound.
- **composition** —
  [Completed Noticing](../compositions/completed-noticing.md): the
  spiral is the cycle's Repeat move — residue exposed to the next turn.

## Sources

- `tesserine/commons` [`PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/PRINCIPLES.md) §5 (Recursive Improvement)
- `tesserine/commons` [ADR-0004](https://github.com/tesserine/commons/blob/main/adr/0004-compound-improvement.md) (principle-shaped; ascended here)
- `pentaxis93/with-claude` [`_shared/principles.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/principles.md) §8 (Recursive Improvement)
