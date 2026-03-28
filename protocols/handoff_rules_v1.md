# Handoff Rules v1

## Purpose

This protocol defines how agents hand off control between one another.

## Rule

No agent may hand off raw intuition.
Every handoff must include:
- current stage
- target type
- signal state
- authority gap
- next action recommendation

## Handoffs

### Signal Hunter -> Constraint Mapper
Condition:
- target signal is above intake threshold

### Constraint Mapper -> Classifier Engine
Condition:
- at least one structural constraint is detected

### Classifier Engine -> Dialogue Executor
Condition:
- classification confidence meets threshold

### Dialogue Executor -> Pressure Injector
Condition:
- response contains partial certainty, defense, or unresolved acknowledgement

### Pressure Injector -> Conversion Engine
Condition:
- ownership signal present
- uncertainty signal present
- boundary exposure present

### Conversion Engine -> Exit
Condition:
- offer accepted, rejected, or archived