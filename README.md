# Governed AI Systems  
**Control-Plane Architecture for Enforceable AI Execution**

---

## Opening Claim

Most AI systems don’t fail because they make the wrong decision.

They fail because they **continue executing after they’ve lost the authority to act**.

At scale, failure is not a model problem.

It is a **control-plane problem**.

> If interruption is not co-temporal with execution, governance collapses into observation.

---

## System Model (Planes)

AI systems are typically described across three planes:

| Plane | Function | Limitation |
|------|---------|-----------|
| Data Plane | Execution, transport | No decision control |
| Management Plane | Monitoring, configuration | Out-of-band authority |
| AI / Decision Plane | Inference, optimization | No enforcement |

---

### What’s Missing: The Control Plane

| Capability | Function |
|-----------|--------|
| Admissibility | Validate decisions before execution |
| Enforcement | Apply constraints at runtime |
| Interruption | Stop execution under load |
| Rollback | Restore system state |
| Attestation | Reconstruct decisions |

---

**Key distinction:**

- Monitoring = visibility  
- Control = authority  

Most systems have the first.  
Very few have the second.

---

## Minimum Survivable Governance Kernel (MSGK)

Every decision must satisfy four conditions:

### 1. Downside Custody  
Who owns failure when it occurs?

### 2. In-Band Stop Authority  
Can execution be halted during runtime?

### 3. Rollback Viability  
Can the system return to a valid state?

### 4. Replay-Grade Evidence  
Can the decision be reconstructed exactly?

---

If any of these are missing:

> The system is operating outside governance.

---

## Decision Lifecycle

```text
Design → Admissibility → Execution → Propagation → Intervention → Rollback
