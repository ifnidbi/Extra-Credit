# 037 · Add session identity and permission checks

**Estimate** 90 minutes · **Stage** Accounts  
**Prerequisites** #10, #12, #13, #14, #18

## In brief

Give the app consistent rules for who is signed in and what they can do.

## Technical steps

1. In `security.py`, load an active student by session student ID using `account_repo.find_by_id` and expose `current_user()`. Add `require_login` and `require_admin` for HTML and JSON behavior from the contract.
2. Initialize Flask-WTF `CSRFProtect` from the app factory. Add HTML token support and a token meta element to the base template. Map CSRF errors to the app error shapes.

## In first-time-coder language

1. On every request, look up the account named in the signed login cookie. Check if it still exists and can sign in.
2. Give pages and API actions a shared door check for regular or admin access. Add a hidden token so the site can tell when a write came from its own form.

## Check your work

- [ ] Guest, ordinary and admin callers receive the intended HTML redirects or API statuses on a temporary protected endpoint or test.
- [ ] A missing CSRF token stops a write, and inactive accounts lose access even if they have old sessions.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [Flask tutorial on authentication blueprint and session](https://flask.palletsprojects.com/en/stable/tutorial/views/)
- [Flask-WTF CSRF protection for forms and Fetch](https://flask-wtf.readthedocs.io/en/1.2.x/csrf/)
- [Flask web application security guidance](https://flask.palletsprojects.com/en/stable/web-security/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 037, Add session identity and permission checks. Teach me the prerequisite ideas for signed sessions, decorators, role checks, and CSRF. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 037, Add session identity and permission checks, using the acceptance checks I paste below. Review session contents, redirects and API statuses, inactive-account behavior, and CSRF coverage. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
