# Lab 7 - Fuzz Testing

Dabbugunta Venya Anand - PES1UG24AM074.

## Submitted deliverables

- [PDF report with screenshots](Lab7_FuzzTesting_Report.pdf) - Original application crash, failing fuzz tests, corrected application and passing tests.
- `processor.py` - Fixed quota parser, compression ratio calculation and bandwidth tier lookup.
- `test_processor.py` - Hypothesis safety and valid-input properties, regression cases and command-line checks.

`requirements.txt` provides pytest and Hypothesis. `pytest.ini` excludes generated folders from discovery.

## Run

```bash
python -m pip install -r requirements.txt
python -m pytest test_processor.py -q
python processor.py
```

The completed suite contains 54 passing tests. Property tests use up to 300 generated examples per property. Invalid input is handled safely, and the command-line program continues after rejected input. Before/after screenshots are included in the PDF.
