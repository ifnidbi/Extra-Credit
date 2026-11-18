# 010 · Keep secrets and settings local

**Estimate** 45 minutes · **Stage** Foundation  
**Prerequisites** #9

## In brief

Wire the settings the app and database will use.

## Technical steps

1. Create `extracredit/config.py` with `Config` and the settings named in the architecture. Load it from the factory and apply `test_config` overrides.
2. Write a placeholder-only `.env.example`. Ignore `.env`, `.venv`, caches, runtime uploads, and IDE files. Enforce size settings and make Secure configurable for dev versus HTTPS.
3. Document how to supply variables in the shell without sharing values.

## In first-time-coder language

1. Give the app a list of knobs such as where the database lives. Put made-up examples in the shared file and your own values on your computer.
2. Tell Git to skip private files. Check your personal settings can be supplied when the app starts.

## Check your work

- [ ] The example contains placeholders only, and Git reports actual local secret and upload paths as ignored.
- [ ] Tests can replace settings independently and an actual secret does not appear in any tracked file.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [Flask configuration settings](https://flask.palletsprojects.com/en/stable/config/)
- [Git reference for ignored files](https://git-scm.com/docs/gitignore)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 010, Keep secrets and settings local. Teach me the prerequisite ideas for environment variables, configuration overrides, and Git ignore rules. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 010, Keep secrets and settings local, using the acceptance checks I paste below. Check the placeholder file, ignore rules, and whether settings or credentials can leak into a public PR. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
