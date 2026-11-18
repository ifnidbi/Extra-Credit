# 049 · Build the catalog and listing detail pages

**Estimate** 60 minutes · **Stage** Listings  
**Prerequisites** #12, #37, #44, #47

## In brief

Give visitors usable pages even on the first server-rendered load.

## Technical steps

1. In `routes/catalog.py`, render `/listings` and `/listings/<listing_id>` from shared feature functions. Add `catalog/index.html` and `catalog/detail.html` with query controls, category names, price and currency, placeholder photos and pagination links.
2. Redirect root from the site blueprint. Preserve initial filter selections, use visible form labels, and include an empty state.

## In first-time-coder language

1. Make a page of items and a separate page for one item. Show the name, complete price, campus, and condition.
2. Give the shopper labeled search boxes and a next-page link. Show a friendly empty message if nothing matches.

## Check your work

- [ ] The home page reaches the listings, search works via normal form navigation, and a visible detail link opens.
- [ ] Missing or hidden listing details return 404 and empty search shows useful feedback.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [Flask tutorial on writing templates](https://flask.palletsprojects.com/en/stable/tutorial/templates/)
- [MDN illustrated guide to your first HTML form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Your_first_form)
- [MDN CSS first steps](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 049, Build the catalog and listing detail pages. Teach me the prerequisite ideas for server rendering, reusable templates, query forms, and links. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 049, Build the catalog and listing detail pages, using the acceptance checks I paste below. Check path handling, accessible controls, privacy and empty/pagination cases. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
