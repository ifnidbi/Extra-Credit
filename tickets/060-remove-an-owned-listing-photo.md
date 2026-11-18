# 060 · Remove an owned listing photo

**Estimate** 45 minutes · **Stage** Photos  
**Prerequisites** #59

## In brief

Allow the owner to detach an image without making the remaining gallery inconsistent.

## Technical steps

1. Implement `delete_image` and `remove_listing_image`, acquiring the listing lock and verifying ownership, editable state and image association. Commit the row deletion before unlinking the fixed-key file, tolerate missing bytes, and log cleanup failures.
2. Add the protected DELETE route returning 204. See that a missing ID returns 404 and a different owner cannot delete it.

## In first-time-coder language

1. Let a seller take down one of their own photos. Remove the link from the table, then clean up its saved file.
2. If the file was already missing, the link still needs to disappear. Try taking down a photo on somebody else's item and see that it stays there.

## Check your work

- [ ] A valid removal updates the gallery and removes existing file bytes or logs the failed cleanup.
- [ ] A mismatched listing/photo or non-owner request produces no change.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [MySQL DELETE syntax and conditions](https://dev.mysql.com/doc/refman/8.4/en/delete.html)
- [InnoDB locking SELECT examples](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-reads.html)
- [Flask file uploads and safe serving](https://flask.palletsprojects.com/en/stable/patterns/fileuploads/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 060, Remove an owned listing photo. Teach me the prerequisite ideas for database deletion, cleanup ordering, and resource ownership. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 060, Remove an owned listing photo, using the acceptance checks I paste below. Check owner and state permissions, row and file order, and result codes for absent or unrelated images. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
