# 040 · Sign in and sign out with a session

**Estimate** 60 minutes · **Stage** Accounts  
**Prerequisites** #39

## In brief

Let verified credentials start and end a local app session.

## Technical steps

1. In `accounts.py`, implement `authenticate(email, password)` with normalized lookup, active check and Werkzeug verification. In `routes/auth.py`, implement GET/POST `/login` and POST `/logout`. Use uniform failure feedback and clear the session before setting or removing `student_id`.
2. Add `auth/login.html`, update registration redirect and shared nav links, and put a CSRF token in the logout form.

## In first-time-coder language

1. Make a page where the student uses their email and password. If the password check and account status pass, remember the account number for this browser.
2. Give them a button to sign out. Use the same gentle message for any failed login and try Tab on the form.

## Check your work

- [ ] A demo account signs in, remains signed in on another page, and is signed out by the token-protected POST.
- [ ] Wrong passwords and inactive users get the same failure message, and GET cannot sign someone out.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Flask tutorial on authentication blueprint and session](https://flask.palletsprojects.com/en/stable/tutorial/views/)
- [Werkzeug password-hash and security helpers](https://werkzeug.palletsprojects.com/en/stable/utils/#security-helpers)
- [Flask-WTF CSRF protection for forms and Fetch](https://flask-wtf.readthedocs.io/en/1.2.x/csrf/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 040, Sign in and sign out with a session. Teach me the prerequisite ideas for credential verification, resetting sessions, and logging out with POST. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 040, Sign in and sign out with a session, using the acceptance checks I paste below. Check how the session changes, generic error behavior, and protected logout. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
