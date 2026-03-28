# Governed AI Systems
Control-Plane Architecture for Enforceable AI Decisions

---

## Governing Doctrine

Most systems describe how decisions are made.

Production systems reveal where decisions can be stopped.

> Governance exists only at the boundary where decisions become irreversible.

If execution outruns interruption, control is decorative.

---

## System Objective

Convert AI interaction systems from:

- non-deterministic
- non-replayable
- non-auditable

into systems that are:

- stateful
- constrained
- replayable
- enforceable at runtime

---

## Minimum Survivable Governance Kernel (MSGK)

No irreversible action proceeds unless:

1. Downside ownership is assigned  
2. Stop authority is enforceable in-loop  
3. Rollback conditions are defined  

Failure of any condition blocks execution.

---

## System Layers (Authoritative)

Each layer has a single responsibility. No overlap.

### 1. Doctrine
**Location:** `README.md`

Defines:
- irreversibility boundary
- control-plane assumptions
- enforcement philosophy

---

### 2. Protocols
**Location:** `protocols/`

Defines allowed behavior:

- interaction stages: entry → probe → classify → escalate → convert → exit  
- agent roles and transitions  

> Protocols define what *may happen*

---

### 3. Schemas
**Location:** `schemas/`

Defines machine-valid structure:

- `agent_message.schema.json` → Atomic Message Object (AMO)  
- `classification.schema.json` → target typing + routing  
- `target_state.schema.json` → persistent state  

Invariant:

> No interaction exists outside a valid schema.

---

### 4. Contracts
**Location:** `contracts/`

Defines enforcement:

- `interaction_rules.yaml` → stage gating, transition rules  
- `scoring_policy.yaml` → weighting, thresholds, ranking  

Critical rule:

> Scoring suggests. Contracts decide.

No action executes without contract satisfaction.

---

### 5. Workflows
**Location:** `workflows/n8n/`

Implements runtime behavior:

- `intake.json` → normalize input → create AMO + target state  
- `classifier.json` → score + classify + route  
- `conversion_trigger.json` → enforce conversion admissibility  

> Workflows execute only what contracts allow.

---

## Execution Flow