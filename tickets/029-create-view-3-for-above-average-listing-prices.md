# 029 · Create view 3 for above-average listing prices

**Estimate** 45 minutes · **Stage** Views  
**Prerequisites** #25

## In brief

Use a correlated subquery to spot listings above their category average.

## Technical steps

1. In `sql/views/03_above_category_average.sql` define `v_above_category_average` with the contract columns. Correlate the average subquery to the current listing's category and currency.
2. Use strict greater-than. Compare a singleton, a row equal to its average, and a higher-priced row.

## In first-time-coder language

1. For every item, ask what similar items in the same category and currency cost on average. Show the item only if it costs more.
2. Try a category with one item and an item exactly at the average. Neither should appear.

## Check your work

- [ ] A higher-priced item in a multi-item group appears.
- [ ] Equal and singleton cases stay out, and a different currency never changes the comparison.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL correlated subquery examples](https://dev.mysql.com/doc/refman/8.4/en/correlated-subqueries.html)
- [MySQL aggregate functions and group behavior](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 029, Create view 3 for above-average listing prices. Teach me the prerequisite ideas for correlated subqueries and strict greater-than. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 029, Create view 3 for above-average listing prices, using the acceptance checks I paste below. Check both outer-row references and the boundary cases in my evidence. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
