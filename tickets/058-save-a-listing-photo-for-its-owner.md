# 058 · Save a listing photo for its owner

**Estimate** 60 minutes · **Stage** Photos  
**Prerequisites** #21, #37, #51, #53, #57

## In brief

Attach a valid photo to the item the signed-in student owns.

## Technical steps

1. Add `insert_image` and ownership-scoped counting in `image_repo.py`. Implement `add_listing_image(actor, listing_id, upload)` using a generated random key, the listing lock, the five-photo cap, and editable status. Save bytes beneath `UPLOAD_DIR` and remove newly written bytes if the database work fails.
2. Wire multipart POST in `routes/photo_api.py` with field `photo`, CSRF and 201 response including the image ID and stable media URL.

## In first-time-coder language

1. When a seller picks a photo, check the item is really theirs and there is room for another. Give the saved file a new random name.
2. Store the file and a link to the item. If you fail to save the database row, clean up the file you just made.

## Check your work

- [ ] A valid upload creates both the image row and file and returns the expected URL.
- [ ] A non-owner, sixth photo, closed listing, or missing upload gets the expected response, and a forced DB error leaves no new file.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Flask file uploads and safe serving](https://flask.palletsprojects.com/en/stable/patterns/fileuploads/)
- [Python random identifiers with UUID](https://docs.python.org/3/library/uuid.html)
- [MySQL commit and rollback reference](https://dev.mysql.com/doc/refman/8.4/en/commit.html)
- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 058, Save a listing photo for its owner. Teach me the prerequisite ideas for multipart input, random storage keys, file cleanup, and ownership. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 058, Save a listing photo for its owner, using the acceptance checks I paste below. Check file and row consistency, generated keys, ownership, and enforcement of the count under the row lock. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
