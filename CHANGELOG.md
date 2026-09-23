# Changelog

All notable public changes will be documented here.

## [1.0.1] - 2026-09-23

### Added

- official `gh skill preview` and `gh skill install` quick-start commands;
- animated delegation/evidence demo and repository social-preview asset;
- reusable launch kit for technical community posts and short-form demos;
- reproducible launch-asset generator.

### Security

- enabled GitHub secret scanning and push protection;
- added active rulesets preventing deletion or history rewrite of `main` and preventing updates/deletion of `v*` release tags.

### Clarified

- distinguished the project from semantic-versioning/deployment-pipeline tools that share the `release-orchestrator` name.

## [1.0.0] - 2026-09-10

### Added

- provider-agnostic `release-orchestrator` core skill;
- runtime capability gate;
- evidence-first release protocol;
- bounded delegation decision gate;
- isolated-writing requirements for parallel workers;
- vendor-neutral model capability tiers: `FAST`, `BALANCED`, `STRONG`, `FRONTIER`;
- proportional validation and evidence freshness rules;
- adapters for Codex, Claude Code, Gemini CLI/Google, Cursor, GitHub Copilot, and generic LLM agents;
- public examples for bug fixes, release readiness, incidents, and security reviews;
- MIT license, contribution guidance, and security policy.

### Changed from the private precursor

- removed customer/project-specific terminology and paths;
- removed provider-specific model names from the core policy;
- replaced fixed model routing with capability tiers;
- updated delegation policy to support optional isolated writing workers on runtimes that genuinely isolate state;
- retained root ownership and evidence-over-consensus as invariants.
