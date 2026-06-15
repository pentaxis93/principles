# Sovereignty

**Movement:** I — Ground · [Index](../README.md)

> **Invariant:** Every boundary divides ownership cleanly: one side owns
> what must be true, the other owns how it becomes true.

## The universal

At every interface between two parties — director and executor, producer
and consumer, layer and layer — each concern has exactly one owner, and
neither side crosses. Direction declares outcomes, constraints, and
consequence surfaces; execution owns path, mechanism, and craft.
HOW-ownership means full judgment and artistry, not mechanical
compliance: the executor interprets, not transcribes.

The principle is fractal. It applies at every scale of interface:
human and agent, component and component, specification and
implementation, stage and stage. When the boundaries hold, maximum
output emerges from minimum input. When they blur, corruption is
symmetric — domination by either side breaks the system. A direction
that smuggles in procedure produces faithful execution of the wrong
thing; an executor that withholds judgment produces compliance instead
of craft.

Authority attaches to the authorized role at the correct boundary, never
to the mechanical act that invokes an operation. Who pressed the key,
launched the shell, or issued the call does not change who owns the
decision.

**Recognition:** A direction names which file, function, pattern, or step
to use when the actual constraint is an outcome. An executor follows the
words while withholding judgment about whether the words serve the end. A
component reaches into another component's named surface. An action is
routed to the wrong owner — most often handed *up* when it was the
executor's to perform.

**Corrective:** Restate the claim as what must be true and what must not
break. Leave the path to the owner of the path, and require judgment from
that owner. Having recognized a situation, name whose action the response
is before taking or offering it.

## Projections

### Declarative framing *(communication)*

Specify outcomes and constraints, not procedure. Declarative framing is
the communication discipline that expresses sovereignty: say what should
be true, not what steps to take. This is the procedural axis — an
ownership claim about who holds WHAT and who holds HOW; how the WHAT
itself is encoded — the negation and history axes — belongs to
[Positive Form](positive-form.md).
— *Source: commons `PRINCIPLES.md` §1; the axis boundary is corpus
synthesis ([#11](https://github.com/pentaxis93/principles/issues/11)).*

### Specification and implementation are separate scopes *(work design)*

A boundary spec defines the interface; the work to implement it is a
separate scope. Mixing them confuses executors — the reader cannot
distinguish constraints from descriptions.
— *Source: commons `DESIGN-PRINCIPLES.md` §14.*

### Each component owns the surface that bears its name *(architecture)*

When a component writes another component's file formats, serializes
another's structures, or expects an operator to stitch together concerns
that should be infrastructure, sovereignty has blurred. The corrective is
to name each surface cleanly and let each component own what its name
implies.
— *Source: commons ADR-0008 (retained as a genuine decision; its
general-principle consequence ascends here).*

### Mode is a property of the session, not the operation *(execution modes)*

Operations carry the same semantics, contracts, and validation regardless
of who issues them — a human driving interactively or an autonomous loop.
Mode changes who issues the verbs and at what checkpoint granularity,
never the verbs' meaning or authority model. Authorization lives in the
authorization, not in the mechanical act of invocation.
— *Source: commons `DESIGN-PRINCIPLES.md` §21; commons ADR-0015 (retained;
it binds the runtime contracts that apply this projection). Edge to
[Single Home](single-home.md): one validated surface serves all callers,
so the architecture cannot fork into a validated path and a route around
it.*

## Relations

- **enables** — [Transmission](transmission.md): a clean WHAT lets the
  recipient own their HOW; a blurred one forces them to reconstruct the
  maker's intent.
- **composition** — Safe Delegation : [Sovereignty](sovereignty.md) ∘
  [Verifiable Completion](verifiable-completion.md); the owner of WHAT
  verifies outcomes instead of supervising steps.
- **composition** — [Contract-First](../compositions/contract-first.md):
  the contract is the structural realization of Sovereignty's WHAT/HOW
  boundary, declared as a surface where only what must cross is named and
  each side's HOW stays its own.
- **kin** — [Positive Form](positive-form.md): declarative framing is
  the procedural axis — who holds WHAT and who holds HOW. Positive Form
  owns how the durable WHAT itself is encoded.

## Sources

- `tesserine/commons` [`PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/PRINCIPLES.md) §1 (Sovereignty)
- `tesserine/commons` [ADR-0001](https://github.com/tesserine/commons/blob/main/adr/0001-sovereignty.md) (principle-shaped; ascended here)
- `tesserine/commons` [`DESIGN-PRINCIPLES.md`](https://github.com/tesserine/commons/blob/main/DESIGN-PRINCIPLES.md) §14, §21
- `tesserine/commons` [ADR-0008](https://github.com/tesserine/commons/blob/main/adr/0008-clean-session-ownership.md), [ADR-0015](https://github.com/tesserine/commons/blob/main/adr/0015-mode-is-a-property-of-the-session.md) (retained decisions that shaped projections)
- `pentaxis93/with-claude` [`_shared/principles.md`](https://github.com/pentaxis93/with-claude/blob/main/_shared/principles.md) §3 (Sovereignty)
