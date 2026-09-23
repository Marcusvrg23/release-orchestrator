# Security policy

Release Orchestrator is an instruction bundle. A malicious or overly permissive skill can still influence an agent with access to powerful tools.

## Security design

The public skill intentionally:

- does not include credentials, customer data, production logs, or private application source;
- does not pre-authorize shell/bash tools;
- treats unknown capabilities as unavailable;
- preserves host sandbox and approval systems;
- keeps workers read-only unless isolated writing is explicitly justified and authorized;
- separates analysis from consequential production, deployment, merge, publication, financial, and messaging actions.

## Reporting a vulnerability

Please avoid publishing secrets, proof-of-concept payloads against real third-party systems, or sensitive account data in a public issue.

Use GitHub private vulnerability reporting when available. If private vulnerability reporting is unavailable, contact the repository owner privately through an available GitHub channel.

## Supported versions

Security fixes are maintained for the latest public release and the current `main` branch.
