# Semester Project Report Outline

## 1. Process Model Selection and Justification
- Chosen model: Agile-inspired iterative process.
- Justification: supports evolving requirements, frequent feedback, modular development, and regular refactoring.
- Evidence from the project: iterative module delivery, seed data updates, sprint-style feature additions, and SPI adjustments.

## 2. Software Process Improvement (SPI)
- SPI activities performed: code refactoring, increased test coverage, UI improvement, and logging enhancement.
- How improvement was tracked: database review records, test status records, and commit history.
- Project outcome: more maintainable code, improved validation, and a stronger QA workflow.

## 3. Version Control Implementation
- Simulated Git-style version control in the `modules/version_control.py` and database `commits` table.
- Features: commit history viewer, branch explanation, and change record tracking.
- Academic justification: demonstrates version tracking and release management concepts.

## 4. Lehman’s Law Justification
- Evidence of continuous system evolution: new modules, UI enhancements, and improved testing over time.
- Feature expansion: added process models, refactoring lab, exception lab, peer review module, deployment planning, and team management.
- Complexity management: modular architecture and refactoring to keep growth sustainable.

## 5. Deployment Management
- Deployment plan: package the application using PyInstaller for Windows executable.
- Deployment topics covered: packaging, installers, release notes, and environment setup.
- If applicable: desktop shortcut creation, configuration file generation, and a repeatable build process.

## 6. Refactoring and Legacy Removal
- Evidence of refactoring: modular code organization, separation of controllers and views, and utility helpers.
- Legacy removal: replaced generic error handling with custom exceptions; improved validation and database error transparency.
- Benefits: easier maintenance, improved readability, and better testing.

## 7. Unit Testing and Automated Testing
- Existing tests: `tests/test_auth.py`, `tests/test_database.py`, `tests/test_validators.py`.
- Testing scope: authentication, database operations, and input validation.
- Automation: use `python -m unittest discover tests` to run the suite.

## 8. Exception Handling
- Exception strategy: custom exception classes in `utils/exceptions.py`.
- Handling patterns: `try/except` in UI actions, logged database errors, and user-friendly messages.
- Examples: authentication errors, validation errors, database failures.

## 9. Peer Review Implementation
- Peer review module: `modules/peer_review.py` provides walkthrough checklists and review status content.
- Review records: seeded `reviews` table and tracked review outcomes.
- Academic purpose: shows structured inspection and team feedback practices.

## 10. Team Roles and Learning Outcomes
- Role categories: project lead, developer, tester, reviewer.
- Contribution tracking: content modules, code quality, testing, and documentation.
- Learning outcomes: software construction, process modeling, version control, refactoring, testing, exception handling, and teamwork.
