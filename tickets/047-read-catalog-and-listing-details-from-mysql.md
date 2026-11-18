# 047 · Read catalog and listing details from MySQL

**Estimate** 60 minutes · **Stage** Listings  
**Prerequisites** #14, #25, #46

## In brief

Keep browse queries focused on public data and stable pages.

## Technical steps

1. Implement `find_listings`, `find_listing`, and `find_seller_listings` in `listing_repo.py`. Bind every filter value and escape LIKE wildcards when filters mean literal text. Return at most 50 listings per page, with stable order and a way to detect a next page.
2. Join seller active state and category. In `listings.py`, add `search_listings`, `get_listing`, and `list_seller_listings`. Enforce detail visibility and use explicit public fields.

## In first-time-coder language

1. Ask the database for items matching what the shopper typed. Keep fifty per page in a reliable order and check if there is another page.
2. Show only public information about people and items. Let the seller see their own list of items even when a guest cannot.

## Check your work

- [ ] Filters combine correctly and pages do not arbitrarily reorder tied rows.
- [ ] Guest detail hides Removed items and inactive sellers, and neither browse nor detail exposes email or password data.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [MySQL SELECT reference including filters and ordering](https://dev.mysql.com/doc/refman/8.4/en/select.html)
- [Connector/Python parameter binding with cursor execute](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html)
- [MySQL supported joins and syntax](https://dev.mysql.com/doc/refman/8.4/en/join.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 047, Read catalog and listing details from MySQL. Teach me the prerequisite ideas for parameterized search, joins, deterministic pages, and public projections. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 047, Read catalog and listing details from MySQL, using the acceptance checks I paste below. Check bound values, literal LIKE matches, stable ordering, visibility and output fields. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
