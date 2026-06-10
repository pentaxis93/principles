# Parsimony

**Movement:** II — Shape · [Index](../README.md)

> **Invariant:** Everything earns its place: the shape of the work is
> demanded by a verified need, not by habit, prestige, or fear.

## The universal

Every element — every line, abstraction, document, state dimension,
process step — traces to a current need or is removed. Parsimony is not
doing less than required; it is disciplined completeness: every real
constraint is met, and nothing unearned is carried forward. An element
that no longer serves today's exigency is debt regardless of how well it
functions.

The familiar engineering maxims are faces of this invariant: YAGNI
(speculative elements are unearned), sufficiency (enough over more), and
elegance (the shape compressed to what the need demands). DRY is kin but
deeper — duplication violates [Single Home](single-home.md), which owns
that argument.

**Recognition:** The solution contains a defensive abstraction, a
compatibility layer, repeated policy, a speculative parameter, or an
element justified by "might need" instead of a current, verified need.

**Corrective:** Ask which verified constraint demands the element. If no
constraint demands it, remove it.

## Projections

### No speculative abstraction, no compatibility layers *(codebases)*

Every abstraction serves a current, concrete use case; when a design
changes, the old design is replaced — no shims, no adapters, no "support
both during transition." Documents and comments describe the present
system; history lives in version control. Tests verify what the system
does, not what it doesn't do.
— *Source: commons ADR-0002 (Everything Earns Its Place), principle-shaped
and ascended here; its grounding half lives in
[Grounding](grounding.md).*

### Policy over status tracking *(system design)*

When a status is always true by convention, enforce it as policy rather
than tracking it as state. This eliminates a state dimension and the
machinery to manage it — the mechanism was never earned.
— *Source: commons `DESIGN-PRINCIPLES.md` §5.*

## Relations

- **composition** — [Grounding](grounding.md) ∘ Parsimony yields
  *everything earns its place*: grounding prevents unearned elements from
  entering; parsimony removes them when they lose their justification.
- **dual (tension)** — [Evolvability](evolvability.md): parsimony forbids
  gold-plating for imagined futures; evolvability forbids under-building
  what is genuinely needed. The pair bounds the same axis from opposite
  sides — the shape is demanded by the need, including the need to keep
  changing.
- **kin** — [Single Home](single-home.md): a duplicate is a special case
  of an unearned element, but duplication's deeper cost (divergence and
  the dissolved evolution boundary) is Single Home's argument.

## Sources

- `pentaxis93/with-claude` [`_shared/principles.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/principles.md) §5 (Parsimony)
- `tesserine/commons` [ADR-0002](https://github.com/tesserine/commons/blob/main/adr/0002-everything-earns-its-place.md) (principle-shaped; ascended here)
- `tesserine/commons` [`DESIGN-PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/DESIGN-PRINCIPLES.md) §5
