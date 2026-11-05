# Static analysis reflection

The supplied handout refers to reflection questions but does not list them. The four questions below are provisional prompts covering the lab's learning outcomes; replace them if the instructor supplies the actual questions.

## 1. What did each analysis tool contribute?

Pylint identified code quality problems such as a mutable default argument, missing documentation, unused variables and unreliable file handling. Flake8 identified formatting violations and the bare exception handler. Bandit identified the high-severity shell-command risk and the silent exception handler. The tools overlapped in some areas but each added a different view.

## 2. Which issues were prioritized and why?

The shell command was the first priority because Bandit rated it high severity and it also failed on Windows. Replacing it with Python file reading removed the shell interpretation entirely. The silent exception handler, shared default, resource handling and style findings were also corrected. Reports contained no medium-severity Bandit findings.

## 3. What did static analysis miss?

Running and inspecting the starter revealed negative booking durations, duplicate room bookings and invalid slot values. The original program accepted `14-12`, the integer `1530`, and `10:30`. These require domain validation. Equipment availability also needed validation before updating stock. Static analysis alone cannot establish that a scheduling program follows its booking rules.

## 4. How were the fixes verified and what was learned?

All three tools were rerun after the changes. Pylint reached 10.00/10, Bandit reported no issues, and Flake8 reported no violations. Behavioral checks covered overlapping and adjacent bookings, invalid slots, equipment exhaustion, cancellation, input-list copying, JSON export and log output. A clean tool report is useful evidence of quality, but functional checks remain necessary to verify the program's purpose.
