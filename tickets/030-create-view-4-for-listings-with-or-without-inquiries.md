# 030 · Create view 4 for listings with or without inquiries

**Estimate** 60 minutes · **Stage** Views  
**Prerequisites** #26

## In brief

Rebuild the submitted MySQL full outer join equivalent.

## Technical steps

1. In `sql/views/04_listing_inquiry_overview.sql`, use LEFT JOIN plus an unmatched-only RIGHT JOIN and UNION ALL for `v_listing_inquiry_overview`. Preserve the submitted output columns.
2. Compare the result to a scratch fixture with matches and gaps on both sides. Record the real FK behavior and the unresolved TA approval in query notes.

## In first-time-coder language

1. Start by keeping every listing even when nobody asked for it. Then add requests that have no matching listing, if the practice tables allow one.
2. Check that matched pairs are shown once. Write down why the second part has no extra rows in the real tables.

## Check your work

- [ ] A real unrequested listing appears with NULL inquiry values and matched rows are not duplicated.
- [ ] The independent scratch case demonstrates unmatched rows from both sides, and TA status is documented as pending.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL supported joins and syntax](https://dev.mysql.com/doc/refman/8.4/en/join.html)
- [MySQL UNION and UNION ALL](https://dev.mysql.com/doc/refman/8.4/en/union.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 030, Create view 4 for listings with or without inquiries. Teach me the prerequisite ideas for outer joins, UNION ALL, null matches, and foreign-key effects. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 030, Create view 4 for listings with or without inquiries, using the acceptance checks I paste below. Check the anti-match predicate prevents duplicates and that both sides of the equivalent are shown by scratch evidence. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
