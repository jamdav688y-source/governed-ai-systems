# The Control Plane

> Intelligence is not the risk.  
> Execution without control is.

This document defines the **Control Plane** — the layer of the system responsible for making AI and automation *governable*, not merely capable.

The control plane does not generate outputs.  
It governs **whether, why, and how** outputs are allowed to affect the real world.

---

## 1. The Core Problem

Most production AI failures are not model failures.

They are failures of:

- Decision traceability
- Ownership
- Reversibility
- Stop authority
- Institutional memory

In other words: **the system can act, but no one can prove, stop, or undo what it did.**

That is not an intelligence problem.  
That is a control problem.

---

## 2. What Is the Control Plane?

The Control Plane is the layer that sits **above**:

- Models
- Prompts
- Agents
- Tools
- Workflows
- Orchestrators

Its job is not to make the system smarter.

Its job is to make the system:

- Inspectable
- Constrainable
- Auditable
- Reversible
- Governable

---

## 3. The Four Invariants

A system is not governable unless all four are true:

1. **It can be stopped**  
   There exists a human or institutional stop authority that can halt execution.

2. **It can be explained**  
   The system can reconstruct why a decision was made, using preserved artifacts.

3. **It can be undone**  
   The system supports rollback to a known-good state or compensating actions.

4. **It remembers**  
   Decisions, changes, incidents, and overrides are stored as first-class artifacts.

If any of these are missing, you do not have a system.  
You have an **ungoverned actor**.

---

## 4. What the Control Plane Owns

The control plane owns:

- Decision records
- Approval chains
- Execution permissions
- Risk classification
- Rollback semantics
- Incident lineage
- Audit trails
- Policy enforcement
- Change history

It does **not** care whether the underlying engine is:

- GPT
- Claude
- Gemini
- A rules engine
- A human
- Or a swarm of agents

All actors are treated as **untrusted executors**.

---

## 5. Control vs Orchestration

Orchestration asks:

> How do we get the work done?

Control asks:

> Should this be done?  
> Who approved it?  
> What happens if it’s wrong?  
> How do we undo it?  
> How do we prove what happened?

Most systems have orchestration.

Almost none have control.

---

## 6. Control Plane as Institutional Memory

The control plane is the **memory of the organization** as expressed through:

- Decisions
- Incidents
- Exceptions
- Overrides
- Policy changes

If it is not written down, versioned, and reviewable, it **does not exist**.

---

## 7. Design Principle

> No action without a decision record.  
> No decision without an owner.  
> No change without a rollback path.  
> No execution without stop authority.

---

## 8. What Comes Next

This repository will define:

- A Decision Artifact schema
- An Incident Artifact schema
- A Policy / Gate system
- A Review and Approval flow
- A Rollback and Reversal model
- A Governance CI layer

These are not documents.

They are **executable constraints**.

---

## 9. The Point

We are not trying to build smarter systems.

We are trying to build systems that **survive contact with reality**.
