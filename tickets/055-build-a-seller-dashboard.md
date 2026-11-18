# 055 · Build a seller dashboard

**Estimate** 45 minutes · **Stage** Listings  
**Prerequisites** #42, #49, #54

## In brief

Show a student their listings and let them finish a sale or remove an item.

## Technical steps

1. Add signed-in `/dashboard` to `routes/catalog.py` and `dashboard.html` using `list_seller_listings`. Add sold/remove actions through `static/dashboard.js` and the API. Add the dashboard link to the shared nav.
2. Show title, price/currency, campus and state. Render only applicable actions and readable 403/409 feedback from the server.

## In first-time-coder language

1. Make a page that shows only the items this student posted. Put buttons beside items when they can be marked sold or removed.
2. Change the item row after the server confirms the action and keep a message visible if it refuses.

## Check your work

- [ ] Seller A sees their own rows and never Seller B's private list.
- [ ] Actions update visible status without reload, and signed-out browsers are directed to login.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Flask tutorial on writing templates](https://flask.palletsprojects.com/en/stable/tutorial/templates/)
- [MDN Using Fetch with examples](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [MDN DOM manipulation lesson and examples](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting)
- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 055, Build a seller dashboard. Teach me the prerequisite ideas for owner-scoped lists, button events, and updating visible state. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 055, Build a seller dashboard, using the acceptance checks I paste below. Check dashboard scoping, server-confirmed state changes, and clear error feedback. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
