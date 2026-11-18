# 061 · Add photo upload and removal controls

**Estimate** 45 minutes · **Stage** Photos  
**Prerequisites** #42, #56, #60

## In brief

Let a seller manage the gallery from the listing edit page.

## Technical steps

1. In `catalog/edit.html` and `static/listing_photos.js`, add a labeled file chooser, upload action using FormData, and remove buttons on accessible image rows. Show upload controls only for a saved listing with allowed ownership and state.
2. Update the gallery or reload the media section after a confirmed API response. Include useful format, count and size feedback.

## In first-time-coder language

1. Give a seller a box for picking a photo and a button to send it. When a photo is saved, put it in the gallery with a remove button.
2. Tell the seller what kinds of file work. If the server says no, explain why and keep the current photos visible.

## Check your work

- [ ] An owner can add and remove an image without navigating away.
- [ ] A bad file or cap error displays a message and the visible gallery still matches saved rows.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [MDN sending files and fields with FormData](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest_API/Using_FormData_Objects)
- [MDN form validation guide with runnable examples](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
- [MDN Using Fetch with examples](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [Flask file uploads and safe serving](https://flask.palletsprojects.com/en/stable/patterns/fileuploads/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 061, Add photo upload and removal controls. Teach me the prerequisite ideas for file chooser events, FormData, and asynchronous image controls. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 061, Add photo upload and removal controls, using the acceptance checks I paste below. Check file field names, response-based updates, errors, and earlier controls for unsaved listings. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
