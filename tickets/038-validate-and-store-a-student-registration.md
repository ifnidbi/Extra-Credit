# 038 · Validate and store a student registration

**Estimate** 60 minutes · **Stage** Accounts  
**Prerequisites** #15, #37

## In brief

Allow students from different schools to register with the same form rules.

## Technical steps

1. In `accounts.py`, define `AccountRegistration`, `validate_registration(data)`, and `register_account(data)`. Normalize email, validate syntax, require name, school, attestation and password length, and prepare field errors.
2. Add `find_by_email` and `insert_student` to `account_repo.py`. Hash using Werkzeug, enforce role user server-side, and map duplicate email to 409 even if two requests race.

## In first-time-coder language

1. Check every box on a new signup slip. Students can enter any school email format that is valid and must confirm they are a student.
2. Save a scrambled password check value and always make the new account a regular user. Give a friendly message for repeat addresses.

## Check your work

- [ ] Two fictional users with different email domains can register, while invalid email, missing attestation, or duplicate normalized email are rejected.
- [ ] The database contains a derived hash and the new row is role user even if a request tries to supply something else.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [Werkzeug password-hash and security helpers](https://werkzeug.palletsprojects.com/en/stable/utils/#security-helpers)
- [Connector/Python parameter binding with cursor execute](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html)
- [Harvard CS50 Python conditionals lecture notes and examples](https://cs50.harvard.edu/python/notes/1/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 038, Validate and store a student registration. Teach me the prerequisite ideas for normalization, validating form fields, password hashing, and unique conflicts. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 038, Validate and store a student registration, using the acceptance checks I paste below. Check registration edge cases, role assignment, how the unique constraint is handled, and where the raw password goes. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
