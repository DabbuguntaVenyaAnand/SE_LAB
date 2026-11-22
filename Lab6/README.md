# Lab 6 - Code and Branch Coverage

Dabbugunta Venya Anand - PES1UG24AM074.

## Submitted files

- [Formal analysis report](Lab6_Code_Branch_Coverage_Report.pdf).
- `cloud_storage_tier.py` - Original application under test.
- `CodeCoverageTest_cloud_storage_tier.py` - Code coverage test suite.
- `BranchCoverageTest_cloud_storage_tier.py` - Branch coverage test suite.
- `test_cloud_storage.py` - Original starter tests.
- [Terminal screenshots](results/) - Code and branch coverage output.
- `requirements.txt` - pytest and coverage dependencies.

## Reproduce the results

Run from this folder.

```bash
python -m pip install -r requirements.txt
python -m coverage run --source=cloud_storage_tier -m pytest CodeCoverageTest_cloud_storage_tier.py -q
python -m coverage report -m --fail-under=90
python -m coverage run --branch --source=cloud_storage_tier -m pytest BranchCoverageTest_cloud_storage_tier.py -q
python -m coverage report -m --fail-under=90
```

Verified results are 7 passing code coverage tests with 100% statement coverage, and 41 passing branch coverage tests with 100% coverage across 57 statements and 40 branches. Both exceed the required 90%.

The imported history preserves the separate code coverage and branch coverage commits (`7ff3323` and `2944cd8`). The report and screenshots are the submitted evidence.
