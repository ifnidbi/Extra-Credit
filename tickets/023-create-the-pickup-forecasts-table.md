# 023 · Create the Pickup Forecasts table

**Estimate** 45 minutes · **Stage** Database  
**Prerequisites** #18

## In brief

Give the external API feature somewhere to save its results.

## Technical steps

1. Write `sql/06_pickup_forecasts.sql` with the student FK, place label, coordinates, forecast date, temperature, chance of rain, and fetch timestamp.
2. Enforce coordinate bounds and precipitation probability at most 100. Test one representative row and one invalid number.

## In first-time-coder language

1. Make a table that remembers a city's forecast for the student who requested it. Save a date, a temperature, and a rain chance.
2. Try to save a rain chance above 100 percent. Check the database refuses it.

## Check your work

- [ ] A normal snapshot inserts with a generated ID and fetched time.
- [ ] Bad coordinates, probability greater than 100, and unknown student IDs fail.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL CHECK constraints and examples](https://dev.mysql.com/doc/refman/8.4/en/create-table-check-constraints.html)
- [MySQL CREATE TABLE reference with examples](https://dev.mysql.com/doc/refman/8.4/en/create-table.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 023, Create the Pickup Forecasts table. Teach me the prerequisite ideas for coordinates, percentage bounds, and snapshot tables. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 023, Create the Pickup Forecasts table, using the acceptance checks I paste below. Check column precision, date fields, bounds and foreign-key behavior against the weather feature. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
