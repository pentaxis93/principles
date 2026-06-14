# Positive Form

**Movement:** II — Shape · [Index](../README.md)

> **Invariant:** A durable claim states what is — in the positive, in
> the present. Description is relative to the thing described alone.

## The universal

Two familiar defects are one disease.

**Negative encoding** — "the system does not do Y" — carries no
information about the system; it fossilizes a past expectation. The
negation is meaningful only relative to the moment someone expected Y:
a temporal trace in disguise.

**Temporal traces** — "originally X; we then moved to Z" — force the
reader to replay history to derive the present state, and the claim is
verifiable only against a substrate that no longer exists.

Both are *author-relative* encodings: they describe the author's
journey to the present, not the present. The positive declarative
present is the only *substrate-relative* encoding — the reader checks
the claim against the thing itself, with nothing else in hand. It is
also the only generative one: a positive statement bounds a finite,
checkable extension and decides cases not yet seen; a negation bounds
an infinite complement and recognizes only the one failure it names.

The principle governs durable registers — documents, criteria,
contracts, principle text — wherever a claim must keep telling the
truth after its author's context is gone. A record holds history
because history is its job; a scope exclusion in an issue is a
decision, not a scar. Apparent exceptions — prohibitions such as
"never log secrets" — restate positively ("every emitted line is
secret-free"), and the positive form is the one a check can verify:
the tell that the principle holds there too. Contrast is not the
defect either: a positive claim may name the nearest confusion to
fence itself off — "say what should be true, not what steps to take" —
and the claim still lives in the positive sentence. The defect is
negation *as* the claim: an assertion whose entire content is an
absence.

**Recognition:** A durable claim leans on "does not," "no longer,"
"previously," "instead of," or "moved away from." A criterion asserts
an absence. A document explains its present shape by narrating its
past shapes.

**Corrective:** Restate the claim as what is true of the present
substrate, verifiable against that substrate alone. Send the history
to version control or the record; send the expectation behind the
negation back to its author.

## Projections

### Present-system documentation *(codebases)*

Documents and comments describe the present system; history lives in
version control. Tests verify what the system does, not what it
doesn't do.
— *Source: commons ADR-0002 fragment, ascended here from
[Parsimony](parsimony.md)'s "No speculative abstraction" projection,
its first landing place.*

### Restate forwards *(principle documents)*

A principle stated forwards — "every X must be Z" — is generative: it
decides cases not yet seen. The same content stated as a failure
case — "X is a defect; the fix is Z" — is brittle, recognizing only
the one failure it describes. The forward statement is the durable
one; the diagnostic half belongs to methodology, the concrete instance
to the record.
— *Source: with-claude
[`_shared/methodology/document-register.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/methodology/document-register.md)
(the restate-forwards move).*

### Positive acceptance criteria *(issue craft)*

Acceptance criteria state what must be true, never what must not
exist. A negative criterion produces tests for the absence of
behavior — implementation-coupled and architecture-distorting — while
a positive criterion that genuinely bounds the outcome already implies
the absence. The same discipline governs the body around the criteria:
an issue carries the decision, not the reasoning journey that produced
it.
— *Source: issue-craft (with-claude
[`_shared/methodology/issue-craft.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/methodology/issue-craft.md)
and the groundwork skill), the* negative-criteria *and*
governance-narrative *corruption modes.*

### Assert the corrected boundary *(contract tests)*

When a defect is repaired, the test protecting the repair positively
asserts the corrected state; merely dropping the stale assertion
verifies nothing, because the absence of the old claim is not a claim.
— *Source: babbie-ops
[#54](https://github.com/pentaxis93/babbie-ops/issues/54).*

## Relations

- **kin** — [Parsimony](parsimony.md): a negative encoding or temporal
  trace is also unearned weight in a document, but the deeper defect —
  author-relativity, the claim that decays when its author's context
  does — is this principle's argument. Parsimony keeps unearned
  abstraction and weight; Positive Form owns how a durable claim is
  encoded.
- **kin** — [Sovereignty](sovereignty.md): its *declarative framing*
  projection (say what should be true, not what steps to take) is the
  procedural axis — an ownership claim about who holds WHAT and who
  holds HOW. The negation axis and the history axis — how the WHAT
  itself is encoded — live here. Both disciplines yield declarative
  sentences; the discriminator is whether the defect crossed an
  ownership boundary or fossilized the author's journey.
- **composition** — History Lives in Version Control : a durable claim
  is present-only (Positive Form), and history has exactly one home —
  the record — of which a durable document is not one
  ([Single Home](single-home.md)).

## Sources

- `tesserine/commons` [ADR-0002](https://github.com/tesserine/commons/blob/main/adr/0002-everything-earns-its-place.md) (the present-system/test fragment; the ADR's entry and removal disciplines live in [Grounding](grounding.md) and [Parsimony](parsimony.md))
- `pentaxis93/with-claude` [`_shared/methodology/document-register.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/methodology/document-register.md) (restate forwards)
- `pentaxis93/with-claude` [`_shared/methodology/issue-craft.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/methodology/issue-craft.md) / `tesserine/groundwork` issue-craft skill (*negative-criteria*, *governance-narrative*)
- `pentaxis93/with-claude` [#103](https://github.com/pentaxis93/with-claude/issues/103), [#104](https://github.com/pentaxis93/with-claude/issues/104) (the negative-exception-framing audit: carve-outs stated as exceptions, restated as positive firing conditions)
- `pentaxis93/babbie-ops` [#54](https://github.com/pentaxis93/babbie-ops/issues/54) (positively asserting a corrected boundary in a contract test)
