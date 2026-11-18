# 059 · Serve listing photos in a gallery

**Estimate** 45 minutes · **Stage** Photos  
**Prerequisites** #49, #58

## In brief

Show stored images when the viewer can see the associated item.

## Technical steps

1. Add `find_images`, `find_image`, and `list_listing_images`. Implement media GET in `routes/photo_api.py` using `get_listing` visibility, the image/listing relationship, and safe file serving from `UPLOAD_DIR`.
2. Render photos on the detail page with accessible alt text and a fallback for missing seed bytes. Keep file paths out of responses.

## In first-time-coder language

1. Look up the item's photos and put them on its page. Use the picture's number to ask the app for it, so people get the photos that go with the right item.
2. If there is no file, show a placeholder. Apply the same visitor rules to the photo as to the listing.

## Check your work

- [ ] Existing photo bytes display on a visible listing. Missing bytes use a placeholder or safe 404.
- [ ] An image belonging to another listing or a hidden listing cannot be fetched through the wrong URL.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Flask file uploads and safe serving](https://flask.palletsprojects.com/en/stable/patterns/fileuploads/)
- [Flask tutorial on writing templates](https://flask.palletsprojects.com/en/stable/tutorial/templates/)
- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 059, Serve listing photos in a gallery. Teach me the prerequisite ideas for media routes, file serving, scoped lookups, and image alt text. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 059, Serve listing photos in a gallery, using the acceptance checks I paste below. Check listing visibility, exact image linkage, and placeholder and 404 handling. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
