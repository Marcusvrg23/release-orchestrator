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

Before the repository is public, report security concerns directly to the repository owner through an available private GitHub contact channel. A dedicated private reporting channel can be added at public launch.

## Supported versions

Until `v1.0.0` is released, the repository is pre-release and only the latest `main` state is maintained.
