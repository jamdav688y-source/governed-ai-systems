# Stage Machine v1

## Purpose

This protocol defines the allowed interaction stages and valid transitions.

## Stages

### ENTRY
Target detected. No engagement yet.

Allowed next stages:
- PROBE
- EXIT

### PROBE
Initial message sent to expose structure, pressure, or boundary awareness.

Allowed next stages:
- CLASSIFY
- EXIT

### CLASSIFY
Target is assigned a type and response strategy.

Allowed next stages:
- ESCALATE
- EXIT

### ESCALATE
Pressure is increased through precision, not intensity.

Allowed next stages:
- CONVERT
- PROBE
- EXIT

### CONVERT
Bounded offer or diagnostic invitation.

Allowed next stages:
- EXIT
- ESCALATE

### EXIT
Thread is closed, paused, filtered, or archived.

Allowed next stages:
- none

## Transition Rules

No stage advance is valid unless:
1. state is recorded
2. required signals are present
3. next action is assigned
4. protocol conditions are satisfied

## Block Rules

- no conversion without trigger
- no escalation without classification
- no probe without entry
- no re-entry without explicit archival reopen
