# 026 · Seed photos and purchase inquiries

**Estimate** 45 minutes · **Stage** Database  
**Prerequisites** #21, #22, #25

## In brief

Prepare the relationship examples used by the ten views.

## Technical steps

1. Write `sql/seed/03_images_and_inquiries.sql` with six or more rows per table and valid stable listing/buyer IDs. Include multiple inquiries on a listing, a listing with none, and available items both with and without photo rows.
2. Use historical inquiry dates on historical rows, all inquiry statuses, and no self-inquiries. Capture counts for the five core tables and note which fixtures are intentionally placeholders.

## In first-time-coder language

1. Add pretend photo labels and buyer requests that connect to the items you already made. Give one item several requests and another none.
2. Leave one available item without a photo, include several request stages, and count the rows in each core table.

## Check your work

- [ ] All five original tables contain six or more rows.
- [ ] Fixture relationships cover matched/unmatched listing rows, photo existence, and Pending versus other inquiry states.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MySQL INSERT statements and examples](https://dev.mysql.com/doc/refman/8.4/en/insert.html)
- [MySQL foreign key constraints and actions](https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 026, Seed photos and purchase inquiries. Teach me the prerequisite ideas for foreign-key fixtures, null matches, and meaningful test data. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 026, Seed photos and purchase inquiries, using the acceptance checks I paste below. Check fixture references, count coverage, and whether the data actually catches common view mistakes. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
