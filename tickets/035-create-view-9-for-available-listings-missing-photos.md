# 035 · Create view 9 for available listings missing photos

**Estimate** 30 minutes · **Stage** Views  
**Prerequisites** #26

## In brief

Find which currently available items have no linked image rows.

## Technical steps

1. Write `sql/views/09_available_without_images.sql` and `v_available_without_images`. Use a correlated NOT EXISTS on Listing_Images and filter Available listings.
2. Compare one Available item with images, one without, and one hidden by status.

## In first-time-coder language

1. Look at every available item. Ask whether the photo table has any row with its item number. Show the item if the answer is no.
2. Try an item with a photo and a removed item and make sure they stay out.

## Check your work

- [ ] An Available no-image listing appears.
- [ ] Available with photo and other statuses are excluded. Photo row existence is the condition being measured.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL EXISTS and NOT EXISTS examples](https://dev.mysql.com/doc/refman/8.4/en/exists-and-not-exists-subqueries.html)
- [MySQL correlated subquery examples](https://dev.mysql.com/doc/refman/8.4/en/correlated-subqueries.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 035, Create view 9 for available listings missing photos. Teach me the prerequisite ideas for NOT EXISTS, correlated conditions, and edge cases. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 035, Create view 9 for available listings missing photos, using the acceptance checks I paste below. Check that my subquery checks images for the specific listing rather than the whole photo table. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
