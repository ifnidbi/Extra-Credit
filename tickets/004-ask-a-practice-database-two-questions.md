# 004 · Ask a practice database two questions

**Estimate** 30 minutes · **Stage** Practice  
**Prerequisites** None. Start any time.

## In brief

Use SQL to see how rows, filters, and ordering work.

## Technical steps

1. In a scratch SQL playground or your local database, use a tiny fictional inventory with `title` and `price`. Write one SELECT that returns every row and one SELECT that filters by price and orders by price.
2. Predict both result sets before running them. Save the statements and observed rows in your learning notes.

## In first-time-coder language

1. Put three imaginary items in a little table. Ask it to show everything, then ask it to show only affordable items from cheapest to most expensive.
2. Write down which items you expect to see, and compare when you run it.

## Check your work

- [ ] Both queries run and the filtered list excludes at least one row.
- [ ] Your notes show the prediction and the actual order.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Harvard CS50 SQL querying lecture, video and practice](https://cs50.harvard.edu/sql/weeks/0/)
- [MySQL SELECT reference including filters and ordering](https://dev.mysql.com/doc/refman/8.4/en/select.html)
- [SQLite project interactive browser playground](https://sqlite.org/fiddle/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 004, Ask a practice database two questions. Teach me the prerequisite ideas for rows, SELECT, WHERE, and ORDER BY. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 004, Ask a practice database two questions, using the acceptance checks I paste below. Check whether my query conditions and ordering actually produce the rows I predicted. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
