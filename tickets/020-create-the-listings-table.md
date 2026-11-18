# 020 · Create the Listings table

**Estimate** 60 minutes · **Stage** Database  
**Prerequisites** #18, #19

## In brief

Store what is for sale, who owns it, and where it can be picked up.

## Technical steps

1. Write `sql/03_listings.sql` with the fields, status and condition values, defaults, amount checks, and currency rules in the database contract.
2. Add seller and category FKs with delete restrictions. In a scratch test insert a valid row, a dangling reference, a negative amount, and a fractional JPY amount.

## In first-time-coder language

1. Make a table for listings. Give each item a name, campus, price and currency, plus the numbers for its seller and category.
2. Ask the database to refuse a made-up seller, a price below zero, and a fraction of a yen.

## Check your work

- [ ] A valid row receives Available and a posting timestamp.
- [ ] The test shows the database refusing invalid references, amounts, and currencies.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL foreign key constraints and actions](https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html)
- [MySQL CHECK constraints and examples](https://dev.mysql.com/doc/refman/8.4/en/create-table-check-constraints.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 020, Create the Listings table. Teach me the prerequisite ideas for foreign keys, DECIMAL, enum values, and check constraints. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 020, Create the Listings table, using the acceptance checks I paste below. Check all foreign keys match parent types and the amount, currency, condition and state rules agree with the contract. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
