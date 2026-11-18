# 034 · Create view 8 for pending pickup requests

**Estimate** 45 minutes · **Stage** Views  
**Prerequisites** #26

## In brief

Give admins a useful list of inquiries waiting for a response.

## Technical steps

1. Create `sql/views/08_pending_inquiries.sql` and `v_pending_inquiries`. Join Purchase_Inquiries through Listings to separate buyer and seller references to Students. Include title, names, location, date and inquiry ID.
2. Limit it to Pending and compare a Pending example and another status.

## In first-time-coder language

1. For each request still waiting, show the item's title, who's buying, who's selling, and the requested place and day.
2. Check you looked up buyer and seller separately, and that a declined request stays off the waiting list.

## Check your work

- [ ] Only Pending rows appear, with the correct buyer and seller names.
- [ ] The date and pickup place match the seed row.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL supported joins and syntax](https://dev.mysql.com/doc/refman/8.4/en/join.html)
- [Harvard CS50 SQL relating lecture, video and notes](https://cs50.harvard.edu/sql/weeks/1/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 034, Create view 8 for pending pickup requests. Teach me the prerequisite ideas for aliasing the same table twice, joins, and conditions. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 034, Create view 8 for pending pickup requests, using the acceptance checks I paste below. Check the buyer and seller joins separately so a result cannot swap the names. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
