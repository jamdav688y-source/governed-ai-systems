Governance Gate

Use this gate before deploying any AI workflow, agent, or automated decision system that can affect live state.

---

1. System Name

Name the system or workflow.

---

2. Purpose and Scope

What is the system allowed to do?

What external effects can it trigger?

Keep the boundary tight. One workflow family only.

---

3. Decision Owner

Who owns the consequences of this system’s decisions?

Name the person or role.

---

4. Stop Authority

Who can halt the system?

How is the halt triggered?

Can interruption happen at or below execution speed?

---

5. Rollback Viability

How are incorrect actions reversed?

Who performs the rollback?

What is the rollback window?

Has the rollback path been tested?

---

6. Evidence Path

What evidence is captured?

At minimum, identify:

- input state
- model output
- decision context
- execution trace
- downstream mutation record

Can the decision be reconstructed later?

---

7. Governance Classification

Choose one:

- Executable
- Advisory
- Decorative

Explain why.

---

8. Approval Checklist

- [ ] Decision owner identified
- [ ] Stop authority identified
- [ ] Rollback path defined
- [ ] Evidence path defined
- [ ] Governance classification assigned
- [ ] Gate reviewed before deployment

---

9. Signature

Decision Owner: ____________________

Stop Authority: ____________________

Date: ____________________
