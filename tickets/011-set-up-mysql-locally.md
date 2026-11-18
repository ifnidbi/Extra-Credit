# 011 · Set up MySQL locally

**Estimate** 45 minutes · **Stage** Foundation  
**Prerequisites** None. Start any time.

## In brief

Get a fresh local MySQL server ready to use from the terminal.

## Technical steps

1. Install or start a MySQL 8.4 LTS instance using the official instructions for your system. Verify the version and connect locally with MySQL Shell, the mysql client, or Workbench.
2. Record the connection method and local service start/stop steps in `docs/mysql-local.md`. Leave real credentials in local config.

## In first-time-coder language

1. Start your own database on your computer, then open a tool that lets you talk to it.
2. Ask the database which version it is. Write down how a teammate can start it and connect on the same operating system.

## Check your work

- [ ] The server reports the 8.4 series and runs a harmless SELECT over a local connection.
- [ ] The instructions disclose zero real passwords, tokens, or host addresses.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [MySQL 8.4 official installation guide](https://dev.mysql.com/doc/refman/8.4/en/installing.html)
- [MySQL command-line client documentation](https://dev.mysql.com/doc/refman/8.4/en/mysql.html)
- [Harvard CS50 SQL designing lecture and examples](https://cs50.harvard.edu/sql/weeks/2/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 011, Set up MySQL locally. Teach me the prerequisite ideas for database server, client, port, and local connection. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 011, Set up MySQL locally, using the acceptance checks I paste below. Review my install notes and proof that I connected to a local MySQL in the target version. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
