# Governed AI Systems

## Core Invariant

No move without rollback.

## What This Repo Enforces

Every system, idea, or node must define:

1. State space (what states exist)
2. Owner (who controls it)
3. Transition rules (how it changes)
4. Rollback path (how it reverses)
5. Drift detection (how failure is detected)

If these are not defined, the system does not execute.

This repository encodes decision control before expansion.