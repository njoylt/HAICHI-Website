# HAICHI First 10 Leads Tracker

Status: draft candidates awaiting Antigravity review; no outreach has been sent.

Candidate-source guardrails:

- A public discussion is context, not permission to cold-DM its author.
- First participation must be useful without mentioning HAICHI or adding a link.
- Do not reply until the account-history and current community-rule gates pass.
- Record an actual reply only after it exists; never treat a draft as sent.

## Target profile

Prioritize people who already have the pain:

- uses Ollama or local models
- tries multiple AI coding tools
- has local scripts/terminals/chats scattered
- can understand local-first tradeoffs
- is willing to report install/workflow blockers

Avoid broad AI-curious audiences until the workflow is proven.

## Lead table

| # | Name / handle | Channel | Persona | Sent? | Reply | Personal request | Founder code request | Paid | Blocker | Next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `facu_75` | [r/LocalLLaMA: orchestrating agents without six terminals](https://www.reddit.com/r/LocalLLaMA/comments/1u99w8w/is_there_actually_a_good_way_to_orchestrate/) | Multi-agent developer; needs isolation, review, and manual intervention | No | — | — | — | — | Account and community gates are not passed | After the gates pass, contribute a no-link explanation of the minimum review packet: task, diff, tests, and stop reason. |
| 2 | `Stitch10925` | [r/LocalLLaMA: getting started with local agents](https://www.reddit.com/r/LocalLLaMA/comments/1ro7t3y/how_to_get_started_with_agents/) | Local .NET developer seeking refactoring, sanity-check, and code-review help | No | — | — | — | — | Older thread; confirm the question is still active before replying | Offer a short, product-neutral Reviewer -> Verifier starter workflow without a link. |
| 3 | `Dry_Shallot_3578` | [r/ollama: Claude Code alternatives](https://www.reddit.com/r/ollama/comments/1ux0p3z/claude_code_alternatives/) | Coding-agent user blocked by tool-call and subagent errors | No | — | — | — | — | HAICHI may not solve the specific Claude Code compatibility issue | If still relevant, explain the harness-versus-model distinction and suggest an isolated verification pass; do not pitch. |
| 4 | `thereisnospooongeek` | [r/LocalLLaMA: self-hosted code review](https://www.reddit.com/r/LocalLLaMA/comments/1u9rpnc/how_can_i_self_host_code_review/) | Developer seeking a repeatable private code-review path | No | — | — | — | — | Their desired GitHub Action flow differs from HAICHI's workstation workflow | Share a generic local review checklist only if it adds something not already answered in the thread. |
| 5 | `BLOCK__HEAD4243` | [r/LocalLLM: real uses for multi-agent workflows](https://www.reddit.com/r/LocalLLM/comments/1tb1c9j/what_are_you_using_your_multi_agent_workflows_for/) | Skeptical local-AI user asking for concrete non-demo value | No | — | — | — | — | Research candidate, not a sales lead yet | Observe the discussion and learn which concrete workflows resonate; do not introduce HAICHI unless directly relevant and permitted. |
| 6 | `r/LocalLLaMA: local agent UI vs CLI` | [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) | Developers seeking clean web UI for local agent coordination instead of terminal logs | No | — | — | — | — | Web UI preference vs CLI tooling | Observe discussions on local agent UX; share localhost dashboard principles without direct promotion. |
| 7 | `r/SelfHosted: dev tools` | [r/SelfHosted](https://www.reddit.com/r/SelfHosted/) | Solo developers looking for local-first workflow tools without SaaS subscriptions | No | — | — | — | — | Requires clear zero-cloud and offline installation proof | Address privacy and self-hosting questions with architectural facts. |
| 8 | `r/Ollama: multi-agent roles` | [r/Ollama](https://www.reddit.com/r/Ollama/) | Users running multiple Ollama models who want structured Reviewer/Verifier workflows | No | — | — | — | — | Model VRAM constraints when running 2 concurrent agents | Explain two-agent memory management and model tiering strategies. |
| 9 | `r/LocalLLM: zero-data leakage` | [r/LocalLLM](https://www.reddit.com/r/LocalLLM/) | Privacy-conscious engineers requiring offline guarantees | No | — | — | — | — | SmartScreen/code-signing trust barriers on Windows | Discuss local binary verification and SHA256 checksum audit practices. |
| 10 | `r/CommandLine: parallel agent workers` | [r/CommandLine](https://www.reddit.com/r/CommandLine/) | Engineers struggling with multi-terminal window clutter during agent runs | No | — | — | — | — | Command-line power user preference | Share clean terminal output and log isolation patterns. |

## Opt-in message after explicit interest

Do not send this as an unsolicited direct message. Use it only after a person
asks for the project link or explicitly says they are open to trying HAICHI.

I built HAICHI because my local AI workflow was split across Ollama, terminals, scripts, and separate agent chats.

The first workflow is simple:

1. Reviewer finds concrete risks.
2. Verifier challenges weak claims.
3. You keep only evidence-backed fixes.

Personal is free. I am looking for blunt feedback from people already using local models or agents.

If you want to try it, download Personal from `https://haichi.app`.

## Reply checklist

When someone responds, ask only what is needed:

- What OS?
- Did download/install work?
- Is Ollama already installed?
- What task did they try?
- Where did they stop?
- If they ask about Pro after trying Personal, what capability do they actually
  need?
