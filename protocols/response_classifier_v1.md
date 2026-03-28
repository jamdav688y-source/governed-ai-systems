# Response Classifier v1

## Purpose

This protocol defines how inbound responses are classified so the system can decide whether to push, hold, align, convert, filter, or exit.

## Core Axes

Each response is evaluated across three axes:

1. Signal Depth
2. Constraint Awareness
3. Ownership Pressure

## Axis Definitions

### Signal Depth
How structurally sophisticated the response is.

- Low: generic, reactive, surface-level
- Medium: partially structured, some system awareness
- High: explicit architecture, constraints, failure surfaces, runtime implications

### Constraint Awareness
Whether the target recognizes a real limit, failure boundary, or enforcement gap.

- Low: no real boundary recognition
- Medium: sees tension but not precisely
- High: names structural breakdown or scalability failure clearly

### Ownership Pressure
Whether the target is exposed to the consequences.

- Low: observer, commentator, theorist
- Medium: adjacent to implementation
- High: accountable for system behavior, deployment, or failure

## Response Types

### Type A
High signal depth, high constraint awareness, high ownership pressure.

Route:
- conversion eligible

### Type B
High signal depth, medium/high awareness, low ownership pressure.

Route:
- alignment or strategic destabilization

### Type C
Medium signal, high felt tension, incomplete structure.

Route:
- shaping

### Type D
Low/medium signal, curiosity without pressure.

Route:
- filter or minimal engagement

### Type E
Noise.

Route:
- drop

## Detection Rules

### Ownership Signal
Present when the target references:
- our system
- our team
- our environment
- our pipeline
- our use case
- our implementation

### Uncertainty Signal
Present when the target expresses:
- unresolved implementation
- incomplete confidence
- enforcement ambiguity
- scaling uncertainty

### Boundary Exposure
Present when the target reveals:
- authority drift
- enforcement gap
- execution/halt mismatch
- context reuse failure
- temporal misalignment
- inability to bind authority

## Action Rules

### If Type A
Action:
- push toward localized diagnostic
- convert when ownership + uncertainty + boundary are all present

### If Type B
Action:
- inject one missing invariant
- do not sell unless ownership emerges

### If Type C
Action:
- structure the problem
- name one failure condition
- do not convert early

### If Type D
Action:
- minimal response or none

### If Type E
Action:
- drop

## Output Labels

Each classified response must output:
- target type
- confidence
- next best action
- response mode
- core constraint
- authority gap
