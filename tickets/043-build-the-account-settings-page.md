# 043 · Build the account settings page

**Estimate** 45 minutes · **Stage** Accounts  
**Prerequisites** #41, #42

## In brief

Show profile controls and deactivation without leaving the page.

## Technical steps

1. Add GET `/account` in `routes/auth.py`, `auth/account.html`, and `static/account.js`. Use the account API to load and update the profile, then send a password-confirmed deactivate action and redirect on success.
2. Show fields and status in accessible text. Reset the password field and avoid passing the secret through a URL.

## In first-time-coder language

1. Make a My Account page with a name and school form. Show a short update message next to it when the save works.
2. Give deactivation a separate password box. When it succeeds, take the person back to the signed-out site.

## Check your work

- [ ] A signed-in user can reload and see a saved change without exposing email changes or hidden account fields.
- [ ] Deactivation signs the user out, and wrong password gives feedback on the page.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [MDN illustrated guide to your first HTML form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Your_first_form)
- [MDN Using Fetch with examples](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [MDN DOM manipulation lesson and examples](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting)
- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 043, Build the account settings page. Teach me the prerequisite ideas for Fetch on form submit, accessible feedback, and destructive action UI. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 043, Build the account settings page, using the acceptance checks I paste below. Check that both actions honor HTTP responses and the password is only sent in the request body. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
