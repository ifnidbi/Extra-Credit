# 031 · Create view 5 for students with activity

**Estimate** 45 minutes · **Stage** Views  
**Prerequisites** #26

## In brief

Use a nested UNION to find students who sold or asked to buy.

## Technical steps

1. Create `sql/views/05_active_students.sql` and `v_active_students` using a nested UNION of seller and buyer IDs.
2. Using the fixture, compare a seller-only, buyer-only, both, and inactive-in-marketplace example. Keep email in this admin-only view.

## In first-time-coder language

1. Make one list of people who posted, another of people who sent a request, and combine the lists so each person counts once.
2. Find a person who did nothing and check they stay off this list, whether or not they can log in.

## Check your work

- [ ] A student appearing in both sources appears once.
- [ ] No-activity accounts are absent, and the view represents activity history instead of login state.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL UNION and UNION ALL](https://dev.mysql.com/doc/refman/8.4/en/union.html)
- [MySQL subquery reference](https://dev.mysql.com/doc/refman/8.4/en/subqueries.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 031, Create view 5 for students with activity. Teach me the prerequisite ideas for nested set operations, identity, and duplication. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 031, Create view 5 for students with activity, using the acceptance checks I paste below. Check that nesting and UNION give the four expected kinds of result and avoid exposing the report publicly. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
