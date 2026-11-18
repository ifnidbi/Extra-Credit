# 069 · Show five catalog views in HTML tables

**Estimate** 45 minutes · **Stage** Reports  
**Prerequisites** #12, #68

## In brief

Create the first admin reporting page.

## Technical steps

1. Add admin GET `/reports/catalog` and `reports/catalog.html`. Build a reusable Jinja table partial with captions, column headers, and an empty state. Display keys for views 1, 3, 6, 7, and 9 via `get_report`.
2. Format NULL, date and money visibly with currency codes from the shared report contract.

## In first-time-coder language

1. Make one page for shop-related reports. Give each saved database answer its own table with headings and readable rows.
2. Keep the headings visible even when a report has nothing to show. Put the currency next to every price.

## Check your work

- [ ] Five correctly labeled tables match their respective SQL results and include readable empty data.
- [ ] Ordinary users cannot load the page, and text is escaped.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MDN HTML table basics and examples](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics)
- [Jinja inheritance, loops, and escaping](https://jinja.palletsprojects.com/en/stable/templates/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 069, Show five catalog views in HTML tables. Teach me the prerequisite ideas for HTML table semantics, template loops, and escaping data. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 069, Show five catalog views in HTML tables, using the acceptance checks I paste below. Check I rendered the five correct reports, correct columns, and a useful empty state. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
