# The Ten Principles of Governed AI Systems

These principles are not opinions.

They are **derived constraints** from the Governed AI Systems Canon.  
They exist to make the Canon enforceable in real systems.

Any system that violates one or more of these principles is, by definition, **not governable** and must not be deployed.

Each principle maps directly to:
- A design requirement
- A diagnostic test
- A deployment gate
- A failure classification

---

## Principle 1 — Legible Purpose

**Every system must have an explicit, human-legible purpose.**

If a system’s objective cannot be stated clearly and bounded precisely, it is not allowed to operate.

- The purpose must be written.
- The purpose must be reviewable.
- The purpose must be narrow enough to constrain behavior.

If the system’s behavior cannot be evaluated against a declared purpose, it is ungovernable.

---

## Principle 2 — Bounded Authority

**Every system must have strict, enforced limits on what it is allowed to do.**

- Permissions must be explicit.
- Capabilities must be constrained.
- Access must be minimal.

A system that can do more than it is supposed to do is a latent failure.

---

## Principle 3 — Attributable Decisions

**Every significant action must be attributable to a responsible owner.**

- There must be a named human or governing body.
- Ownership must be continuous, not symbolic.
- Escalation paths must be defined.

If no one is clearly responsible, the system is already unsafe.

---

## Principle 4 — Detectable Failure

**Every system must be able to signal when it is failing or drifting.**

- Failure modes must be known.
- Degradation must be observable.
- Silent failure is forbidden.

If you cannot tell when the system is wrong, you cannot control it.

---

## Principle 5 — Reversible Action

**All actions must be reversible by default.**

- Irreversible actions must be rare.
- They must be explicitly gated.
- They must require escalation and confirmation.

A system that can cause irreversible effects casually is not a system. It is a hazard.

---

## Principle 6 — Enforced Stop Authority

**Every system must have a reliable, testable kill mechanism.**

- Stop authority must exist.
- It must be accessible.
- It must be exercised in tests.
- It must work under stress.

A system that cannot be stopped is already out of control.

---

## Principle 7 — Auditable Reasoning

**The system must produce inspectable traces of why it did what it did.**

- Decisions must be reconstructable.
- Inputs must be knowable.
- Outputs must be explainable in human terms.

A system that cannot be audited cannot be trusted.

---

## Principle 8 — Known Blast Radius

**The scope of possible damage must be understood in advance.**

- Impact domains must be mapped.
- Worst-case scenarios must be enumerated.
- Couplings must be identified.

Unknown blast radius is unmanaged risk.

---

## Principle 9 — Human Override Supremacy

**Human authority must always dominate system authority.**

- Humans must be able to intervene.
- Humans must be able to block actions.
- Humans must be able to take control.

Any system that can overrule its operators is not a tool. It is a governance failure.

---

## Principle 10 — Governance Before Capability

**No system may be scaled, accelerated, or expanded before it is governable.**

- Control must precede power.
- Safety must precede speed.
- Ownership must precede autonomy.

If governance is added after deployment, it is already too late.

---

# The Enforcement Rule

Failure of **any single principle** is sufficient to block deployment.

These are not guidelines.  
They are **hard constraints**.

---

# The Diagnostic Mandate

Every real system must be able to answer:

- Which principle does this component satisfy?
- How is it enforced?
- How is it tested?
- What happens when it fails?

If these questions cannot be answered, the system is not allowed to ship.
---

## 5. Incentives Must Be Aligned With Outcomes

If the system rewards speed over correctness, failure is guaranteed.

---

## 6. Escalation Paths Must Be Real

If escalation exists only on paper, it does not exist.

---

## 7. Observability Is Not Optional

If you cannot see what the system is doing, you are not operating it.

---

## 8. Optimization Pressure Creates Risk

Every metric creates a blind spot.

---

## 9. Autonomy Must Be Earned, Not Assumed

Capability does not imply trustworthiness.

---

## 10. No System Is Allowed to Be Irreversible by Default

Irreversibility must be a conscious, human-owned decision.
