# 019 · Create the Categories table

**Estimate** 30 minutes · **Stage** Database  
**Prerequisites** #17

## In brief

Give listings a reusable list of categories.

## Technical steps

1. Write `sql/02_categories.sql` with unsigned generated `category_id` and required, unique `category_name`.
2. Apply it to the test database and try distinct, duplicate, and null names.

## In first-time-coder language

1. Make a small table for labels like Textbooks. Give every label its own number.
2. Try typing in the same label again and leaving one blank at the database level. See what the database says.

## Check your work

- [ ] Valid rows receive unique IDs.
- [ ] Duplicate and NULL category names are rejected by MySQL.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL CREATE TABLE reference with examples](https://dev.mysql.com/doc/refman/8.4/en/create-table.html)
- [Harvard CS50 SQL designing lecture and examples](https://cs50.harvard.edu/sql/weeks/2/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 019, Create the Categories table. Teach me the prerequisite ideas for auto-increment, unique columns, and required values. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 019, Create the Categories table, using the acceptance checks I paste below. Check I used the right types and that the test distinguishes an empty string from SQL NULL. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
