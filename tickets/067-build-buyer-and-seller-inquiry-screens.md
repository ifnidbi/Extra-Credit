# 067 · Build buyer and seller inquiry screens

**Estimate** 60 minutes · **Stage** Inquiries  
**Prerequisites** #42, #49, #66

## In brief

Let students arrange pickup through the browser without page refreshes.

## Technical steps

1. Add a buyer inquiry form to listing detail, GET `/inquiries` with incoming/outgoing controls, `inquiries/index.html`, and `static/inquiries.js`. Use Fetch for create, list, edit, withdraw, accept, and decline. Use role and state to surface the right buttons, and only render contact links returned to that participant.
2. Show pending, success, empty and error messages, and refresh relevant rows after the server responds.

## In first-time-coder language

1. Give the buyer a short meeting form and a place to see sent requests. Give the seller a list of requests on their own items with approve and refuse buttons.
2. When you submit or change one, update the request list and show what the server said.

## Check your work

- [ ] Two demo users can complete the inquiry journey through the pages without a full reload on each action.
- [ ] Each participant sees only permitted controls and contacts, with readable validation and conflict feedback.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [MDN Using Fetch with examples](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [MDN illustrated guide to your first HTML form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Your_first_form)
- [MDN DOM manipulation lesson and examples](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 067, Build buyer and seller inquiry screens. Teach me the prerequisite ideas for dynamic forms, scoped role controls, and refreshing participant data. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 067, Build buyer and seller inquiry screens, using the acceptance checks I paste below. Check every visible action calls the right API and contact and error states follow participant rules. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
