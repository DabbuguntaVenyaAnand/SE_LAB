# Static analysis reflection

The supplied handout requests reflection but does not contain specific reflection questions. This reflection describes the completed scheduler analysis and its results.

## Contributions of the tools

Pylint identified the shared mutable default argument, missing documentation, unused variables and unreliable file handling. Flake8 identified spacing, line length and bare exception handling issues. Bandit identified shell execution and silent exception handling risks.

## Prioritization and fixes

The high-severity shell execution finding was prioritized. Python file reading replaced the shell command. The broad exception handler was replaced with an explicit result for unknown cancellation IDs. Equipment lists are copied, file operations use context managers and UTF-8 encoding, and documentation and formatting were corrected. The reports contain no medium-severity Bandit findings.

## Limits of static analysis

Manual inspection also identified booking overlaps, invalid or reversed hour ranges and equipment allocation problems. These require checks against scheduling rules. The cleaned scheduler rejects overlaps and invalid ranges, validates equipment before updating state, and returns equipment when a reservation is cancelled.

## Verification and learning

The after reports record Pylint 10.00/10, no Bandit findings and no Flake8 violations. Re-running the program and checking booking behavior complements those reports. Static analysis helps identify coding and security issues, while functional verification checks that the scheduler follows its booking rules.
