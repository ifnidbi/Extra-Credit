# 042 · Make a shared browser Fetch helper

**Estimate** 45 minutes · **Stage** Foundation  
**Prerequisites** #12, #13, #37

## In brief

Let pages make requests and show success or errors consistently.

## Technical steps

1. Create `static/api.js` with `requestJson(path, options)`. Read the page's CSRF token for same-origin writes, encode plain JSON, leave FormData boundaries to the browser, and handle 204 without parsing JSON.
2. Parse the shared envelope, expose HTTP/field messages to callers, and distinguish network failure from HTTP failure. Try it against health and one safe test route.

## In first-time-coder language

1. Write one helper that asks your own server to do something. It should understand normal replies, an empty success, and something going wrong.
2. Teach it to bring the site's hidden pass for changes and to let a photo form keep its own packaging.

## Check your work

- [ ] A JSON success, 204, structured failure and network failure each follow a known path.
- [ ] The helper sends CSRF on writes and works with FormData without overwriting the file request's content type.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [MDN Using Fetch with examples](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [Flask-WTF CSRF protection for forms and Fetch](https://flask-wtf.readthedocs.io/en/1.2.x/csrf/)
- [MDN sending files and fields with FormData](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest_API/Using_FormData_Objects)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 042, Make a shared browser Fetch helper. Teach me the prerequisite ideas for Fetch promises, response status, JSON envelopes, and multipart forms. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 042, Make a shared browser Fetch helper, using the acceptance checks I paste below. Check handling of 204, HTTP and network errors, same-origin writes, and safe header defaults. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
