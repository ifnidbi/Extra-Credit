# 021 · Create the Listing Images table

**Estimate** 30 minutes · **Stage** Database  
**Prerequisites** #20

## In brief

Make room for multiple photos on an item.

## Technical steps

1. Write `sql/04_listing_images.sql` using `image_id`, `listing_id`, and unique `image_path`. Set the listing FK to cascade on delete.
2. Test two image rows against one scratch listing and observe deletion in an isolated test database.

## In first-time-coder language

1. Keep a separate little photo table so one item can have multiple photos. Store the photo key and the item's number together.
2. Use a pretend item to check its linked rows go away when it is physically deleted in the practice database.

## Check your work

- [ ] Two distinct photo keys fit on one listing.
- [ ] A duplicate key or missing listing fails, and physical deletion of a scratch listing cascades to its image rows.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL foreign key constraints and actions](https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html)
- [Harvard CS50 SQL relating lecture, video and notes](https://cs50.harvard.edu/sql/weeks/1/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 021, Create the Listing Images table. Teach me the prerequisite ideas for one-to-many photos, unique storage keys, and cascade deletes. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 021, Create the Listing Images table, using the acceptance checks I paste below. Check the foreign-key action, unique photo key, and the test target is disposable. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
