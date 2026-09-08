# AgenticX Project 2 - CI/CD Pipeline

A small Python project with a GitHub Actions CI pipeline that runs automatically on pushes and pull requests.

## What it does

- Runs automated tests with pytest.
- Runs on every pull request targeting `main`.
- Runs on pushes to `main`.
- The `test` job can be configured as a required status check so failing changes cannot be merged.

## Local test

```bash
pip install -r requirements.txt
pytest -q
```

## CI/CD design decisions

1. Tests run automatically on pull requests before merge.
2. The workflow uses a clean Ubuntu runner and Python 3.12.
3. Dependencies are pinned for repeatable CI runs.
4. The `test` status check should be required in GitHub branch protection/rulesets.
5. A failing pull request should remain blocked until the tests pass.

## Verification

Create a branch, make a change that breaks a test, and open a pull request. The GitHub Actions check should fail. With the `test` check required on `main`, GitHub will block the merge.

Fix the change, push again, wait for the check to pass, and the pull request becomes mergeable.
