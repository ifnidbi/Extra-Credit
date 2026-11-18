# 033 · Create view 7 for category totals and averages

**Estimate** 45 minutes · **Stage** Views  
**Prerequisites** #25

## In brief

Show category counts even when no one has listed an item there.

## Technical steps

1. Create `sql/views/07_category_summary.sql` and `v_category_summary` with LEFT JOIN from Categories, grouping by category and currency. Count real listing IDs and average amounts within currency.
2. Check that a category with nothing listed gets zero plus NULL currency and average.

## In first-time-coder language

1. Keep every category on the page, including the empty ones. Group each category's prices by the kind of money they use.
2. Check that an empty category says zero items and has no average.

## Check your work

- [ ] Counts match seed records and currency groups stay distinct.
- [ ] The empty category has exactly one row showing 0 and NULL average.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL supported joins and syntax](https://dev.mysql.com/doc/refman/8.4/en/join.html)
- [MySQL aggregate functions and group behavior](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 033, Create view 7 for category totals and averages. Teach me the prerequisite ideas for COUNT(column), left joins, NULL averages, and grouping. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 033, Create view 7 for category totals and averages, using the acceptance checks I paste below. Check I did not count the empty join row or combine different prices in one currency group. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
