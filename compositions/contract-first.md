# Contract-First

**Named composition** · [Index](../README.md)

> **Invariant:** The boundary between two parts is declared explicitly
> and checkably in the substrate; each part is built to the declaration
> and verified against it, not against its own report; the declaration
> is the single home of the seam's truth.

Long form: *declare the seam, build to it, verify against it.* A seam
discipline composed of four existing universals. Each constituent's
content lives in its own document — consult them by link; this document
owns only what no constituent holds: the contract as the unit of agentic
composition, and the constraint-surface formulation that makes that
composition tractable.

## The composition

- **The boundary** — [Sovereignty](../principles/sovereignty.md). The
  contract is the WHAT/HOW boundary realized as a declarative surface:
  only what must cross is declared, and each side's HOW stays its own.
  The contract is the structural realization of Sovereignty — the
  ownership boundary made into a surface a builder reads.
- **The single home** — [Single Home](../principles/single-home.md).
  The declaration is the one authoritative locus of the seam's truth;
  both sides consult it or derive from it, and the seam's truth lives in
  one place.
- **Built to the declaration** — [Sequence](../principles/sequence.md).
  The declaration is the prior stage whose output each side requires: a
  side is shaped to the contract before it is built. Its behavioral form
  is **BDD**, where the declared behavior is the contract the code is
  written to satisfy and verified against.
- **Verified against the declaration** —
  [Verifiable Completion](../principles/verifiable-completion.md). Each
  side's completion is decided by the declaration as evidence: the
  contract is the gate, and a side's own report is not the proof.

## What the composition itself owns

**The contract is the unit of agentic composition.** An agent is handed
a contract — a schema to satisfy, an interface to implement, a behavior
to meet — works to it independently, and is verified against it rather
than against its own report. A system specified as a graph of such
surfaces, with agents mapping one surface to the next, presents a more
stable topology to work against than the imperative path of execution,
and that stability is what makes agentic work tractable. No constituent
alone carries this claim about the whole.

**The energy-state formulation.** Declaring the seam rather than
scripting the path is isomorphic to the move in mechanics from a
force-and-time formulation to an energy-state one: the same system
solved either by integrating forces along a trajectory, or by specifying
states and constraints and letting the dynamics follow — the second far
more elegant, and for constrained systems far simpler. The contract is
the constraint surface; declaring it is the energy-state formulation of
the work.

**The precondition for agentic work.** The agentic-work principles
compose soundly only over a named seam discipline: each assumes a
contract to hand an agent and to verify the agent against. This
composition is that assumption made explicit.

**Recognition:** Work is specified as a trajectory of steps an executor
follows; an executor is accepted on its own report rather than against a
declared surface; or the seam between two parts lives in two places held
in agreement by hand.

**Corrective:** Declare the boundary as a checkable surface in the
substrate, build each side to it, verify each side against it, and keep
the declaration the single home of the seam.

## Failure diagnostic

Each missing constituent corrupts the discipline in a named way:

- *Without Sovereignty:* the declaration carries HOW — it dictates a
  path instead of a boundary, and each side loses its craft.
- *Without Single Home:* the seam lives in two places — declaration and
  copy diverge, and the contract stops being authoritative.
- *Without Sequence:* the build precedes the declaration — there is no
  surface to build to, and the seam is reconstructed after the fact from
  whatever was built.
- *Without Verifiable Completion:* each side is taken on its own report —
  the contract is declared but never the gate, and conformance is
  asserted rather than checked.

## Relations

- **composed-of** — [Sovereignty](../principles/sovereignty.md) · [Single Home](../principles/single-home.md) · [Verifiable Completion](../principles/verifiable-completion.md) · [Sequence](../principles/sequence.md). Each constituent carries the reciprocal **composition** edge.
- **kin** — [Grounding](../principles/grounding.md): a contract in the substrate is reality, not residue — a consumer grounds in it as territory rather than replaying how it came to be.
- **kin** — [Honest Signal](../principles/honest-signal.md): the contract is a surface that tells the truth about the seam; a declaration that diverges from what each side does is a lying surface.
- **kin** — [Parsimony](../principles/parsimony.md): only the WHAT that must cross the boundary is declared — the surface carries nothing the seam does not demand.

## Sources

- [pentaxis93/principles#23](https://github.com/pentaxis93/principles/issues/23) — the candidate and its form decision (a composition of existing universals, not a new universal); the source of record for this document.
- `tesserine/commons` [ADR-0001](https://github.com/tesserine/commons/blob/main/adr/0001-sovereignty.md), [`DESIGN-PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/DESIGN-PRINCIPLES.md) §14 (spec and implementation are separate scopes), §17 (interfaces describe themselves), §18 (schema is the source), §20 (verify before act), [`PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/PRINCIPLES.md) §2 (behavior before implementation — BDD), and [ADR-0015](https://github.com/tesserine/commons/blob/main/adr/0015-mode-is-a-property-of-the-session.md) (the dual-mode session contracts) — the already-classified register items this composition assembles; their per-item classification lives in [SOURCES.md](../SOURCES.md).
