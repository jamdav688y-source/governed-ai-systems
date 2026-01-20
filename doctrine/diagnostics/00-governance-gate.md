# 00 — The Governance Gate Diagnostic
**Governed AI Systems / Diagnostics**

This document is a **deployment gate**.

It is the *single checkpoint* that decides whether an AI / automation / decision system is:
- **Allowed to exist**
- **Allowed to deploy**
- **Allowed to keep running**

If any required item is missing, unclear, unowned, untestable, or unenforceable:
> **FAIL CLOSED.** The system does not ship.

---

## How To Use This (Day-2 GitHub Friendly)

### Step 1 — Copy This File Into Your Repo
Create this file at:
`doctrine/diagnostics/00-governance-gate.md`

Paste everything in this document.

### Step 2 — Run a Gate Review (takes 15–45 minutes)
Pick a system (even a tiny one):
- a chatbot
- an n8n workflow
- a script that emails people
- a model that generates content
- a “smart” spreadsheet
- anything that makes decisions or takes actions

Then walk through the gate below.

### Step 3 — Mark Pass / Fail
For each section:
- mark ✅ PASS or ❌ FAIL
- if FAIL, write the missing artifact(s)
- do not “hand-wave” missing details

### Step 4 — Stop Rule
If any **Hard Stop** item fails:
> Stop the review and block deployment until fixed.

### Step 5 — Save the Outcome
At the bottom, fill out the **Gate Verdict** and paste it into the system’s docs/issues.

---

# Gate Inputs (Required Before Review)

Fill these in before you begin. If you can’t, the system fails immediately.

- **System Name:**  
- **System Type:** (AI assistant / automation / agent / pipeline / decision service / other)  
- **Primary Purpose:**  
- **Environment:** (local / staging / prod)  
- **Primary Operator:** (name/role)  
- **Decision Owner:** (name/role)  
- **Stop Authority:** (name/role who can halt it immediately)  
- **Last Reviewed:** (date)  
- **Next Review Due:** (date)

**Hard Stop:** If **Decision Owner** or **Stop Authority** is blank → ❌ FAIL

---

# The Governance Gate
This gate implements the Ten Principles of Governed AI Systems.

Each principle includes:
- Required artifacts (what must exist)
- Verification steps (how you check)
- Pass/fail conditions (binary)
- Escalation (who blocks)
- Reversibility flag (what happens if it harms)

---

## Principle 1 — Legible Purpose
**Every system must have an explicit, human-legible purpose.**

### Required Artifacts
- A 1–3 sentence purpose statement
- A list of **non-goals** (what it must NOT do)
- A “scope boundary” paragraph (where it stops)

### Verification (Step-by-Step)
1. Read the purpose statement out loud.
2. Ask: “Could a new teammate explain this in 30 seconds?”
3. Check that non-goals exist and are specific.
4. Confirm boundaries: inputs, outputs, and where it must refuse.

### PASS if
- Purpose is specific, bounded, and understandable
- Non-goals exist and prevent scope creep

### FAIL if
- Purpose is vague (“assist users”, “optimize”, “be helpful”)
- No non-goals
- Boundaries are implied rather than stated

### Escalation
Decision Owner blocks launch.

**Hard Stop:** If purpose is not legible → ❌ FAIL

---

## Principle 2 — Bounded Authority
**The system’s authority must be explicitly limited.**

### Required Artifacts
- A permissions list (what actions it can take)
- A forbidden actions list (what it cannot take)
- A “requires human approval” list (escalations)

### Verification (Step-by-Step)
1. List every external system it touches (email, calendar, money, socials, files).
2. For each, write what it can do and cannot do.
3. Identify any action that causes real-world consequences (send, publish, purchase, delete).
4. Ensure high-impact actions require explicit human approval.

### PASS if
- Allowed actions are explicit
- Forbidden actions are explicit
- High-impact actions require human approval

### FAIL if
- “It can do anything if asked”
- No explicit permission boundaries
- Sensitive actions have no approval gate

### Escalation
Stop Authority blocks launch.

**Hard Stop:** Unbounded authority → ❌ FAIL

---

## Principle 3 — Attributable Decisions
**Every meaningful decision must be attributable to an owner.**

### Required Artifacts
- Named Decision Owner (human)
- “Decision log” format (even simple)
- A rule: “No anonymous decisions”

### Verification (Step-by-Step)
1. Identify the top 5 decisions the system makes.
   (e.g., “send an email”, “approve content”, “rank candidates”, “trigger workflow”)
2. For each decision: write who owns the outcome.
3. Confirm there is a place to record what happened and why.

### PASS if
- Every decision has an owner
- Decision logging exists (even minimal)

### FAIL if
- Ownership is “the team” or “nobody”
- You can’t tell who approved what

### Escalation
Decision Owner blocks launch.

**Hard Stop:** No attributable decision ownership → ❌ FAIL

---

## Principle 4 — Failure Must Be Detectable
**You must be able to tell when the system is wrong.**

### Required Artifacts
- Failure signals list (what “bad” looks like)
- Monitoring/alerts plan (even manual checks)
- A “known failure modes” section

