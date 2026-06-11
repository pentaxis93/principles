# Parsimony

**Movement:** II — Shape · [Index](../README.md)

> **Invariant:** Everything earns its place: the shape of the work is
> demanded by a verified need, not by habit, prestige, or fear.

## The universal

Every element — every line, abstraction, document, state dimension,
process step — traces to a current need or is removed. Parsimony is not
doing less than required; it is disciplined completeness: every real
constraint is met, and nothing unearned is carried forward. An element
that no longer serves today's exigency is debt — a carrying cost —
regardless of how well it functions.

The same invariant selects among rival accounts: when two explanations
or designs meet the same verified constraints, the one with fewer moving
parts is correct until a constraint demands more — the extra mechanism
is unearned weight in a theory exactly as in a built thing. This razor
is not [Single Home](single-home.md)'s *one mechanism, not two*, which
unifies two loci that must agree; here nothing must agree — the second
mechanism is simply undemanded.

The familiar engineering maxims are faces of this invariant: YAGNI
(speculative elements are unearned), sufficiency (enough over more), and
elegance (the shape compressed to what the need demands; its derivation
face — form arising from the problem itself — is
[Grounding](grounding.md)'s *form follows the problem* projection). DRY
is kin but deeper — duplication violates
[Single Home](single-home.md), which owns that argument.

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
- **composition** —
  [Dosed Compliance](../compositions/dosed-compliance.md): parsimony
  supplies the dose — an extreme or costly lever earns its place by a
  verified constraint or is not built.
- **kin** — [Single Home](single-home.md): a duplicate is a special case
  of an unearned element, but duplication's deeper cost (divergence and
  the dissolved evolution boundary) is Single Home's argument.

## Sources

- `pentaxis93/with-claude` [`_shared/principles.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/principles.md) §5 (Parsimony)
- `tesserine/commons` [ADR-0002](https://github.com/tesserine/commons/blob/main/adr/0002-everything-earns-its-place.md) (principle-shaped; ascended here)
- `tesserine/commons` [`DESIGN-PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/DESIGN-PRINCIPLES.md) §5
- `tesserine/groundwork` [`skills/reckon/SKILL.md`](https://github.com/tesserine/groundwork/blob/main/skills/reckon/SKILL.md) §Navigational Principles 1 (Parsimony — the razor; its "one mechanism" wording is a homonym of [Single Home](single-home.md)'s projection, disambiguated in both documents), 3 (Sufficiency — a sibling statement of the disciplined-completeness clause), and 2 (Elegance, clause-level: the nothing-imposed compression face)
