# 048 · Expose listing reads as JSON

**Estimate** 45 minutes · **Stage** Listings  
**Prerequisites** #37, #44, #47

## In brief

Make listing search and details accessible to browser JavaScript.

## Technical steps

1. Add GET handlers in `routes/listing_api.py` for `/api/listings` and `/api/listings/<listing_id>`. Use `parse_filters`, `search_listings`, and `get_listing`. Register the blueprint.
2. Serialize catalog response as `items`, `page`, and `has_next`. Keep price strings and fields from the safe projection. Return 404 for hidden or unknown detail IDs.

## In first-time-coder language

1. Give the browser two addresses. One finds a group of items and the other answers with one item.
2. Return numbers and dates in the agreed format. If the visitor cannot see that item, give the same message as a missing item.

## Check your work

- [ ] GET returns expected JSON and query filters work at the HTTP boundary.
- [ ] An invalid filter returns 400, missing/hidden detail returns 404, and a guest response omits private fields.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [MDN overview of HTTP diagrams and examples](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)
- [Flask quickstart with minimal examples](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 048, Expose listing reads as JSON. Teach me the prerequisite ideas for REST GET, query parameters, typed JSON, and 404 behavior. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 048, Expose listing reads as JSON, using the acceptance checks I paste below. Check response shapes, preserved decimal precision, and the absence of contact data. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
