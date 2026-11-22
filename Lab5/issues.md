# Scheduler issues and fixes

Line numbers refer to the original starter file, before edits. Bandit severity is reported exactly; functional bugs are identified by manual inspection and execution, not claimed as tool findings. No medium-severity Bandit findings were reported.

| Issue | Type | Line(s) | Description | Fix Approach |
| ----- | ---- | ------- | ----------- | ------------ |
| Shell command built from a filename | Security — High, Bandit B605 | 43 | A filename enters a shell command, allowing shell injection; `cat` also fails on Windows. | Remove `os.system` and display the log using Python file reading. |
| Shared mutable default | Bug — Pylint W0102 | 11 | The default equipment list is shared across calls; stored caller lists can also change later. | Default to `None` and copy each supplied list. |
| Silent broad exception | Reliability — Low, Bandit B110; Pylint W0702; Flake8 E722 | 27–28 | Every cancellation error is swallowed, hiding failures. | Use a dictionary lookup/removal with an explicit Boolean result for missing IDs. |
| Unreliable file cleanup | Resource handling — Pylint R1732, W1514 | 35–37, 40–43 | Files have no explicit encoding; the log is not closed before display. | Use `with open(..., encoding="utf-8")` for all file operations. |
| Unused local variables | Maintainability — Pylint W0612; Flake8 F841 | 46–47, 49 | Reservation IDs are assigned but never used. | Remove unnecessary assignments and make the demonstration explain validation failures. |
| Missing documentation and inconsistent naming | Maintainability — Pylint C0114, C0116, C0103 | 1, 11, 22, 30, 34, 39, 45 | The module/functions lack documentation and `logConflicts` uses inconsistent naming. | Add docstrings and rename the function to `log_conflicts`. |
| Spacing and long lines | Style — Flake8 E302, E305, E501; Pylint C0301 | 11, 14, 18, 22, 30, 34, 39, 45, 59 | Function spacing and line lengths violate style rules. | Add blank lines and wrap expressions to 79 characters. |
| Double bookings accepted | Functional bug — manual finding | 13–18 | A conflict is recorded but the conflicting reservation is still inserted. | Reject exact and partially overlapping bookings before changing state. Allow adjacent slots. |
| Invalid time slots accepted | Functional bug — manual finding | 11–18, 30–32, 48–49, 53–54 | Reversed ranges, integers and `10:30` can be stored. | Require HH-HH with 00 <= start < end <= 24; reprompt after invalid interactive input. |
| Equipment can be overallocated | Functional bug — manual finding | 16–18 | Stock can become negative, and unknown items can cause partially applied changes. | Count requested items and validate all stock before updating any quantities. |
| Import starts the program | Design bug — manual finding | 59 | Importing prompts for input and writes files. | Use an `if __name__ == "__main__"` guard. |

Equipment remains reserved until cancellation, preserving the starter's inventory model. This implementation does not reuse equipment across different time slots.
