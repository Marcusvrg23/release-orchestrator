# Example: incident investigation

User request:

```text
Production login failures started after the last deploy. Find the cause; do not change production.
```

Recommended behavior:

- mark production writes as unauthorized;
- identify deploy/ref/time boundary;
- inspect logs/configuration read-only if accessible;
- compare the last known-good and current candidate;
- delegate one log investigator or one competing-hypothesis investigator only if it speeds diagnosis;
- keep findings tied to timestamps and refs;
- distinguish correlation from reproduced cause;
- propose the smallest corrective action and validation plan;
- do not roll back or deploy without authorization.
