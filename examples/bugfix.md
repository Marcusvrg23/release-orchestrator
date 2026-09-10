# Example: bounded bug fix

User request:

```text
Fix the checkout error. Do not deploy.
```

Recommended behavior:

1. capability gate;
2. inspect repository state and payment-path instructions;
3. reproduce the error;
4. define expected vs actual behavior;
5. stay root-only if the cause is obvious;
6. make the smallest fix;
7. run targeted payment tests plus adjacent regression checks;
8. do not deploy because deployment was not authorized;
9. report evidence and remaining risk.

A second agent is not useful merely because payment code is important. Delegate only if an independent investigation or adversarial review will materially improve evidence.
