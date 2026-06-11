# Verifiable Completion

**Movement:** IV — Land · [Index](../README.md)

> **Invariant:** Completion is an observable state: evidence decides the
> claim, and the evidence comes first.

## The universal

Every unit of work has completion criteria that can be checked
mechanically — by inspection, command, artifact shape, or another
concrete gate. Complete is pass/fail, not subjective and approximate;
"done" is a fact, not a feeling, an assertion, or a confidence level.
Verification precedes the completion claim: the evidence decides the
claim, the claim does not select the evidence.

Without this, nothing downstream holds. Participants cannot
self-organize, reviewers cannot evaluate, and a system cannot enforce
its own contracts when "done" is an assertion. The same invariant
applies before action as after it: a party about to commit to an
operation checks its validity against the governing contract first,
because acting on stale assumptions and cleaning up partial state costs
more than the check — and for autonomous actors, the confusion
propagates into the next act.

**Recognition:** You are about to say work is complete because it reads
well, matches intent, seems obvious, or passed a partial check. Or
acceptance criteria describe activity instead of an observable state.

**Corrective:** Identify the command, inspection, or artifact gate that
distinguishes complete from incomplete. Run it fresh, read the result,
and only then make the claim the evidence supports.

## Projections

### Mechanical completion criteria *(work design)*

Every unit of work carries criteria that are observable and pass/fail:
file gates, typed artifacts, behavior contracts. Acceptance criteria
name an observable state of the world, not a step performed.
— *Source: commons `PRINCIPLES.md` §7.*

### Verify before act *(consumers)*

A consumer constructing a call should be able to check validity before
committing: type-check against the schema, dry-run the operation,
validate the payload against the contract. The cost of the capability is
paid once; the cost of acting on stale assumptions is paid every call.
— *Source: commons `DESIGN-PRINCIPLES.md` §20.*

## Relations

- **soundness condition** — [Single Home](single-home.md)'s
  *consult, don't model* corollary: a gate that models its authority
  instead of consulting it can pass what the authority rejects —
  enforcement theater. A gate verifies only if it consults what
  governs.
- **kin** — [Honest Signal](honest-signal.md): surfaces must not lie;
  claims must not outrun evidence. Same demand, two sites.
- **kin** — [Traceability](traceability.md): evidence decides the claim;
  the chain decides the conclusion. Nothing asserted beyond what can be
  audited, at two sites — completion claims and reasoning.
- **enabled-by** — [Sequence](sequence.md): verification-before-claim is
  sequence applied to the final boundary of a unit of work.
- **composition** —
  [Completed Noticing](../compositions/completed-noticing.md): *verify
  before act* is half of the cycle's Verify move; the evidence-first
  completion claim is half of its Release.

## Sources

- `tesserine/commons` [`PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/PRINCIPLES.md) §7 (Verifiable Completion)
- `tesserine/commons` [`DESIGN-PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/DESIGN-PRINCIPLES.md) §20
- `pentaxis93/with-claude` [`_shared/principles.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/principles.md) §12 (Verifiable Completion)
