# 07 — Changes since v0.2, corrected errors and open decisions

**Date: November 14, 2026.** This package does not retroactively replace v0.1/v0.2 documents: it preserves them and flags implementation choices that changed.

## What changed since v0.2

| Topic | v0.2 on November 12 | Prototype direction on November 14 |
|---|---|---|
| Deliverable | Mainly documentary reference | Documentation repository + minimal local tool + reports and prompts, without a new model |
| Workflows | START / RESCUE, cross-cutting domains | START / RESCUE / supervised IMPROVE, accessible TOKEN EFFICIENCY |
| Agent | Bibliography, prompts, procedures | Local scripts produce evidence + existing host agent interprets |
| Interface | Undecided | CLI menu and Markdown/JSON reports; optional static HTML; no SaaS |
| Self-improving harness | Emerging possibility | Incident-based proposal management; recursive loop not activated |
| Graphs/RAG | Advanced research | Planned interfaces; laboratory-only integrations; native search first |
| Skills | External skill catalog and selection | No custom creation, no bulk installation, versioned entries |
| Tokens | Cross-cutting domain, cost distinctions | Dedicated command using actually available data and explicit limits |
| Quality | Test quality and validation | Schemas, evidence, confirmation status, safety and fixture tests |

## Important factual corrections

1. **SWE-Skills-Bench:** use **version 2 from October 2026** as the current reference for the 98/92/4/2 results. Figures from the first March version are not interchangeable.
2. **No universal skill gain:** an official or popular skill may be useful without experimental validation; the reference study is contextual.
3. **Tokens ≠ prices ≠ quotas:** compression may reduce success and increase cost. Do not convert cache reads into ordinary consumption or invent a subscription bill.
4. **Graphs/vectors:** literature does not support recommending them systematically; a study of eleven production harnesses finds deterministic code search without embedding-based code retrieval in that sample.
5. **The screenshot's “The End of Harness Engineering” paper:** a visual/social post exists, but the screenshot does not establish a primary scientific source. Do not cite it as a verified publication or proof that humans are unnecessary.
6. **Google Harness²:** real repository and research paper verified; Codex setup conditions require sandbox precautions. Do not install on the real repository by default.
7. **The v0.1 “Patrimoine” case:** historical RESCUE example, not a fixture or available source code to reuse. Never infer that this repository can access the user's real code.
8. **AGENTS.md:** research results conflict; retain only short operational guidance, not a huge mandatory policy.

## Decisions a human must confirm before publication

- **License** for the new open-source repository: MIT or Apache 2.0, considering liability, redistribution and contributions; do not mix external code without checking.
- **Public name** and slogan; “Vibe Coding Reference” remains the working name.
- **Promised platforms** (macOS/Linux first, Windows if tests are available).
- **Possible HTML UI** alongside the terminal, guided by actual ease for beginners.
- **Codex/Claude trace collection policy** if advanced import is proposed: consent, redaction, retention and deletion.
- **Third-party extension policy:** who may recommend/install and how to isolate permissions.
- **Catalog maintenance:** review cadence and owners to avoid stale recommendations.

## Hypotheses that must not become facts in Codex

- “A modular monolith is optimal architecture for all agents” — unproven.
- “Adding a second reviewing agent always improves quality” — depends on context and cost.
- “More navigation tools means fewer tokens” — depends on success and cache.
- “A green PR proves business quality” — no.
- “Regex secret detection is a confirmed incident” — no.
- “No imports means dead code” — no.

## Condition for scope changes

If Codex finds a radically simpler or much more powerful option, it must:

1. summarize the concrete problem addressed;
2. cite evidence or identify it as a hypothesis;
3. compare setup and maintenance costs with the minimal solution;
4. explain security and compatibility implications;
5. propose a reversible change for human approval.

Complex innovation is allowed, but must never be **hidden in the backend merely because it is technically interesting**.
