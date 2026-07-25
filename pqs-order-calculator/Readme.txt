PQS ORDER CALCULATOR - BUILD INSTRUCTIONS
=========================================

Purpose
-------
The build script automates four stages:
1. Cleans old build, test-cache and distribution files.
2. Compiles the Python source code to check for syntax errors.
3. Runs five pytest unit tests. The assessment intentionally requires three
   passing tests and two failing tests, so the script continues after the
   expected test failures.
4. Creates a deployable package at dist/pqs_order_calculator.pyz.

Prerequisites
-------------
- Python 3.10 or later
- pip

Set-up
------
Open Terminal, Command Prompt or PowerShell in the repository folder and run:

    python -m pip install -r requirements.txt

Run the automated build
-----------------------
Windows:

    python build.py

macOS or Linux:

    python3 build.py

Expected results
----------------
- Compilation succeeds.
- Pytest reports: 3 passed and 2 failed.
- The package is created at:

    dist/pqs_order_calculator.pyz

Run the deployable package
--------------------------
Windows:

    python dist/pqs_order_calculator.pyz

macOS or Linux:

    python3 dist/pqs_order_calculator.pyz

The two failing tests are deliberately incorrect for the assessment. In a real
CI/CD pipeline, failing tests would block a merge until corrected.
