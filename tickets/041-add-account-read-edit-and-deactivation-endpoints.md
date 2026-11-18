# 041 · Add account read, edit, and deactivation endpoints

**Estimate** 90 minutes · **Stage** Accounts  
**Prerequisites** #15, #40

## In brief

Give signed-in users control of their own basic profile.

## Technical steps

1. Implement `get_profile`, `update_profile` and `deactivate_account` in `accounts.py` and corresponding bound repository writes. GET /api/account returns only safe fields. PUT changes name and school. DELETE checks current password, blocks admin self-deactivation, updates active status and clears session.
2. Define JSON endpoints in `routes/auth.py`. Keep identity from the session and omit hashes and internal fields from responses.

## In first-time-coder language

1. Let the person see and edit their own profile name and school. Treat the account number on their signed-in ticket as the source of truth.
2. If they choose to deactivate, ask for their password again, turn off the account, and sign them out while keeping old records linked.

## Check your work

- [ ] An ordinary user can read and edit only their own profile.
- [ ] Deactivation clears the session, blocks login, preserves history, and fails on the wrong password or a demo admin account.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [MySQL UPDATE clauses and examples](https://dev.mysql.com/doc/refman/8.4/en/update.html)
- [Werkzeug password-hash and security helpers](https://werkzeug.palletsprojects.com/en/stable/utils/#security-helpers)
- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 041, Add account read, edit, and deactivation endpoints. Teach me the prerequisite ideas for self-service API permissions, server-owned identity, and soft deletion. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 041, Add account read, edit, and deactivation endpoints, using the acceptance checks I paste below. Check identity source, sensitive-field filtering, admin rule, and that a failed deactivation changes no data. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
