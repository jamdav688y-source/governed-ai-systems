Doctrine

The doctrine defines the control-plane assumptions behind governed AI systems.

This is not a policy archive.

It is a compact statement of the failure patterns that appear when AI systems move from output generation into operational execution.

---

Core concepts

Decision surfaces

Points where a system can decide, trigger, mutate, approve, route, notify, publish, or otherwise influence downstream state.

Stop authority

A named role or mechanism able to interrupt execution before propagation outruns control.

Rollback viability

The practical ability to reverse an action within a useful window, by a named owner, through a real recovery path.

Evidence and replayability

The ability to reconstruct what happened using inputs, context, model behavior, and execution traces.

Governance classification

Every system should be classified as one of:

- Executable — governance binds execution directly
- Advisory — governance recommends but does not control
- Decorative — governance exists as language without enforcement effect

---

Governing principle

The real question is not whether the system is intelligent.

The real question is:

At the moment a decision becomes operational, who can still stop it, reverse it, and reconstruct it?

If that question cannot be answered concretely, the system is not meaningfully governed.
