# Single Home

**Movement:** II — Shape · [Index](../README.md)

> **Invariant:** Everything shared has exactly one home — one locus that
> is authoritative for it. Every other appearance derives from that home
> or consults it.

## The universal

When one fact, behavior, or asset lives in two places, two things go
wrong, and they are different in kind.

**Soundness.** Two loci that must agree will diverge. Two filters drift,
two sources of truth contradict, a hand-maintained mirror goes stale. A
copy is a promise of synchronization that nothing enforces.

**Evolvability.** A single home is the boundary condition that makes
evolution possible. Improvement acts on a *bounded asset*: friction with
the asset accumulates at one place, the important friction is claimed,
and the asset evolves as a unit. A duplicated thing has no boundary —
friction lands in two places and cannot cohere, so the thing cannot
evolve as a unit. Duplication does not merely risk divergence; it
dissolves the edges that evolution needs to act within.

Stated positively: every shareable thing has exactly one home, and that
home is the boundary within which it is allowed to evolve. Everything
else *consumes* — derives mechanically, or consults at need — and never
keeps an editable second copy.

**Recognition:** Two systems must be kept in sync by discipline rather
than derivation. A check models the thing it checks. A document
paraphrases a contract that exists in authoritative form. A function,
register, or convention is copied into a second editable location.

**Corrective:** Find the single mechanism underneath the two. Name one
home; make every other appearance derive from it or consult it. If two
loci genuinely must both exist, make one authoritative and the
derivation mechanical.

## Corollaries

### Consult, don't model

Where an authority exists, consult it; a model of the authority is not
the authority. A guard that re-derives what its authority already
declares — a copied matrix, a hand-rolled parser for a syntax the
platform parses, a regex standing in for a tool's real behavior — can
pass what the authority rejects and reject what it accepts, while
looking like enforcement. Where the authority can be executed, execute
it; where it is declared, read the declaration. Reserve modeling for
when the authority genuinely cannot be consulted, as a named exception.
This corollary is the *soundness condition* on
[Verifiable Completion](verifiable-completion.md): a gate that does not
consult what governs does not actually verify.
— *Source: with-claude `_shared/principles.md` §13 (Consult, Don't
Reimplement).*

## Projections

### One mechanism, not two *(system design)*

When two systems must agree, make them one system. If a remediation
patches a second filter to match a first, look for the architectural fix
that eliminates the class.
— *Source: commons `DESIGN-PRINCIPLES.md` §2. The same words name a
[Parsimony](parsimony.md) face when nothing must agree — groundwork
reckon's "one mechanism over two" removes an undemanded second mechanism
rather than unifying two loci. The discriminator: must the two agree?
If yes, unify here; if the second is merely unearned, remove it there.*

### Computed over stored *(state)*

If the source of truth is available at query time, derive the answer
instead of storing it. Stored derived state goes stale, creating
consistency bugs and meta-staleness problems.
— *Source: commons `DESIGN-PRINCIPLES.md` §4.*

### Schema is the source; documentation is derived *(interfaces)*

When schema and docs both describe a contract, the schema moves first
and the docs are generated from it — drift becomes structurally
impossible. The direction of derivation is the principle; the format is
implementation.
— *Source: commons `DESIGN-PRINCIPLES.md` §18.*

### Self-maintaining over maintainer-dependent *(architecture)*

Prefer architectures where the system maintains itself: runtime
resolution over build-time embedding, upstream verification over local
verification files. A self-maintaining design beats a
maintainer-dependent one even when it is less elegant, because the
maintainer is a synchronization promise.
— *Source: commons `DESIGN-PRINCIPLES.md` §13.*

### Consume, never duplicate *(shared assets)*

A shared asset — a principles corpus, a methodology, a convention — has
one public home that every consumer refers to. No project keeps an
editable second copy or a separately-maintained distillation; a
distillation that outgrows its source has become a second home.
— *Source: with-claude #96, #110 (the governance practice this corpus
itself exists under). DRY is this projection at the scale of code.*

## Relations

- **composition** — History Lives in Version Control : a durable claim
  is present-only ([Positive Form](positive-form.md)), and history has
  exactly one home — the record — of which a durable document is not one
  (Single Home).
- **enables** — [Recursive Improvement](recursive-improvement.md): the
  single home is the precondition of the spiral, because the spiral's
  unit of action is a bounded asset (with-claude #96's bridge, stated
  natively here).
- **enables** — [Verifiable Completion](verifiable-completion.md):
  consulting the governing authority is the soundness condition for a
  gate; a gate that models its authority instead of consulting it can
  pass what the authority rejects.
- **isomorphism** — the consult-don't-model corollary and
  [Grounding](grounding.md)'s *read the manual* projection are the same
  move in two domains: enforcement consults its authority; cognition
  consults its substrate.
- **composition** — [Contract-First](../compositions/contract-first.md):
  the declaration is the one authoritative surface every layer consults
  or derives from, so the seam's truth keeps a single home.
- **kin** — [Parsimony](parsimony.md): a duplicate is also an unearned
  element, but the dissolved evolution boundary is the deeper cost.

## Sources

- `tesserine/commons` [`DESIGN-PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/DESIGN-PRINCIPLES.md) §2, §4, §13, §18
- `pentaxis93/with-claude` [`_shared/principles.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/principles.md) §13 (Consult, Don't Reimplement)
- `pentaxis93/with-claude` [#96](https://github.com/pentaxis93/with-claude/issues/96) (single home as the evolvability boundary — resolved natively as this principle's second rationale)
