Sample Client Deliverable

AI Failure Boundary Audit

Client

ExampleCo

System

AI-assisted support ticket triage and escalation workflow

---

Executive Findings Memo

We audited ExampleCo’s AI-assisted ticket triage workflow, which classifies inbound support tickets, assigns priority, and escalates a subset to higher-support tiers.

The main issue is not classification quality alone.

The main issue is that execution can continue without a clearly bounded interruption path, without a tested rollback mechanism, and without evidence sufficient to reconstruct why a routing decision occurred.

As currently implemented, governance is advisory rather than executable.

---

Failure Boundary Map

Decision Surface 1

Ticket priority classification

- Owner: Support Operations Lead
- Stop authority: not explicitly assigned
- Rollback: manual reclassification
- Evidence quality: partial

Decision Surface 2

Escalation to Tier 2 support

- Owner: Support Operations Lead
- Stop authority: team lead can intervene manually
- Rollback: manual reassignment
- Evidence quality: moderate

Decision Surface 3

Automatic management alerting on severe tickets

- Owner: Director of Support
- Stop authority: unclear
- Rollback: none defined
- Evidence quality: weak

---

Decision Surface Register

Surface

Ticket priority classification

- Decision owner: Support Operations Lead
- Stop authority: none named
- Rollback owner: support supervisor
- Governance classification: advisory

Surface

Tier 2 escalation

- Decision owner: Support Operations Lead
- Stop authority: support team lead
- Rollback owner: support supervisor
- Governance classification: partially executable

Surface

Management alert trigger

- Decision owner: Director of Support
- Stop authority: not clearly assigned
- Rollback owner: undefined
- Governance classification: decorative

---

Stop / Rollback Matrix

Ticket priority classification

- Stop authority present: No
- Halt latency: N/A
- Rollback viability: Partial

Tier 2 escalation

- Stop authority present: Yes
- Halt latency: Moderate
- Rollback viability: Yes, manual

Management alert trigger

- Stop authority present: No
- Halt latency: N/A
- Rollback viability: No defined path

---

Risk-Ranked Remediation Plan

30 days

Assign explicit stop authority for each decision surface.

60 days

Define and test rollback procedures for misrouted and misclassified tickets.

90 days

Upgrade evidence capture to preserve input state, model output, routing context, and downstream action history for replay.

---

Sample Governance Gate

System Name: Support Ticket Triage Workflow

Purpose and Scope: Classify and route inbound support tickets using AI assistance.

Decision Owner: Support Operations Lead

Stop Authority: Not fully defined. Requires explicit assignment.

Rollback Viability: Manual reassignment exists, but no tested rollback standard.

Evidence Path: Partial logs captured. Replay-grade evidence not yet available.

Governance Classification: Advisory
