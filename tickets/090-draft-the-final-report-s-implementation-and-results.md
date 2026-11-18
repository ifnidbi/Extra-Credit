# 090 · Draft the final report's implementation and results

**Estimate** 60 minutes · **Stage** Delivery  
**Prerequisites** #83, #84, #86, #88

## In brief

Explain the implemented behavior and the evidence behind it.

## Technical steps

1. Write methodology/implementation, results and analysis using the query screenshots, sample rows, CRUD, login roles, chart, exports, weather queries and performance notes. Include actual observations, bugs found and fixed, one limitation, and evidence labels.
2. Describe the relevant transaction and permission choices in words and use diagrams/screenshots as needed.

## In first-time-coder language

1. Walk a reader through one real app action and show how the database changes. Include examples from the views, chart, downloads and weather feature.
2. Show what actually happened in tests, timings, and bug fixes. Use numbers and screenshots that readers can trace.

## Check your work

- [ ] The draft ties claims to screenshots and measured results, and it includes query coverage and actual error or edge cases.
- [ ] Claims about performance, enrollment and usability match observed or documented behavior.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [SOFE 3700U coverage and evidence checklist](../docs/course-coverage.md)
- [Purdue OWL guidance for revising drafts](https://owl.purdue.edu/owl/general_writing/the_writing_process/proofreading/steps_for_revising.html)
- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL EXPLAIN output and usage](https://dev.mysql.com/doc/refman/8.4/en/explain.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 090, Draft the final report's implementation and results. Teach me the prerequisite ideas for evidence-based technical writing, results, and explaining implementation. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 090, Draft the final report's implementation and results, using the acceptance checks I paste below. Check for unsupported claims, missing screenshots, and whether each result has enough context to reproduce. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
