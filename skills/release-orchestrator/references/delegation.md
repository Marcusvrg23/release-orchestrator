# Delegation protocol

Use this reference only when delegation is being considered.

## Decision gate

Delegation must have a concrete expected benefit. Before spawning a worker, state internally or in the assignment:

```text
WHY_DELEGATE
QUESTION
SCOPE
KNOWN_FACTS
PROTECTED_BEHAVIOR
FORBIDDEN_ACTIONS
OUTPUT_CONTRACT
```

If `WHY_DELEGATE` is weak, do the work directly.

## Good delegation cases

Delegate when a worker can produce evidence the root would otherwise obtain more slowly or with materially more context cost. Common cases:

- independent log or code-path investigation;
- adversarial review of a consequential change;
- large but bounded search or corpus inspection;
- independent verification of a competing hypothesis;
- isolated implementation in a disjoint worktree/branch/sandbox.

## Bad delegation cases

Do not delegate when:

- the root already knows the cause and fix;
- the task is a simple mechanical check;
- two workers would read or edit the same files for the same question;
- a previously verified gate is unaffected;
- the only reason is that agent slots exist;
- the worker cannot return distinct evidence.

## Concurrency

Start at 0. Use 1 specialist when one precise role is enough. The normal maximum is 2 concurrent specialists.

Use more than 2 only for truly independent high-volume work where the host can sustain isolation and the coordination cost is justified. Never create a fan-out tree simply to consume available parallelism.

## Worker permissions

Default worker mode: **read-only**.

A writing worker requires all of:

1. implementation is authorized by the user;
2. `ISOLATE_WORKERS` is proven;
3. disjoint ownership is explicit;
4. integration remains with the root;
5. validation is specified;
6. no consequential external action is delegated implicitly.

## Worker return contract

Read-only specialists should normally return:

```text
FINDING
EVIDENCE
CONFIDENCE
AFFECTED_SURFACE
RECOMMENDED_NEXT_CHECK
```

Writing specialists should additionally return:

```text
FILES_CHANGED
VALIDATION_RUN
INTEGRATION_NOTES
```

The root independently verifies material claims before acting on them.

## Nested delegation

Do not assume nested delegation exists. A worker may create children only if the runtime supports it and the root explicitly grants coordination ownership. Otherwise every worker is a leaf.

## Human-readable spawn disclosure

When the host exposes model selection and spawning is visible to the user, disclose the requested role and capability tier before spawning. Treat the selection as a request until the runtime confirms what was actually used.
