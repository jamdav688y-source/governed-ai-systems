# Inter-Agent Communication Protocol (IACP) v1

## Purpose

IACP v1 defines how specialized agents communicate, hand off state, and enforce stage transitions across a distributed psychological-compression system.

The protocol exists to prevent:
- raw-language drift between agents
- premature escalation or conversion
- inconsistent handling of targets across threads
- non-replayable decision paths

The protocol enforces a typed, structured, replayable message model.

---

## Core Principle

No agent communicates with another agent using raw language.

All inter-agent communication must be:
- structured
- typed
- state-bound
- replayable
- stage-aware

---

## Operating Model

Each target moves through a bounded interaction lifecycle:

`ENTRY -> PROBE -> CLASSIFY -> ESCALATE -> CONVERT -> EXIT`

No stage transition is valid unless:
1. current state is recorded
2. transition conditions are satisfied
3. next action is explicitly assigned
4. handoff artifact is valid under schema
5. confidence threshold is met where required

---

## Agent Roles

### 1. Signal Hunter
Detects candidate targets and produces intake records.

### 2. Constraint Mapper
Extracts structural constraints, authority gaps, and linguistic precision blobs (LPBs).

### 3. Classifier Engine
Assigns target type and response mode.

### 4. Dialogue Executor
Generates outbound language aligned to stage, type, and pressure policy.

### 5. Pressure Injector
Introduces controlled asymmetry, missing constraints, or failure invariants.

### 6. Conversion Engine
Activates only when conversion trigger conditions are satisfied.

### 7. Architect Intelligence
Handles peer-level technical alignment and collaboration pathways.

### 8. Cross-Thread Synthesizer
Detects recurring patterns, contradictions, and doctrine-worthy structures.

### 9. Authority Core
Enforces all transition rules and blocks invalid advancement.

---

## Message Unit

The atomic communication primitive is the Agent Message Object (AMO).

Each AMO must contain:
- source and target agent
- target entity identity
- current interaction stage
- state snapshot
- action payload
- classification result
- handoff conditions

No agent may act on unstamped conversational intuition alone.

---

## State Requirements

Every target must maintain a state record containing at minimum:
- target identity
- current type
- current stage
- signal score
- constraint profile
- authority gap
- conversion readiness
- last response type
- assigned agent
- next action

---

## Target Types

### Type A
High signal, high constraint awareness, high ownership pressure.
Typical route: conversion.

### Type B
High signal, medium/high conceptual depth, low ownership pressure.
Typical route: alignment or strategic destabilization.

### Type C
Partial understanding, growing awareness, medium structure.
Typical route: shaping.

### Type D
Curiosity without pressure.
Typical route: filter.

### Type E
Noise.
Typical route: drop.

---

## Stage Definitions

### ENTRY
Target detected. No engagement yet.

**Required fields**
- identity
- source
- initial signal score

**Valid next stages**
- PROBE
- EXIT

---

### PROBE
Initial precision contact to expose structure, pressure, or constraint awareness.

**Goal**
Elicit a response that reveals ownership, uncertainty, or system maturity.

**Valid next stages**
- CLASSIFY
- EXIT

---

### CLASSIFY
Assign target type and next interaction pattern.

**Requirements**
- classification confidence >= configured threshold
- failure surface profile present

**Valid next stages**
- ESCALATE
- EXIT

---

### ESCALATE
Increase pressure only through structured constraint introduction.

**Goal**
Move from abstract discussion to localized system recognition.

**Valid next stages**
- CONVERT
- EXIT
- PROBE (if downgrade required)

---

### CONVERT
Offer bounded diagnostic or collaboration path.

**Requirements**
All of the following must be present:
- ownership signal detected
- uncertainty tied to system
- boundary exposure present

**Valid next stages**
- EXIT
- ESCALATE (if resistance requires softening)

---

### EXIT
No further pressure applied.
Thread is logged as:
- converted
- paused
- filtered
- dropped
- archived for later re-entry

---

## Handoff Rules

### Signal Hunter -> Constraint Mapper
Condition:
- signal_strength >= configured threshold

Payload:
- raw interaction
- target identity
- source metadata

Output:
- LPBs
- candidate failure surfaces

---

### Constraint Mapper -> Classifier Engine
Condition:
- at least one structural constraint detected

Output:
- type classification candidate
- failure surface profile
- authority gap summary

---

### Classifier Engine -> Dialogue Executor
Condition:
- classification confidence >= threshold

Output:
- target type
- stage directive
- tone policy
- pressure ceiling

---

### Dialogue Executor -> Pressure Injector
Condition:
- response contains partial certainty, defense, or unresolved acknowledgement

Output:
- escalation vector
- missing invariant
- recommended injection type

---

### Pressure Injector -> Conversion Engine
Condition:
All must be true:
- ownership signal detected
- uncertainty tied to system
- boundary exposure present

Output:
- conversion packet
- diagnostic framing
- bounded offer recommendation

---

### Conversion Engine -> Exit or Continue
If accepted:
- mark converted
- record engagement outcome
- route to post-conversion workflow

If resisted:
- reduce pressure
- reroute to Dialogue Executor or archive

---

## Validation Gates

### Gate 1 — Structural Validity
AMO must pass schema validation.

### Gate 2 — State Coherence
Proposed stage must be reachable from current stage.

### Gate 3 — Evidence Sufficiency
Required signals for next stage must be present.

### Gate 4 — Pressure Discipline
Outbound message must not exceed pressure ceiling for target type.

### Gate 5 — Replayability
A third party must be able to reconstruct why the transition occurred.

---

## Pressure Policies

### Type A
Use narrow, concrete, system-bound language.
Aim: conversion.
Avoid abstraction surplus.

### Type B
Use one new invariant or one sharpened boundary.
Aim: alignment or destabilization.
Avoid selling.

### Type C
Use structuring language.
Aim: clarify the failure condition.
Avoid premature conversion.

### Type D/E
Minimal effort or no response.

---

## Non-Negotiable Constraints

1. No conversion without trigger.
2. No escalation without evidence.
3. No message without classification.
4. No raw-language handoff between agents.
5. No unstamped state mutation.
6. No pressure increase after signal collapse.
7. No diagnostic offer to peer-alignment targets unless ownership emerges.

---

## Example Target Instantiation

### Faustina
- type: A
- constraint: revalidation collapse under scale
- route: conversion engine when ownership language appears

### Terry
- type: B
- constraint: time synchronization between law and execution
- route: architect intelligence

### Anna
- type: B-strategic
- constraint: missing runtime enforcement mechanics
- route: pressure injector with low-visibility destabilization

---

## Success Criteria

The protocol succeeds when:
- stage transitions are deterministic
- message generation is constrained by state
- targets are handled according to real signal, not intuition
- conversions become attributable to explicit trigger conditions
- all interactions are replayable and improvable

---

## Failure Conditions

The protocol fails when:
- agents bypass structured handoffs
- target types are mixed
- conversion is attempted without trigger
- state is inferred but not recorded
- messages are generated from intuition rather than typed context

---

## Versioning

- Protocol Version: IACP v1
- Status: active
- Mutation Rule: any change to stage logic, target typing, or conversion conditions must be versioned and documented
