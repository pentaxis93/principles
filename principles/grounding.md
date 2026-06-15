# Grounding

**Movement:** I — Ground · [Index](../README.md)

> **Invariant:** Reason from what is needed, not from what exists.

## The universal

Everything that already exists — code, documents, structures, habits, prior
decisions, current behavior — is evidence about one past attempt to meet a
need. It is not the need. The invariant holds laterally as well as
historically: an adjacent problem's solution is evidence about another
need's attempt, not a template for this one — each problem is reasoned
from its own constraints. Grounding distinguishes descriptive truth (what
is) from normative truth (what must be enabled now), and starts generative
work from the normative side. For diagnosis the polarity flips: material
truth — what actually happened, what the artifact actually says — is the
starting point, because diagnosis is about what is, not what ought to be.

The same invariant governs measurement. Tests, milestones, metrics, and
checklists are proxies that stand in for the need; when a proxy and the
need it measures diverge, the need is served and the proxy is repaired.
Satisfying the instrument while the foundation drifts is the
characteristic grounding failure at the system level, just as treating
current behavior as the definition of correct behavior is the
characteristic grounding failure at the artifact level.

Grounding re-fires on every generative act, not once at the start of a
project. The trigger is creation, not position.

**Recognition:** You are organizing the current state, optimizing inside an
inherited frame, treating an existing structure as the definition of what
should exist, working to satisfy an instrument rather than the thing it
measures, or importing a conclusion from an adjacent problem because "we
already solved this."

**Corrective:** Ask: what must this enable, for whom, and what evidence
proves that need? Use the existing substrate only after that answer
exists — as comparison material or diagnostic evidence. Re-derive any
imported solution from this problem's constraints: if the same answer
emerges, the import is validated; if not, it was wrong for this context.

## Projections

### Ground to needs, not to code *(software design)*

Code is current state, not ground truth. Ground to what is needed, then
compare the code to what the needs require. Treating what the system
currently does as the definition of what it should do is the most common
grounding failure.
— *Source: commons `DESIGN-PRINCIPLES.md` §15.*

### Read the manual *(cognition)*

Where an authoritative account of a topic exists, read it before forming
questions, objections, or designs about that topic. Reasoning from priors
where the account exists produces *confident* error — the same mind is
sharp after reading and clueless before, and cannot tell which state it is
in from the inside. The manual is the input grounding depends on. When a
source names its own source, the pointer is an instruction, not a
citation: follow it to the territory.
— *Source: with-claude `_shared/principles.md` §2. Isomorphic to
[Single Home](single-home.md)'s consult-don't-model corollary: the same
move in cognition that the guard makes in enforcement.*

### Form follows the problem *(design)*

Structure arises from the problem, not from the designer's habits or
adjacent examples. The test is isomorphism: the form of the solution
maps to the problem it solves, with nothing imposed from outside the
constraints. A design can look good and fail this test — the shape came
from a familiar pattern, a preferred style, an adjacent architecture —
so the corrective is to derive the structure the problem itself demands,
then compare with what you have.
— *Source: groundwork reckon §Navigational Principles 2 (Elegance), its
derivation clause; the isomorphism's compression face — nothing beyond
what the need demands — is [Parsimony](parsimony.md)'s elegance face.*

### Resist proxies *(process)*

Instruments — tests, CI gates, review checklists, release tags — serve the
foundation they measure. A passing test whose passing required narrowing a
surfaced gap is not success; a failing test that surfaces something real
is not obstruction. Treating instrument satisfaction as the goal destroys
the information channel the instrument exists to provide.
— *Source: commons ADR-0007 (Day-One Stance), "Resist proxies."*

### The recipient is ground truth *(delivery)*

The humans and systems that consume the work are the authoritative signal
for whether it is sound. Internal markers of progress — issues closed,
commits made, tests passing — are proxies. When they disagree with the
consumer's experience, the consumer's experience wins.
— *Source: commons ADR-0007, "Customer obsession." Edge to
[Transmission](transmission.md).*

### Play to learn, not to win *(practice)*

A round is played to win — optimizing the outcome, treating the round as
a means to the score — or played to learn — treating the round as the
object, willing to lose for what the loss reveals. In the moment the two
stances compete: protecting the score suppresses what the round teaches,
and half-holding both yields neither the lesson nor the win. Where the
work needs the learn-frame — the grounded diagnosis, the real lesson of a
run — the salient outcome-metric is not an input to the play. A count, a
tally, a streak, the brighter beckoning thing the mind reaches for: each
is surface, and the surface must not move the stance. The stance is the
constant; the read comes from the substrate, not from the score. This is
the *resist proxies* discipline turned on attention itself — the score is
a proxy for the need, and the moment it captures the play, the need it
stood for is lost.
— *Inspired by E.J. Gold's game-as-practice teaching, distilled here as
the win-or-learn stance. Consumer instance: `pentaxis93/with-claude`
[`_shared/workflows/agent-governance.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/workflows/agent-governance.md)'s
regeneration-count vow, "play the same at level twenty as at level one" —
the count is the win-surface, held out of the diagnosis.*

## Relations

- **dual** — [Traceability](traceability.md): position and momentum.
  Grounding establishes what is true at the start of reasoning;
  Traceability keeps every subsequent inference anchored to it. Two
  faces of one act.
- **composition** — Everything Earns Its Place : grounding prevents
  unearned elements from entering; [Parsimony](parsimony.md) removes
  them when they lose their justification (commons ADR-0002 states this
  composition explicitly).
- **composition** —
  [Completed Noticing](../compositions/completed-noticing.md): grounding
  is the cycle's Attend move, and its diagnostic face is half of Verify.
- **composition** —
  [Dosed Compliance](../compositions/dosed-compliance.md): grounding
  supplies the goal-not-gate move — the gate is an instrument, the need
  is that the property holds.
- **enables** — [Sequence](sequence.md): grounding supplies the input
  sequence requires at the design boundary; inherited framing is the
  failure mode there.
- **isomorphism** — [Single Home](single-home.md)'s *consult, don't
  model* corollary and Grounding's *read the manual* projection are the
  same move in two domains: enforcement consults its authority;
  cognition consults its substrate.
- **kin** — [Transmission](transmission.md): grounding names whose
  reality decides; transmission makes the artifact land in that reality.

## Sources

- `tesserine/commons` [`PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/PRINCIPLES.md) §3 (Grounding)
- `tesserine/commons` [`DESIGN-PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/DESIGN-PRINCIPLES.md) §15
- `tesserine/commons` [ADR-0002](https://github.com/tesserine/commons/blob/main/adr/0002-everything-earns-its-place.md), [ADR-0007](https://github.com/tesserine/commons/blob/main/adr/0007-day-one-stance.md)
- `pentaxis93/with-claude` [`_shared/principles.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/principles.md) §1 (Grounding), §2 (Read The Manual)
- `tesserine/groundwork` [`skills/reckon/SKILL.md`](https://github.com/tesserine/groundwork/blob/main/skills/reckon/SKILL.md) §Navigational Principles 5 (Independence — ascended into the universal's lateral form) and 2 (Elegance, derivation clause — attached as the *form follows the problem* projection)
- Inspired by E.J. Gold's game-as-practice teaching (post-synthesis, [#5](https://github.com/pentaxis93/principles/issues/5)) — distilled as the *play to learn, not to win* projection; consumer instance is `pentaxis93/with-claude` [`_shared/workflows/agent-governance.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/workflows/agent-governance.md)'s regeneration-count vow
