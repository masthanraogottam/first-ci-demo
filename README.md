# First CI Demo

A small Python project demonstrating automated testing with GitHub Actions.

## Project files

- `result_logic.py` — determines whether a student passes based on internal marks and attendance.
- `test_result_logic.py` — unit tests for pass/fail scenarios.
- `.github/workflows/ci.yml` — runs the unit tests automatically on pushes and pull requests targeting `main`, and supports manual runs.

## Result rules

The project returns `PASS` when internal marks are at least 40 and attendance is at least 75. Otherwise, it returns `FAIL`.

## Run locally

Requires Python 3.11 or compatible.

```bash
python -m unittest discover -v
```

## GitHub Actions

After pushing to `main` or opening a pull request targeting `main`, open the **Actions** tab in this repository to view the Python CI workflow and test results. You can also run it manually using **Run workflow**.
