# 007 · Update the marketplace relationship diagram

**Estimate** 45 minutes · **Stage** Practice  
**Prerequisites** None. Start any time.

## In brief

Draw how the six planned tables connect for the revised project.

## Technical steps

1. Read the database contract. In `docs/er-diagram.md` draw Students, Categories, Listings, Listing_Images, Purchase_Inquiries, and Pickup_Forecasts with primary keys, foreign keys, and cardinalities.
2. Label the seller and buyer relationships separately and identify optional photo, inquiry, and forecast relationships.

## In first-time-coder language

1. Draw a box for each group of stored information. Connect the boxes where one record points at another.
2. Show that a student can sell several things, a different student can ask to buy them, and a listing can have zero or several photos.

## Check your work

- [ ] All six tables and all six foreign-key relationships appear with correct direction and cardinality.
- [ ] A teammate can trace how to find the seller for an inquiry and the student for a forecast.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [Harvard CS50 SQL relating lecture, video and notes](https://cs50.harvard.edu/sql/weeks/1/)
- [MySQL foreign key constraints and actions](https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 007, Update the marketplace relationship diagram. Teach me the prerequisite ideas for primary keys, foreign keys, and one-to-many relationships. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 007, Update the marketplace relationship diagram, using the acceptance checks I paste below. Check the six relationships and point out missing or misleading cardinalities. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