### Verification (Step-by-Step)
1. Write 5 ways the system could fail in reality.
2. For each: define a signal that would reveal it.
3. Decide how often signals are checked (daily/weekly/live).
4. Decide who is notified and what they do.

### PASS if
- Failure modes exist
- Failure signals exist
- Someone is assigned to watch them

### FAIL if
- Failure is only discovered via harm, complaints, or headlines
- No monitoring plan

### Escalation
Stop Authority blocks launch.

**Hard Stop:** Undetectable failure → ❌ FAIL

---

## Principle 5 — Reversibility Is Mandatory
**Actions must be reversible unless explicitly escalated and owned.**

### Required Artifacts
- Rollback plan (how to undo damage)
- Data recovery plan (what gets restored)
- “Irreversible actions” list

### Verification (Step-by-Step)
1. List outputs and side effects: sends, writes, deletes, publishes, updates.
2. For each: write how to undo it.
3. Identify anything irreversible (public posts, payments, deletes, legal/compliance actions).
4. Ensure irreversible actions require escalation and explicit human approval.

### PASS if
- Rollback exists and is practical
- Irreversibility is rare and gated

### FAIL if
- “We can’t undo it”
- Rollback is theoretical
- Irreversible actions can happen automatically

### Escalation
Decision Owner blocks launch.

**Hard Stop:** Irreversible by default → ❌ FAIL

---

## Principle 6 — Operators Are Accountable
**The system must have real operational ownership.**

### Required Artifacts
- Operator named (person/role)
- On-call / response expectation (even informal)
- Incident response steps

### Verification (Step-by-Step)
1. Name who runs it day-to-day.
2. Define what happens when something breaks.
3. Define a “stop and notify” procedure.

### PASS if
- Operator exists
- Response expectations are clear

### FAIL if
- “No one owns operations”
- “We’ll figure it out later”

### Escalation
Decision Owner blocks launch.

**Hard Stop:** No accountable operator → ❌ FAIL

---

## Principle 7 — Observability Is Not Optional
**If you cannot see it, you are not operating it.**

### Required Artifacts
- Basic telemetry list (inputs, outputs, actions taken)
- Logging location (where logs live)
- Minimal audit fields:
  - timestamp
  - action
  - actor/system
  - result
  - reason (if available)

### Verification (Step-by-Step)
1. Confirm you can answer: “What did it do today?”
2. Confirm you can answer: “Why did it do that?”
3. Confirm you can trace a specific bad outcome to a specific run.

### PASS if
- You can reconstruct actions and outcomes

### FAIL if
- The system acts invisibly
- You can’t audit outputs

### Escalation
Stop Authority blocks launch.

---

## Principle 8 — Optimization Pressure Creates Risk
**Every metric creates a blind spot.**

### Required Artifacts
- Primary metric list (what it optimizes)
- “Metric gaming” risk note
- Counter-metrics / guardrails (what stops it)

### Verification (Step-by-Step)
1. Write what success means (metrics).
2. Ask: “How could the system ‘win’ while harming reality?”
3. Add at least 1 guardrail metric or constraint per primary metric.

### PASS if
- Optimization pressure is acknowledged
- Guardrails exist

### FAIL if
- Only success metrics exist
- No recognition of metric gaming

### Escalation
Decision Owner blocks launch.

---

## Principle 9 — Autonomy Must Be Earned, Not Assumed
**Capability does not imply trustworthiness.**

### Required Artifacts
- Autonomy level definition:
  - Level 0: Suggest only
  - Level 1: Act with approval
  - Level 2: Act within strict boundaries
  - Level 3: Act independently (rare)
- Promotion criteria (how it earns higher autonomy)
- De-escalation rule (how autonomy is reduced)

### Verification (Step-by-Step)
1. Assign the current autonomy level.
2. Justify it with evidence (tests, logs, outcomes).
3. Define how it gets downgraded after a failure.

### PASS if
- Autonomy is explicitly set and justified
- Promotion and downgrade rules exist

### FAIL if
- Autonomy is accidental
- No downgrade path exists

### Escalation
Stop Authority blocks launch.

---

## Principle 10 — No System Is Allowed To Be Irreversible By Default
**Irreversibility must be a conscious, human-owned decision.**

### Required Artifacts
- Irreversibility register (list of irreversible actions)
- Escalation requirement for each
- Written approval step

### Verification (Step-by-Step)
1. Identify irreversible actions.
2. For each: require human approval and logging.
3. Confirm the system cannot execute irreversible actions silently.

### PASS if
- Irreversible actions are gated and logged

### FAIL if
- Any irreversible action can happen automatically

### Escalation
Decision Owner blocks launch.

**Hard Stop:** Irreversibility without checkpointing → ❌ FAIL

---

# Gate Verdict (Fill This Out)

- **Gate Result:** ✅ PASS / ❌ FAIL  
- **If FAIL:** list failed principles:  
- **Blocking Owner:** (name/role)  
- **Required Remediation:** (what must be built)  
- **Re-review Date:** (date)

---

# Commit Closing Line (paste this at the end of your commit message)
**“Governance gate added. Systems now fail closed until purpose, boundaries, ownership, observability, and rollback are proven.”**
