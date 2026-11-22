# Lab 5 - Static Code Analysis

Conference room and equipment scheduler, completed by Dabbugunta Venya Anand (PES1UG24AM074).

## Submitted files

- `scheduler_system.py` - Cleaned scheduler with validation, safe file handling and shell execution removed.
- `issues.md` - Eleven documented tool findings and functional issues, with fixes.
- `reflection.md` - Reflection on the analysis and verification.
- `pylint_before.txt` and `pylint_after.txt` - Pylint reports.
- `bandit_before.txt` and `bandit_after.txt` - Bandit reports.
- `flake8_before.txt` and `flake8_after.txt` - Flake8 reports. An empty after report indicates no violations.

## Run and verify

```bash
python -m pip install pylint bandit flake8
python scheduler_system.py
python -m pylint scheduler_system.py
python -m bandit -r scheduler_system.py
python -m flake8 scheduler_system.py
```

Press Enter at the slot prompt to use `10-12`. The program exports `schedule.json` and writes `conflicts.log` locally.

The completed reports record Pylint 10.00/10, zero Bandit findings and zero Flake8 violations. The imported history preserves separate Bandit, Pylint and Flake8 fix commits.
