# 039 · Build the student signup page

**Estimate** 45 minutes · **Stage** Accounts  
**Prerequisites** #12, #37, #38

## In brief

Connect the registration rules to a beginner-friendly form.

## Technical steps

1. In `routes/auth.py`, wire GET/POST `/register` and template `auth/register.html`. Label fields and checkbox, include CSRF token, call `register_account`, and redirect after success to login when available or the home route until it lands.
2. Show per-field errors and preserve only safe fields on validation failure. Register the auth blueprint.

## In first-time-coder language

1. Make a page where a student types their name, school, email and a password and ticks a student box.
2. When a field is wrong, put a helpful message next to it and leave the password box empty. After a good signup, send them onward.

## Check your work

- [ ] Valid form submission creates a user and redirects.
- [ ] An invalid form shows field errors with no saved row, and the password is never repopulated.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [MDN illustrated guide to your first HTML form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Your_first_form)
- [Flask-WTF CSRF protection for forms and Fetch](https://flask-wtf.readthedocs.io/en/1.2.x/csrf/)
- [Flask tutorial on authentication blueprint and session](https://flask.palletsprojects.com/en/stable/tutorial/views/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 039, Build the student signup page. Teach me the prerequisite ideas for GET versus POST, HTML labels, redirects, and field errors. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 039, Build the student signup page, using the acceptance checks I paste below. Check registration dispatch and whether passwords or submitted roles are echoed, stored, or trusted. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
