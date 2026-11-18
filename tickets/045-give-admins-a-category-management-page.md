# 045 · Give admins a category management page

**Estimate** 45 minutes · **Stage** Listings  
**Prerequisites** #42, #44

## In brief

Let the admin manage categories using simple browser controls.

## Technical steps

1. Render GET `/admin/categories` with an admin guard, `catalog/categories_admin.html` and `static/categories.js`. Show the live list from the API and hook up add, rename, and remove controls.
2. Refresh visible rows after success and keep controls usable when 400 or 409 returns. Use text nodes for names.

## In first-time-coder language

1. Make a page for the admin with buttons for add, rename and remove. Connect each button to the right database request through the app.
2. When the page gets a refusal, tell the admin which action failed and leave the old list visible.

## Check your work

- [ ] Admin can perform three permitted actions without reloading.
- [ ] An attempted removal of a category in use displays a helpful message, and ordinary users cannot load the page.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [MDN form validation guide with runnable examples](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
- [MDN Using Fetch with examples](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [MDN DOM manipulation lesson and examples](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 045, Give admins a category management page. Teach me the prerequisite ideas for form events, updating DOM rows, and showing conflicts. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 045, Give admins a category management page, using the acceptance checks I paste below. Check owner roles, request methods, and that category text is displayed safely after refresh. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
