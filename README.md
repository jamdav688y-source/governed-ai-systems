## Example: Enforced Conversion Decision (Faustina)

This example demonstrates how the system enforces a conversion boundary.

### Input (Observed Interaction)

Target expresses:
- ownership of a real system  
- partial uncertainty in safeguards  
- exposure of a boundary condition  

---

### Intake Output (Normalized State)

- AMO created  
- Target state initialized  
- Thread context bound  

---

### Classification Output

- signal_score: 0.91  
- ownership_signal: true  
- uncertainty_signal: true  
- boundary_exposure: true  
- classification: Type A  

---

### Contract Evaluation

contracts/interaction_rules.yaml requires:

- ownership_signal_detected = true  
- uncertainty_signal_detected = true  
- boundary_exposure_detected = true  

All conditions satisfied.

---

### Decision

Conversion: **ALLOWED**

---

### Counterfactual (Failure Case)

If:

- uncertainty_signal_detected = false  

Then:

Conversion: **BLOCKED**

Reason:
Missing trigger condition → contract violation

---

### Invariant Demonstrated

> No conversion score may override missing trigger conditions.

This example shows:

- scoring does not control execution  
- contracts enforce admissibility  
- the system prevents premature conversion  

---

### What This Proves

The system does not:

- react to perceived intent  
- optimize for engagement  

It:

- enforces decision boundaries  
- blocks invalid transitions  
- allows only contract-valid execution