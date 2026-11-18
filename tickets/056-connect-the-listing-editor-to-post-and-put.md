# 056 · Connect the listing editor to POST and PUT

**Estimate** 60 minutes · **Stage** Listings  
**Prerequisites** #42, #44, #52, #55

## In brief

Let students create or edit an item through a shared form.

## Technical steps

1. Add `/listings/new` and owner-only `/listings/<listing_id>/edit` in `routes/catalog.py`. Factor shared fields into `catalog/edit.html`. Prefill existing data on edit and populate categories from the service.
2. Use `static/listing_editor.js` to send POST or PUT through `requestJson`, show inline field errors, and send the student to the resulting detail page.

## In first-time-coder language

1. Make one form that can start with a blank item or an item the seller already made. Fill in the category list and show mistakes next to the boxes.
2. Save to the correct address. After success, take the seller to the item's page.

## Check your work

- [ ] The normal new/edit flow writes the intended listing and displays the correct currency.
- [ ] Invalid input is shown on the matching field, and another student cannot open the editor.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [MDN form validation guide with runnable examples](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
- [MDN Using Fetch with examples](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [Flask tutorial on writing templates](https://flask.palletsprojects.com/en/stable/tutorial/templates/)
- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 056, Connect the listing editor to POST and PUT. Teach me the prerequisite ideas for reusable forms, form submission, and server field errors. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 056, Connect the listing editor to POST and PUT, using the acceptance checks I paste below. Check create versus edit methods, prefilled fields, server errors, and prevention of unauthorized editing. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
