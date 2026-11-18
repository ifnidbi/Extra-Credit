# 070 · Show five activity views in HTML tables

**Estimate** 45 minutes · **Stage** Reports  
**Prerequisites** #69

## In brief

Complete the course requirement to display all ten views on pages.

## Technical steps

1. Add admin GET `/reports/activity` and `reports/activity.html` reusing the existing table partial. Display view keys for 2, 4, 5, 8, and 10 from `get_report`.
2. Add admin navigation between report pages. Check NULL inquiry fields and explicit zeroes from the selling summary.

## In first-time-coder language

1. Make a second report page for activity. Reuse the same table pattern and add links so an admin can move between the two pages.
2. Check an item with no request and a student with zero sales so those two different situations are readable.

## Check your work

- [ ] Together both pages render all ten unique views with no missing or repeated assignment.
- [ ] Activity preserves zero values and NULL has clear display. Student and guest access is refused.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit database and view contracts](../docs/database.md)
- [MDN HTML table basics and examples](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics)
- [Jinja inheritance, loops, and escaping](https://jinja.palletsprojects.com/en/stable/templates/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 070, Show five activity views in HTML tables. Teach me the prerequisite ideas for template reuse, report navigation, and distinguishing zero from missing data. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 070, Show five activity views in HTML tables, using the acceptance checks I paste below. Check that all ten views now have one table each and private activities are restricted. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
