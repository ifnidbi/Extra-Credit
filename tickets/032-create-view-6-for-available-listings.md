# 032 · Create view 6 for available listings

**Estimate** 30 minutes · **Stage** Views  
**Prerequisites** #25

## In brief

Save an admin list of available items and their sellers.

## Technical steps

1. Write `sql/views/06_available_listings.sql` for `v_available_listings`, joining the listing, category, and seller. Return the specified contact and price fields, filtered to Available.
2. Query the result in currency, price, and ID order and compare allowed statuses.

## In first-time-coder language

1. Show the items currently marked for sale. Add the category and seller's contact details for admin use.
2. Look at some sold and reserved examples and check that they are absent.

## Check your work

- [ ] Every selected listing is Available and joins to the right seller.
- [ ] The view supplies currency and admin contact fields in the contract.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL supported joins and syntax](https://dev.mysql.com/doc/refman/8.4/en/join.html)
- [MySQL SELECT reference including filters and ordering](https://dev.mysql.com/doc/refman/8.4/en/select.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 032, Create view 6 for available listings. Teach me the prerequisite ideas for filters, column aliases, and deterministic ordering. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 032, Create view 6 for available listings, using the acceptance checks I paste below. Check the status predicate, joins, and that the ordering compares amounts within currency. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
