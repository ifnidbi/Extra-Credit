# 025 · Seed listings across campuses and currencies

**Estimate** 45 minutes · **Stage** Database  
**Prerequisites** #20, #24

## In brief

Create listing data that exercises search and price reports.

## Technical steps

1. Write `sql/seed/02_listings.sql` with at least six rows and valid stable seller/category references. Include all four statuses, repeated categories within a currency, a second currency, and multiple fictional campus names.
2. Choose price examples with hand-checkable higher-than-average results and record listing IDs for image and inquiry fixtures.

## In first-time-coder language

1. Fill the marketplace with made-up items from several campuses. Give them different prices, currencies, and sale stages.
2. Pick some prices so you can tell by hand which is above the average. Tell the teammate adding photos which item numbers to use.

## Check your work

- [ ] Rows exercise Available, Reserved, Sold, and Removed, and leave a category unused.
- [ ] At least one distinct price comparison can be hand-checked without mixing currencies.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL INSERT statements and examples](https://dev.mysql.com/doc/refman/8.4/en/insert.html)
- [MySQL aggregate functions and group behavior](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 025, Seed listings across campuses and currencies. Teach me the prerequisite ideas for seed data, references, and useful price examples. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 025, Seed listings across campuses and currencies, using the acceptance checks I paste below. Check that my chosen seed rows let reports distinguish currency and include every important listing state. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
