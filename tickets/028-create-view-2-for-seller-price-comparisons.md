# 028 · Create view 2 for seller price comparisons

**Estimate** 60 minutes · **Stage** Views  
**Prerequisites** #25

## In brief

Compare seller averages to categories using the required ANY pattern.

## Technical steps

1. In `sql/views/02_seller_price_comparison.sql`, create `v_seller_price_comparison`. Group per seller and currency. Use a nested ANY over category averages in that currency, with GROUP BY, following the contract.
2. Calculate one pass and one miss by hand or in isolated fixtures. Test a seller with different currencies separately.

## In first-time-coder language

1. Work out each seller's average for each kind of money. Compare it with the average for different categories using that same money.
2. Show the seller and currency when at least one category average is lower. Check examples that should appear and disappear.

## Check your work

- [ ] The SQL retains nested ANY and GROUP BY.
- [ ] Results match hand-computed examples and compare only rows sharing a currency.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL ANY and SOME subquery examples](https://dev.mysql.com/doc/refman/8.4/en/any-in-some-subqueries.html)
- [MySQL aggregate functions and group behavior](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 028, Create view 2 for seller price comparisons. Teach me the prerequisite ideas for ANY, grouped aggregates, and currency-scoped subqueries. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 028, Create view 2 for seller price comparisons, using the acceptance checks I paste below. Check the outer grouping and inner currency reference, then compare my pass and miss examples. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
