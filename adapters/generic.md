# Generic LLM / agent adapter

Release Orchestrator can still be useful when the host has no native Agent Skills loader.

## Prompt mode

Provide the contents of `skills/release-orchestrator/SKILL.md` as reusable system/developer instructions or prepend it to the task context, subject to the host's instruction hierarchy.

Do not pretend unavailable tools exist. Set capabilities only from the actual harness.

Examples:

- chat-only model: all execution capabilities false; use the protocol for planning/review;
- API agent with filesystem tools: enable only file capabilities actually exposed;
- local agent with shell and Git: enable those, but keep `SPAWN_AGENTS=false` unless the harness implements workers;
- custom multi-agent harness: enable spawning/isolation only if the implementation provides them.

## Model routing

If your harness supports several models, map them to the four capability tiers. If it does not, use one model and reduce cost through scope and tool choice.

## Safety

The skill never overrides the host's system instructions, security policy, sandbox, tool permissions, or human approval gates.
