# 062 · Validate a purchase inquiry

**Estimate** 45 minutes · **Stage** Inquiries  
**Prerequisites** #22

## In brief

Make sure every request has a place, payment preference and usable date.

## Technical steps

1. In `inquiries.py`, implement `validate_inquiry(data)` using `pickup_location`, `payment_method`, and `preferred_date`. Trim and check lengths, accept only known payment methods, and parse an ISO calendar date today UTC or later.
2. Return normalized values or field errors through `AppError`. Keep validation reusable by create and edit.

## In first-time-coder language

1. Read the buyer's meeting note. Make sure there is a place, a chosen payment preference, and a real date that has not passed.
2. If one answer is wrong, tell the person which box to fix. Use the same checks when they edit their note.

## Check your work

- [ ] Valid data returns parsed clean fields.
- [ ] Blank location, unknown payment, impossible and past dates are refused separately.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [Python dates and ISO strings](https://docs.python.org/3/library/datetime.html)
- [Harvard CS50 Python conditionals lecture notes and examples](https://cs50.harvard.edu/python/notes/1/)
- [MDN form validation guide with runnable examples](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 062, Validate a purchase inquiry. Teach me the prerequisite ideas for date parsing, boundary validation, and shared field errors. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 062, Validate a purchase inquiry, using the acceptance checks I paste below. Check all field limits and try a bad calendar day and the UTC-today boundary. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
