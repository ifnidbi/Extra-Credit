# 036 · Create view 10 for student selling summaries

**Estimate** 45 minutes · **Stage** Views  
**Prerequisites** #25

## In brief

Count activity for each student, even someone who has listed nothing.

## Technical steps

1. Write `sql/views/10_student_selling_summary.sql` for `v_student_selling_summary`. LEFT JOIN Students to Listings and count total, Available, and Sold with conditional aggregation.
2. Inspect a zero-listing student, a mixed-status seller, and the total listing counts across all students.

## In first-time-coder language

1. Start with every student. Count how many things they listed, how many are still for sale, and how many are sold.
2. Check that someone who never listed anything gets three zeroes.

## Check your work

- [ ] Zero-activity students appear with 0/0/0.
- [ ] Matched status totals match source rows and total listings across students equals the listing table count.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL aggregate functions and group behavior](https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html)
- [MySQL CASE and flow-control functions](https://dev.mysql.com/doc/refman/8.4/en/flow-control-functions.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 036, Create view 10 for student selling summaries. Teach me the prerequisite ideas for left joins, CASE, SUM, and conditional counts. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 036, Create view 10 for student selling summaries, using the acceptance checks I paste below. Check conditional aggregation and whether the left-join placeholder creates a phantom listing. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
