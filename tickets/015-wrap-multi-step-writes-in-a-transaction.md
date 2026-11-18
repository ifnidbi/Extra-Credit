# 015 · Wrap multi-step writes in a transaction

**Estimate** 45 minutes · **Stage** Foundation  
**Prerequisites** #14

## In brief

Give feature code a shared commit-and-rollback boundary.

## Technical steps

1. Add `transaction()` to `extracredit/db.py`. Yield the existing request's connection to writers, commit only after success, and roll back if work or commit raises. Keep cursor lifetime with the caller.
2. Exercise it with harmless writes in a temporary table. Document that repositories use the passed connection and do not commit independently.

## In first-time-coder language

1. Make a wrapper that treats a group of database changes like one action. If anything fails, the group goes back to how it started.
2. Try two pretend writes and fail the second on purpose. Check that the first one did not stick.

## Check your work

- [ ] A successful two-step action persists both rows.
- [ ] A failing two-step action persists neither, and the original exception remains visible to the caller.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Connector/Python transaction commit reference](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html)
- [MySQL commit and rollback reference](https://dev.mysql.com/doc/refman/8.4/en/commit.html)
- [Python context managers and contextlib](https://docs.python.org/3/library/contextlib.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 015, Wrap multi-step writes in a transaction. Teach me the prerequisite ideas for transactions, commit, rollback, and context managers. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 015, Wrap multi-step writes in a transaction, using the acceptance checks I paste below. Check that caller work and failed commits roll back, and look for accidentally nested commits. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
