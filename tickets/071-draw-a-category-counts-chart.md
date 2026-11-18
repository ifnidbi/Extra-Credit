# 071 · Draw a category counts chart

**Estimate** 45 minutes · **Stage** Reports  
**Prerequisites** #42, #69

## In brief

Turn MySQL category totals into a bar chart.

## Technical steps

1. Implement `get_category_counts()` and admin JSON `/api/reports/category-counts`. Aggregate listing counts across currency groups from view 7 without losing empty categories.
2. Use Chart.js in `static/reports_chart.js` to draw bars on the catalog reports page. Use accessible text/table and constructive feedback for empty or failed data. Record the Chart.js version or asset origin.

## In first-time-coder language

1. Add up the number of listings in each category. Ask the server for those totals and turn them into a picture with bars.
2. Check that a zero category is still listed. Keep the report table available to anyone who cannot use the chart.

## Check your work

- [ ] Labels and bar heights match hand-checked MySQL counts, including zero and split currency groups.
- [ ] A failed chart request leaves the report tables readable and shows a visible message.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Chart.js step-by-step chart walkthrough](https://www.chartjs.org/docs/latest/getting-started/usage.html)
- [Chart.js bar chart reference and options](https://www.chartjs.org/docs/latest/charts/bar.html)
- [MDN Using Fetch with examples](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [ExtraCredit database and view contracts](../docs/database.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 071, Draw a category counts chart. Teach me the prerequisite ideas for aggregating counts, chart labels, and data visualization. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 071, Draw a category counts chart, using the acceptance checks I paste below. Check the totals match the view, especially categories with multiple currency rows or none. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
