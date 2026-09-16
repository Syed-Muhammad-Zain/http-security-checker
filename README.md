Day 4 HTTP Security Checker
============================

Purpose
-------
A small Python CLI for authorized lab environments.

The tool checks an HTTP target and reports:
- HTTP status code
- Security headers
- JSON results
- CSV results

Authorized Use
--------------
Use this tool only against systems that you are explicitly
authorized to test.

Current Lab Target
------------------
http://127.0.0.1:8000

Usage
-----
python guided_http_check.py --target http://127.0.0.1:8000

Multiple Targets
----------------
python guided_http_check.py --target http://127.0.0.1:8000 --target http://127.0.0.1:8000

Timeout
-------
HTTP requests use a 5-second timeout.

Security Headers Checked
------------------------
Strict-Transport-Security
Content-Security-Policy
X-Content-Type-Options
X-Frame-Options
Referrer-Policy

Output
------
JSON output is printed to the terminal.

CSV output is saved as:
http_audit.csv

Testing
-------
The test plan includes:
1. Valid local target
2. Unavailable local port
3. Missing target argument
4. Multiple targets

Limitations
-----------
This tool reports HTTP behavior and security-header presence.
A missing header is not automatically proof of a vulnerability.
Further manual validation is required.