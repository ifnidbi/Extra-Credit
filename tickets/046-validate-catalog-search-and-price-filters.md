# 046 · Validate catalog search and price filters

**Estimate** 45 minutes · **Stage** Listings  
**Prerequisites** #20

## In brief

Turn browser search values into a predictable set of filters.

## Technical steps

1. In `listings.py`, define `ListingFilters` and `parse_filters(args)` using the architecture fields. Validate IDs, positive page, known condition/currency, text limits and sanitized trim.
2. Use Decimal for prices, require a currency with price bounds, require min no greater than max, and raise field-specific errors for invalid values.

## In first-time-coder language

1. Make a checklist for the search boxes. Turn a category number into a number and remove extra spaces from search words.
2. If someone searches by price, ask which kind of money they mean. Reject an upside-down price range and point to the bad box.

## Check your work

- [ ] A normal query gives the expected criteria and default page.
- [ ] Bad page, category ID, price, condition, currency, and reversed bounds each get a readable error.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [Python exact decimal arithmetic](https://docs.python.org/3/library/decimal.html)
- [MDN URLSearchParams interactive reference](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)
- [Harvard CS50 Python conditionals lecture notes and examples](https://cs50.harvard.edu/python/notes/1/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 046, Validate catalog search and price filters. Teach me the prerequisite ideas for URL query values, typed fields, currency bounds, and Decimal values. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 046, Validate catalog search and price filters, using the acceptance checks I paste below. Check normalization, default fields, and malformed or non-finite price values. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
