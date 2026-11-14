# Contributing to Vibe Coding Reference

Thank you for your interest! Bug reports, usage feedback, documentation fixes, translations and tests are welcome in French or English. VCR is a prototype maintained as maintainers' time permits; response times are not guaranteed.

## Before you start

- Search for an existing issue. For a substantial change, open an issue to discuss the need and scope before writing code.
- Never publish secrets, personal data, private reports or session histories. For security concerns, see [SECURITY.md](SECURITY.md).
- Use fictional projects and artificial data for reproductions and tests.
- See [AGENTS.md](AGENTS.md) for project rules and the [prototype status](docs/IMPLEMENTATION_STATUS.md) for known limitations. These documents are currently in French.

## Prepare and check a change

Python 3.11 or newer and Git are required. From a repository clone:

```sh
git switch -c fix/short-description
export PYTHONPATH="$PWD/src"
python3 -m vcr --help
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

On PowerShell, use `$env:PYTHONPATH = "$PWD/src"` and `python` if needed. This Windows workflow has not been verified. Tests use fixtures and require neither an API key nor network access. Installing development dependencies is not necessary for this command.

Keep changes focused and add relevant functional tests for changed behavior. Verify documentation changes, including commands and links. VCR does not run scripts from an inspected project, modify the target or contact a service during use. Proposals remain subject to human review; observed facts and limitations must remain distinct. No homemade token or performance benchmark is requested.

## Propose a change

1. Create a branch and open a pull request to `main` from your fork or authorized branch.
2. Describe the problem, solution, commands run and limitations using the provided template.
3. Wait for review and CI checks. Discussion may lead to a different approach or to the change not being accepted.

For a bug, include VCR, Python and OS versions, steps using a minimal fixture, and observed and expected results. Agent instructions do not replace human judgment or the contribution rules.
