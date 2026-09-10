# Release gates

Use gates to prevent a release decision from becoming a vague feeling.

## Gate 1: candidate state

Know what is being evaluated:

- repository and branch/ref;
- intended changes;
- pre-existing local changes;
- target environment;
- explicit user constraints.

## Gate 2: blocker definition

For each release blocker, establish:

```text
EXPECTED
ACTUAL
REPRODUCTION_OR_EVIDENCE
AFFECTED_SURFACE
SEVERITY
```

Do not fix unrelated polish while a confirmed blocker remains open unless the user asks.

## Gate 3: change containment

Before integration, confirm:

- change addresses the demonstrated cause or requirement;
- blast radius is bounded;
- protected behavior remains intentionally unchanged;
- no unrelated refactor was smuggled into the fix.

## Gate 4: targeted validation

Run the smallest meaningful test that can fail if the fix is wrong. Then add adjacent checks if the changed dependency graph warrants them.

## Gate 5: integration evidence

Use real integration evidence when the claim crosses boundaries such as:

- browser/UI;
- database;
- external API/webhook;
- authentication/session;
- deployment/runtime configuration;
- filesystem/object storage;
- queue/worker/background job.

Mocks are useful but do not prove the external boundary itself.

## Gate 6: regression and policy checks

Run required project checks and any high-value regression checks. Avoid broad test repetition without a reason.

## Gate 7: release decision

Only the root makes the final decision.

Recommended states:

```text
NOT_READY
READY_FOR_FINAL_CHECK
RELEASE_READY
CANNOT_RELEASE
```

A release decision should state remaining known risks and any unverified external assumptions.

## Gate invalidation

Invalidate only gates affected by new changes or contradictory evidence. Preserve still-valid evidence instead of starting every release review from zero.
