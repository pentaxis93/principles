# Honest Signal

**Movement:** III — Protect · [Index](../README.md)

> **Invariant:** Every surface tells the truth about what it is, what it
> does, and what it supports.

## The universal

Systems teach their readers through their surfaces — names, behaviors,
failure modes, reported identities — and those lessons outweigh any
disclaimer written beside them. A surface that silently accepts a
condition models that condition as acceptable. A name that borrows
prestige teaches a shape the system does not have. A degradation path
that hides failure teaches that a capability exists where none does.
Readers, human and machine, build on what the surface signals; when the
signal is false, everything built on it inherits the falsehood.

Honest systems therefore make wrong assumptions fail at the surface that
creates them: explicitly, immediately, where the false signal would
otherwise originate. Explicit failure is clearer than graceful
degradation, because it prevents downstream work from building on
capabilities that do not exist.

**Recognition:** Code silently accepts a condition the design considers
unsupported. A layer exists only because an adjacent system has one. A
fallback masks an error. A surface reports an identity (a version, a
capability, a status) at odds with its substance.

**Corrective:** Fix the surface that emits the false signal — make the
unsupported explicit, rename to the real shape, fail loudly at the point
of wrongness. Do not add a disclaimer beside a signal that still lies.

## Corollaries

### Prefer absence to wrongness

An absent capability fails honestly; a wrong one lies. Waste is
recoverable — it produces identical output done over; wrongness
propagates silently into everything downstream. So omit rather than
half-implement, and ship correct before optimizing: an optimization that
introduces a correctness gap is a regression, not a saving.
— *Sources: commons `DESIGN-PRINCIPLES.md` §11 (Ship correct, then
optimize), §12 (Omit rather than half-implement).*

## Projections

### Fail explicitly, never silently *(error handling)*

Silent degradation paths create false assumptions about what is
supported. Explicit failure prevents downstream systems from building on
capabilities that don't exist.
— *Source: commons `DESIGN-PRINCIPLES.md` §10.*

### Silent code teaches louder than docs *(codebases)*

Code that silently accepts a condition models it as acceptable. Readers
follow the code's model, not the documentation's disclaimers. When code
and docs disagree about what is supported, fix the code — that is where
the false signal originates.
— *Source: commons `DESIGN-PRINCIPLES.md` §6. Edge to
[Source Repair](source-repair.md): the fix belongs at the emitting
artifact.*

### Name what it is, not what you wish it were *(naming)*

Borrowed prestige inflates architecture; honest naming compresses to the
real shape. If a layer exists only because an adjacent system has one,
it doesn't earn its place.
— *Source: commons `DESIGN-PRINCIPLES.md` §9. Edge to
[Parsimony](parsimony.md).*

### The artifact tells the truth about its identity *(release engineering)*

Every released surface has a version of record whose identity
mechanically matches what the release names: the binary self-reports the
version the tag claims, the image labels the refs it was built from. A
tag pointing at substance that reports a different identity is a lying
surface, and the remediation is to re-emit the truth, not amend the
record.
— *Instances in the wild: commons ADR-0006's workspace-version
invariant, ADR-0010's image labels, ADR-0011's version-of-record rule —
all retained as genuine decisions; each applies this projection to a
concrete release surface.*

## Relations

- **kin** — [Verifiable Completion](verifiable-completion.md): border
  derived once at A4, site of assertion
  ([derived-relations register](../ONTOLOGY.md#the-derived-relations-register)).
- **composition** — Repair at the Emitter :
  [Honest Signal](honest-signal.md) ∘ [Source Repair](source-repair.md);
  the false signal is repaired at the artifact that emits it, not
  annotated where it is noticed.
- **kin** — [Contract-First](../compositions/contract-first.md): the
  contract is a surface that tells the truth about the seam, and a
  declaration that diverges from what each side does is a lying surface.

## Sources

- `tesserine/commons` [`DESIGN-PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/DESIGN-PRINCIPLES.md) §6, §9, §10, §11, §12
- `pentaxis93/with-claude` [`_shared/principles.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/principles.md) §6 (Source Repair — its "honest systems make wrong assumptions fail at the surface that creates them" clause ascends here)
