# 013 · Standardize app and API errors

**Estimate** 60 minutes · **Stage** Foundation  
**Prerequisites** #9

## In brief

Return friendly errors consistently across HTML and JSON.

## Technical steps

1. Create `extracredit/errors.py` with `AppError`, its `status`, `code`, `message`, and optional `fields`, plus handlers registered from the factory.
2. Respond with the architecture envelope for API failures and simple HTML otherwise. Preserve expected HTTP codes including 400, 404, 405, and 413. Log unexpected failures privately.

## In first-time-coder language

1. Make one place that decides how to explain errors. A page should show a readable message and a browser request for data should get a structured message.
2. Check that the problem still has the right number, and keep the confusing internal details in the server logs.

## Check your work

- [ ] An unknown page and an unknown API URL both return 404 in their own formats.
- [ ] A known AppError carries its field message, and a generic 500 exposes no stack trace.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [Flask error handling reference and examples](https://flask.palletsprojects.com/en/stable/errorhandling/)
- [MDN overview of HTTP diagrams and examples](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 013, Standardize app and API errors. Teach me the prerequisite ideas for HTTP status codes, Flask error handlers, and structured exceptions. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 013, Standardize app and API errors, using the acceptance checks I paste below. Check the different request types and verify expected statuses and private logging survive handling. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
