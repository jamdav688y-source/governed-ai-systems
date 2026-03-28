# Conversion Trigger Runbook

## Purpose

This runbook defines exactly when the system is permitted to move from diagnostic probing into a bounded offer.

The goal is precision, not eagerness.

---

## Hard Requirement

Conversion is allowed only when all three signals are present:

1. Ownership Signal
2. Uncertainty Tied to System
3. Boundary Exposure

If one is missing, conversion is blocked.

---

## Ownership Signal

The target refers to:
- their system
- their team
- their environment
- their workflow
- their implementation
- their actual deployment conditions

### Valid examples
- "We're seeing this under load."
- "In our setup..."
- "We tried X and it still fails."
- "We don't have a clean way to stop that."

---

## Uncertainty Tied to System

The target signals:
- unresolved implementation
- incomplete confidence
- uncertain enforcement
- scaling doubt
- inability to hold the boundary in practice

### Valid examples
- "Not sure how to enforce that."
- "It changes under scale."
- "We still haven't solved that cleanly."

---

## Boundary Exposure

The target reveals a real failure seam:
- authority drift
- enforcement gap
- halt/execution mismatch
- context reuse invalidation
- temporal misalignment
- inability to bind authority

### Valid examples
- "We evaluate it, but execution still slips through."
- "Caching reintroduces authority assumptions."
- "The law layer lags execution."

---

## Canonical Conversion Frame

That failure mode is exactly where most systems lose control without realizing it.

What we usually do there is map a single execution path and force three things into alignment:

- where authority is assumed vs actually proven
- where it’s evaluated vs where it’s bound
- where execution outruns the system’s ability to interrupt it

It’s a short diagnostic, but it makes the gap very concrete—usually in one or two transitions.

Happy to walk through it if useful.

---

## Abort Conditions

Abort conversion if:
- the target becomes abstract again
- ownership disappears
- the signal collapses into generic agreement
- the thread shifts into theory only
- pressure begins to exceed tolerance

If aborted:
- downgrade to HOLD
- reroute to Dialogue Executor
- or archive the thread

---

## Logging

Every conversion attempt must record:
- target name
- stage before conversion
- ownership signal evidence
- uncertainty evidence
- boundary evidence
- message used
- result
- stage after