# 018 · Create the Students table

**Estimate** 45 minutes · **Stage** Database  
**Prerequisites** #17

## In brief

Store student accounts, role, and active state.

## Technical steps

1. Write `sql/01_students.sql` with the ID, name, email, password hash, school, role, and active status from the database contract.
2. Check the PK, unique email, required columns and defaults using synthetic rows in the test database.

## In first-time-coder language

1. Make a table where one row stands for one account. Give each student a number and keep their school and email with that number.
2. Try using the same email twice. Look at the automatic normal-user and active values on a fresh row.

## Check your work

- [ ] A normal insert receives a new ID, role user, and active status.
- [ ] A duplicate email fails, and the schema stores a hash field rather than a plain-password field.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL CREATE TABLE reference with examples](https://dev.mysql.com/doc/refman/8.4/en/create-table.html)
- [Harvard CS50 SQL designing lecture and examples](https://cs50.harvard.edu/sql/weeks/2/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 018, Create the Students table. Teach me the prerequisite ideas for primary keys, uniqueness, defaults, and account table types. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 018, Create the Students table, using the acceptance checks I paste below. Check field lengths, defaults, unique email, and that the DDL has a hash field only. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
