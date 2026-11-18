# 050 · Refresh catalog results without reloading

**Estimate** 45 minutes · **Stage** Listings  
**Prerequisites** #42, #48, #49

## In brief

Use Fetch so filters update the list in place.

## Technical steps

1. Create `static/catalog.js` to capture search form submission, serialize filters with URLSearchParams, and call `GET /api/listings` through `requestJson`. Render items and statuses with safe text nodes.
2. Reset page on filter changes, keep pagination using current filters, and prevent stale responses from replacing newer results. Preserve the normal form fallback.

## In first-time-coder language

1. When someone presses Search, quietly ask the server for matching items and redraw only the list. Give them feedback while it loads or if nothing matches.
2. If they search again quickly, show the newest answer. Keep the simple form available if JavaScript is off.

## Check your work

- [ ] The network panel shows a Fetch request and no full-page navigation for an enhanced search.
- [ ] Empty, error and fast repeated searches show the right final state, and the no-JS form still works.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [MDN Using Fetch with examples](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [MDN URLSearchParams interactive reference](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)
- [MDN DOM manipulation lesson and examples](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting)
- [Chrome DevTools Network panel screenshot walkthrough](https://developer.chrome.com/docs/devtools/network/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 050, Refresh catalog results without reloading. Teach me the prerequisite ideas for form events, async search, race conditions, and progressive enhancement. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 050, Refresh catalog results without reloading, using the acceptance checks I paste below. Check the newest request wins, input is escaped, filters are preserved, and success/errors have visible states. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
