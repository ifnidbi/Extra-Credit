# 022 · Create the Purchase Inquiries table

**Estimate** 45 minutes · **Stage** Database  
**Prerequisites** #20, #18

## In brief

Store a buyer's pickup request and its progress.

## Technical steps

1. Write `sql/05_purchase_inquiries.sql` with listing and buyer FKs, pickup text, payment preference, preferred date, status, and submission timestamp. Apply the types and constraints in the database contract.
2. Check that a valid insert uses Pending and that dangling references fail.

## In first-time-coder language

1. Make a table for messages that say who wants an item, where to meet, how they plan to pay, and on which day.
2. Check that a new request starts at Pending automatically. Try linking it to a student or item number that does not exist.

## Check your work

- [ ] One valid row records an ISO date and starts Pending with a timestamp.
- [ ] A nonexistent buyer or listing is rejected, and a parent with dependent inquiries is protected from physical deletion.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL foreign key constraints and actions](https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html)
- [MySQL date and time data types](https://dev.mysql.com/doc/refman/8.4/en/date-and-time-types.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 022, Create the Purchase Inquiries table. Teach me the prerequisite ideas for two foreign keys, DATE versus DATETIME, and default status. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 022, Create the Purchase Inquiries table, using the acceptance checks I paste below. Check parent relations, date types, status values, and restrictive delete behavior. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
