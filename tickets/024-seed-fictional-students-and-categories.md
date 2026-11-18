# 024 · Seed fictional students and categories

**Estimate** 45 minutes · **Stage** Database  
**Prerequisites** #18, #19

## In brief

Give teammates consistent accounts and category names to test with.

## Technical steps

1. Write `sql/seed/01_accounts_and_categories.sql` with six or more fictional students and six or more categories. Include a demo admin, an inactive ordinary student, a student with no activity, and a deliberately unused category.
2. Use example-domain email addresses and safe test hashes or placeholders. Coordinate stable IDs and record how a teammate can provision login-ready demo accounts locally.

## In first-time-coder language

1. Add made-up people and category labels so everybody can practice on the same sample database. Include a demo administrator and a person with no listings or inquiries.
2. Use fake addresses and leave real passwords on your own computer. Write down which numbered rows other fixtures should use.

## Check your work

- [ ] Student and category counts are at least six and initial IDs are documented.
- [ ] No personal email or real credential appears in the seed, and the admin is intentionally designated.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL INSERT statements and examples](https://dev.mysql.com/doc/refman/8.4/en/insert.html)
- [Harvard CS50 SQL writing and transaction lecture](https://cs50.harvard.edu/sql/weeks/3/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 024, Seed fictional students and categories. Teach me the prerequisite ideas for INSERT, fixtures, stable test IDs, and password hashes. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 024, Seed fictional students and categories, using the acceptance checks I paste below. Check the sample variety and downstream fixture IDs, and review the draft for real credentials or personal data. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
