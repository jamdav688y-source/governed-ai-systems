# Unified Artifact Diagnostic Engine v1
Executable Analysis Protocol for Post + Diagram + Runtime Interpretation

## Purpose

This protocol defines how to analyze a post and diagram as **one executable system artifact**, not as separate media.

The text is treated as the system’s **declared logic**.  
The diagram is treated as the system’s **implied runtime model**.

The objective is not summarization.

The objective is to determine:

- what the system claims to do
- what it is actually optimizing for
- where consequence becomes real
- whether governance is executable or decorative
- who can interrupt failure before durability
- whether rollback is real, partial, or fictional
- whether observability is being mistaken for control

This protocol exists to produce analysis that is:
- architecturally precise
- operationally credible
- diagnostically useful
- trust-generating under real production scrutiny

---

## Core Doctrine

Most diagrams explain components.

Production systems reveal control surfaces.

Look for where decisions become irreversible.

That boundary is where governance must exist.

---

## Governing Principle

No artifact analysis is complete unless it answers all of the following:

1. Where does this system decide?
2. Where does this system mutate state?
3. Where can this system be interrupted?
4. What can still be reversed after commit?
5. What evidence will prove why the decision was allowed?

If the analysis cannot answer these, it is descriptive, not diagnostic.

---

## Operating Assumptions

This protocol assumes:

- real systems fail at boundaries, not in marketing language
- architectural diagrams usually omit authority topology
- text often overstates governance while diagrams reveal execution bias
- control must be evaluated at commit, not after propagation
- the most important distinction is not between “good” and “bad” systems, but between:
  - monitored systems
  - governed systems

---

## Required Analysis Output

Every execution of this protocol must produce the following sections.

### 1. Thesis
State:
- what the artifact says it does
- what it is actually optimizing for
- what control model it implies

Output must distinguish:
- declared thesis
- operational thesis
- governance thesis

---

### 2. Actors
Enumerate:
- human actors
- system actors
- external systems
- hidden operators
- implied authority holders
- implied stop authorities

For each actor define:
- role
- authority scope
- dependency
- whether they are advisory, executory, interruptive, or audit-bearing

---

### 3. Components
Extract:
- inputs
- transforms
- state stores
- decision nodes
- execution surfaces
- outputs
- feedback loops
- memory layers
- synchronization layers
- evidence layers

Distinguish:
- explicit components
- implied components
- missing components required for control

---

### 4. Runtime Architecture

#### Data Plane
Trace:
- data ingress
- transformation
- storage
- replication
- retrieval
- egress

Identify:
- provenance loss risk
- stale state risk
- compression-induced ambiguity
- delayed synchronization

#### Control Plane
Identify:
- admissibility gates
- policy resolution points
- enforcement seams
- interrupt mechanisms
- rollback prerequisites
- escalation paths

Ask:
- is control pre-execution, in-execution, or post hoc?
- is control enforceable or observational?
- is the control plane in-band with execution or outside it?

#### Decision Plane
Identify:
- where the system determines next action
- which evidence is used
- whether law/state/support conditions are live or inherited
- whether the decision is re-derived or assumed

Ask:
- who is allowed to decide?
- under what basis?
- can a prior valid decision become invalid at commit?
- can that invalidation interrupt in time?

#### Execution Plane
Identify:
- where side effects occur
- what becomes durable
- how propagation happens
- when reversibility degrades
- which downstream systems are affected

Ask:
- where does consequence become real?
- what is the exact commit boundary?
- does halt latency beat execution latency?

---

### 5. Hidden Layers
Infer:
- unstated trust assumptions
- hidden approval models
- operator fallback paths
- synchronization dependencies
- caching or inheritance shortcuts
- dead-snapshot risks
- implicit revocation models
- externalized law or support conditions

Distinguish:
- explicit truth
- implied truth
- missing truth

---

### 6. State Mutation Map
For each mutation point record:
- trigger
- actor
- target state
- reversibility class
- evidence produced
- propagation risk
- recovery path

Reversibility classes:
- fully reversible
- partially reversible
- patch-forward only
- irreversible

No mutation map is complete unless it states:
- whether rollback is real
- who owns rollback
- how long rollback remains viable

---

### 7. Governance Gates
Identify all of the following where present:
- approval gates
- admissibility gates
- exception gates
- escalation gates
- interrupt gates
- rollback gates
- revalidation gates
- continuation-validity gates

For each gate specify:
- when it occurs
- who owns it
- whether it is binding
- whether it can be bypassed
- whether it executes before durability

Classify each gate:
- decorative
- advisory
- partial
- executable

---

### 8. Authority Topology
Map:
- decision authority
- stop authority
- rollback authority
- override authority
- audit authority
- revocation authority

For each authority define:
- scope
- timing
- binding power
- escalation dependency
- whether it is in-band with commit

