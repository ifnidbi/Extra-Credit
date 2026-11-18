# 027 · Create view 1 for listing details

**Estimate** 30 minutes · **Stage** Views  
**Prerequisites** #25

## In brief

Show one printable view of each listing, seller, and category.

## Technical steps

1. Create `sql/views/01_listing_details.sql` and `v_listing_details` with the columns in the database guide. Join Listings, Students, and Categories on their IDs.
2. Run it with a deterministic listing ID order and compare two result rows to their source records.

## In first-time-coder language

1. Make a saved question that starts with an item and looks up the person's name and category's name from two other tables.
2. Pick two items and check the answers by looking at the original rows.

## Check your work

- [ ] Exactly one row per seeded listing appears, with the right seller and category.
- [ ] Money includes the currency code.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL supported joins and syntax](https://dev.mysql.com/doc/refman/8.4/en/join.html)
- [Harvard CS50 SQL relating lecture, video and notes](https://cs50.harvard.edu/sql/weeks/1/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 027, Create view 1 for listing details. Teach me the prerequisite ideas for joining three tables, join keys, and view output columns. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 027, Create view 1 for listing details, using the acceptance checks I paste below. Check that both joins use IDs and do not multiply listings or pair them with the wrong people. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
