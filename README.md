Governed AI Systems

Control-plane architecture for AI systems that must remain stoppable, reversible, and accountable under execution pressure.

Most AI repositories explain components.

This repository focuses on something else:

who holds authority when an AI system is already running, how continuation becomes admissible, how interruption happens in time, and whether rollback is real or assumed.

---

What this repository is for

Governed AI Systems is a practical framework for designing and auditing AI workflows, agents, and automated decision systems that can:

- classify
- route
- approve
- notify
- publish
- trigger actions
- mutate downstream state

The core concern is not model quality alone.

It is whether a system can continue operating without enforceable authority, timely interruption, rollback viability, or replay-grade evidence.

---

Core thesis

A system is not governed because it has policies, dashboards, or monitoring.

A system is governed when control remains enforceable at the moment decisions become operational.

That requires:

- explicit decision ownership
- named stop authority
- bounded rollback
- evidence sufficient for reconstruction
- admissibility checks at the execution boundary

Without those, governance becomes advisory at best and decorative at worst.

---

Repository contents

"doctrine/"

First principles for governed AI systems:

- decision surfaces
- stop authority
- rollback viability
- evidence and replayability
- governance classification

"doctrine/diagnostics/"

Deployment gates and audit checklists for real systems.

"docs/offers/"

Client-facing commercial packaging for the AI Failure Boundary Audit.

"docs/deliverables/"

Sample delivery artifacts showing what an audit produces.

".github/workflows/"

Governance-oriented CI checks that block merges when required governance artifacts are missing or incomplete.

"scripts/"

Lightweight validation tools used by CI.

---

Getting started

1. Read the doctrine in "doctrine/README.md"
2. Review the governance gate in "doctrine/diagnostics/00-governance-gate.md"
3. Inspect the client offer in "docs/offers/ai-failure-boundary-audit.md"
4. Review the sample deliverable in "docs/deliverables/sample-client-deliverable.md"
5. Enable the GitHub Actions workflow in ".github/workflows/governance-ci.yml"

---

Who this is for

This repository is designed for:

- CTOs
- technical founders
- platform and infrastructure leads
- AI product and operations leads
- teams deploying agentic workflows into live systems

---

Commercial use

This repository also supports a fixed-scope service:

AI Failure Boundary Audit

A diagnostic engagement for identifying where AI systems can continue executing without clear authority, enforceable stop conditions, rollback viability, or replay-grade evidence.

---

License

MIT