Key diagnostic question:
Can the authority to invalidate a continuation interrupt propagation before consequence becomes durable?

If not, authority is present in form and absent in operation.

---

### 9. Propagation Paths
Trace:
- direct propagation
- downstream fan-out
- cross-system side effects
- delayed durability
- consistency windows
- stale-state inheritance
- retry/replay amplification

State:
- what error travels
- how far it travels
- how quickly it becomes harder to reverse
- whether containment is pre- or post-commit

---

### 10. Failure Surfaces
At minimum evaluate:

#### Injection
Can invalid input, malformed intent, or stale assumptions enter the system and become executable?

#### Drift
Can the system become structurally different from what it claims while still looking coherent?

#### Privilege Escalation
Can any actor or process execute beyond lawful scope?

#### Rollback Failure
Can the system reverse state meaningfully, or only cosmetically?

#### Timing Mismatch
Can control or revocation arrive after execution has already hardened state?

#### Stale Authority
Can the system continue under an authority basis that is formally valid but substantively expired?

#### Invalid Continuation
Can a continuation remain executable after law/state/support conditions have changed?

Each failure surface must include:
- technical explanation
- operational implication
- likely production symptom

---

### 11. Infrastructure Alignment
Classify the artifact against known patterns:

- orchestration stack
- observability-heavy system
- policy layer
- supervisory control system
- agent loop
- distributed commit system
- workflow engine
- event-driven control fabric
- monitoring façade
- governance substrate

Then state:
- what it resembles in practice
- what it claims in language
- where the mismatch lives

---

### 12. Architectural Verdict
Every analysis must end with one of four verdicts:

- decorative governance
- advisory governance
- partial enforcement
- executable governance

The verdict must be justified using:
- authority topology
- commit boundary control
- halt latency vs execution latency
- rollback realism
- evidence replayability
- ability to invalidate before durability

---

## Compression Rule

Every paragraph must do three things at once:

1. explain the architecture
2. expose the failure boundary
3. imply deployable judgment under real operating conditions

If a paragraph does only one of these, it is incomplete.

---

## Trust-Grade Writing Rule

Analysis must signal:
- production grounding
- practical exposure
- calm authority
- deployable judgment

Use lines like:
- "In production, this usually breaks where..."
- "The pattern that shows up under load is..."
- "This often looks disciplined on paper, but fails when..."
- "Easy to miss until the system has to decide under time pressure."

Avoid:
- pure abstraction
- moralizing
- feature praise
- generic criticism
- vague "best practice" phrasing

---

## Production-Grounded Diagnostic Moves

### Move 1 — Name the boundary
Always identify the exact point where consequence becomes real.

### Move 2 — Name the owner
Always identify who owns downside once failure crosses commit.

### Move 3 — Name the interrupt
Always state whether any authority can stop the path in-loop.

### Move 4 — Name rollback realism
Always classify rollback as real, partial, or fictional.

### Move 5 — Name the evidence
Always say what artifact would prove why the decision was allowed.

---

## Non-Negotiable Questions

Every analysis must answer these explicitly:

- What is the decision boundary?
- What is the commit boundary?
- What authority may invalidate?
- Under what active basis?
- Can invalidation preempt durability?
- What state remains reversible at failure time?
- What log, trace, or artifact proves why the system allowed it?

---

## Final Output Template

Use this structure exactly:

### Thesis
### Actors
### Components
### Runtime Architecture
#### Data Plane
#### Control Plane
#### Decision Plane
#### Execution Plane
### Hidden Layers
### State Mutation Map
### Governance Gates
### Authority Topology
### Propagation Paths
### Failure Surfaces
### Infrastructure Alignment
### Architectural Verdict

Close with:

**If this system fails at 9:17 AM, who can stop it at 9:18, what state can still be reversed, and what evidence will prove why it happened?**

---

## Example Compression Lines

- This architecture is optimized for throughput and coherence, but it leaves authority ambiguity unresolved at the exact point consequence becomes durable.
- The system can explain itself after execution, but cannot interrupt itself before propagation, which makes the control model observational rather than operative.
- Rollback exists in interface terms, but not in state terms, so recovery is partial at best and mostly narrative under load.
- The diagram suggests synchronization, but the hidden failure is that continuity remains executable even after its lawful basis has degraded.
- This is a well-composed execution model with weak governance binding: strong movement, weak admissibility.

---

## Operator Use Cases

Use this protocol when analyzing:
- architecture diagrams
- workflow diagrams
- system posts
- vendor diagrams
- AI product posts
- security and observability architectures
- HITL models
- orchestration stacks
- MCP / function calling / CLI control patterns
- governance and compliance posts that lack runtime enforcement detail

---

## Final Principle

A system is not governed because it has controls.

A system is governed only when those controls can interrupt consequence before durability.