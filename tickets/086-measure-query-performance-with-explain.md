# 086 · Measure query performance with EXPLAIN

**Estimate** 60 minutes · **Stage** Verification  
**Prerequisites** #54, #68, #76, #78

## In brief

Collect evidence for the course performance discussion.

## Technical steps

1. In `docs/performance.md`, measure a realistic filtered listing search and one report or forecast-history read. Save repeatable parameters, data size, a baseline EXPLAIN, and a small repeated timing sample.
2. Test one justified candidate index in the test database and compare the same query and result. If evidence warrants keeping it, add a numbered SQL index script and update setup notes.

## In first-time-coder language

1. Ask MySQL to describe how it finds the data before and after trying one index. Time the same question more than once with the same pretend dataset.
2. Keep the index only if you can explain what it helps, and write down anything the experiment cannot prove.

## Check your work

- [ ] Notes include data size, EXPLAIN changes, repeat timings, correctness comparison and tradeoffs.
- [ ] Any retained index has a reproducible installation step and clear evidence of purpose.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [MySQL EXPLAIN output and usage](https://dev.mysql.com/doc/refman/8.4/en/explain.html)
- [MySQL multiple-column index guide](https://dev.mysql.com/doc/refman/8.4/en/multiple-column-indexes.html)
- [Harvard CS50 SQL optimizing lecture and examples](https://cs50.harvard.edu/sql/weeks/5/)
- [ExtraCredit database and view contracts](../docs/database.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 086, Measure query performance with EXPLAIN. Teach me the prerequisite ideas for query plans, composite indexes, and fair before/after comparisons. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 086, Measure query performance with EXPLAIN, using the acceptance checks I paste below. Check that parameters/data match across trials and conclusions track observed plans and results. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
