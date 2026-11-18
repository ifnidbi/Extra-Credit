# 068 · Register and read the ten database views

**Estimate** 60 minutes · **Stage** Reports  
**Prerequisites** #14, #27, #28, #29, #30, #31, #32, #33, #34, #35, #36, #37

## In brief

Give reports a predictable, safe route from a short URL key to one SQL view.

## Technical steps

1. In `reports.py`, create fixed `REPORTS` definitions for view names, columns, display labels and order from the database guide. In `report_repo.py`, implement `fetch_view_rows(report_definition)`. Only fixed identifiers can enter SQL. Add `get_report(report_key)`.
2. In `routes/reporting.py` expose admin-only GET for a single registered view and map an unknown key to 404. Serialize ordered columns and records consistently.

## In first-time-coder language

1. Make a lookup card for each of the ten reports. The short name on a link points to exactly one known database question and its display headings.
2. Read the selected report from MySQL, and only show the answer when an admin asks for it.

## Check your work

- [ ] Every registered key returns the intended view and columns in deterministic order.
- [ ] Unknown keys and unauthorized callers are refused. No caller-supplied string becomes a SQL identifier.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL SELECT reference including filters and ordering](https://dev.mysql.com/doc/refman/8.4/en/select.html)
- [Harvard CS50 SQL views lecture and examples](https://cs50.harvard.edu/sql/weeks/4/)
- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 068, Register and read the ten database views. Teach me the prerequisite ideas for SQL views, allowlisted identifiers, and role-gated reports. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 068, Register and read the ten database views, using the acceptance checks I paste below. Check the registry covers all ten unique views and allows only fixed SQL names, correct columns, and admin access. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
