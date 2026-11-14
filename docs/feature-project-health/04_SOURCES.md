# Project Health Checklist sources and limitations

This add-on reuses decisions from VCR v0.2 and the November 14, 2026 implementation package. The sources below justify the **topics** of the checks; they do not prove that an automated VCR audit fully covers these standards.

## Official standards and references

- **OpenSSF Scorecard** — https://github.com/ossf/scorecard — project and repository security practices; its presence does not mean business tests pass.
- **OpenSSF Best Practices** — https://www.bestpractices.dev/ — open-source maintenance and quality criteria; adapt to public or private projects.
- **NIST SP 800-218 / SSDF** — https://csrc.nist.gov/pubs/sp/800/218/final — secure software development framework, not identical obligations for every script.
- **OWASP ASVS 5.0** — https://asvs.owasp.org/ — detailed web-security requirements; file-presence checks do not implement ASVS.
- **Google Engineering Practices** — https://google.github.io/eng-practices/ — code review, simplicity and change quality.
- **Google SRE Launch Checklist** — https://sre.google/sre-book/launch-checklist/ — production-launch checks, not fully applicable to a local tool.
- **OpenAI Harness Engineering** — https://openai.com/index/harness-engineering/ — navigable documentation, enforceable constraints and agent environments.

## Tools to reuse only when useful, installed and authorized

- **Git** — https://git-scm.com/docs — read repository status and remotes.
- **Gitleaks** — https://github.com/gitleaks/gitleaks — detect *potential* secrets; never reproduce discovered values.
- **OSV-Scanner** — https://github.com/google/osv-scanner — scan lockfiles and dependencies; network access may be needed depending on the mode.
- **Ruff** — https://docs.astral.sh/ruff/ — Python linting; conditional use.
- **ESLint** — https://eslint.org/ — JS/TS linting; conditional use.
- **Biome** — https://biomejs.dev/ — alternative JS/TS linting and formatting; do not add redundant tools without reason.
- **pytest** — https://docs.pytest.org/ — Python tests; executes project code and is not passive.
- **Vitest** — https://vitest.dev/ — JS/TS tests; executes project code.
- **GitHub Actions** — https://docs.github.com/en/actions — CI; workflow files do not prove execution.
- **Import Linter / Dependency Cruiser** — https://import-linter.readthedocs.io/ / https://github.com/sverweij/dependency-cruiser — architecture-boundary checks for sufficiently complex projects only.

## Research relevant to VCR's *limitations*

- **Agent Retrieval Bench** — https://arxiv.org/abs/2607.24882 — difficulty retrieving relevant files; do not automatically install a vector database.
- **Evaluating AGENTS.md** — https://arxiv.org/abs/2602.11988 — additional instructions do not always improve success; a long AGENTS.md is not a goal.
- **SWE-Skills-Bench** — https://arxiv.org/abs/2603.15401 — coding skills have variable effectiveness; prefer careful selection.
- **SWE-Mutation** — find complete bibliographic references in the existing v0.2; agent-generated tests can be weak, making business tests important.

## Editorial precautions

- An installed tool does not establish compliance with a standard it only partially covers.
- P0/P1/P2 risks are **our product conventions**, not the cited organizations' classification.
- Control of changes and truthfulness of results matter more than a summary score.
- Study percentages are **not** guaranteed performance for `vcr check`.
