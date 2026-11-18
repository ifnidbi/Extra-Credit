# 017 · Create a fresh development database

**Estimate** 30 minutes · **Stage** Database  
**Prerequisites** #11

## In brief

Set up a clean place to build the ExtraCredit schema.

## Technical steps

1. Write `sql/00_database.sql` to create and choose `extra_credit` with utf8mb4. Record how later scripts target a selected database and how to create a separate test database.
2. Keep schema scripts as the tool to create fresh tables. Keep any documented clean rebuild action explicit about the target database.

## In first-time-coder language

1. Make a new empty container called ExtraCredit for your development tables. Pick a text format that can hold names in different languages.
2. Write down how to make a second container for tests. Read the selected name before a rebuild.

## Check your work

- [ ] The script establishes `extra_credit` and reports utf8mb4.
- [ ] An independent `extra_credit_test` database can be selected without changing the development data.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL CREATE DATABASE syntax and permissions](https://dev.mysql.com/doc/refman/8.4/en/create-database.html)
- [MySQL utf8mb4 character set reference](https://dev.mysql.com/doc/refman/8.4/en/charset-unicode-utf8mb4.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 017, Create a fresh development database. Teach me the prerequisite ideas for databases, character sets, and selecting a schema. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 017, Create a fresh development database, using the acceptance checks I paste below. Check the database names, Unicode setting, and isolation of destructive rebuild steps. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
