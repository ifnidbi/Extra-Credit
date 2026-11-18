# 087 · Write and verify a fresh-install README

**Estimate** 60 minutes · **Stage** Delivery  
**Prerequisites** #16, #61, #67, #73, #77, #78

## In brief

Make it possible for a new teammate or grader to run the finished project.

## Technical steps

1. Add installation steps to README for a clean Windows or Linux setup, plus macOS if verified. Include Python/venv, pinned dependencies, MySQL and schema/view order, seed and login-ready fictional demo account, settings, server startup, and tests.
2. Have a teammate follow the written steps in a fresh folder or machine. Add troubleshooting for DB connection, test isolation, upload folder and weather issues.

## In first-time-coder language

1. Pretend someone has just downloaded the project. Tell them everything to install, how to make the practice database and demo accounts, which command starts the website, and how to check it.
2. Ask someone else to follow the notes while you watch. Fix any steps they had to guess.

## Check your work

- [ ] A clean Windows or Linux run reaches catalog, login and reports using only the README, and the outcome is recorded.
- [ ] The instructions use placeholders and never expose real credentials or unsafe rebuild targets.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [SOFE 3700U coverage and evidence checklist](../docs/course-coverage.md)
- [Python virtual environments and pip](https://docs.python.org/3/tutorial/venv.html)
- [MySQL script files and batch mode](https://dev.mysql.com/doc/refman/8.4/en/mysql-batch-commands.html)
- [Flask quickstart with minimal examples](https://flask.palletsprojects.com/en/stable/quickstart/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 087, Write and verify a fresh-install README. Teach me the prerequisite ideas for reproducible setup, environment variables, and documenting tested commands. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 087, Write and verify a fresh-install README, using the acceptance checks I paste below. Check commands are in the right order, the fresh-run proof is specific, and private config stays private. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
