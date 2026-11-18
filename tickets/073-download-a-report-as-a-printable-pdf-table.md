# 073 · Download a report as a printable PDF table

**Estimate** 60 minutes · **Stage** Reports  
**Prerequisites** #72

## In brief

Make a printable version with clear titles and repeated headers.

## Technical steps

1. Add ReportLab and implement `render_pdf(report)` using a titled, paginated table. Wrap long cells, repeat headers, and safely escape display strings when using markup-aware elements. Verify the chosen fonts cover demo text and document font coverage limits.
2. Add the admin PDF route and download links to both report pages. Set attachment name and PDF content type.

## In first-time-coder language

1. Give admins a printable report with a heading and the same rows as on screen. Keep long text inside each cell and repeat the headings when the report spills to another page.
2. Try a report with a long cell, one with several pages and one empty report.

## Check your work

- [ ] A PDF opens with correct title, columns, safe cell text, and legible multi-page output.
- [ ] An empty report gives a useful printable state, and non-admin download attempts are rejected.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ReportLab document generation guide](https://docs.reportlab.com/reportlab/userguide/ch5_platypus/)
- [ReportLab table and pagination guide](https://docs.reportlab.com/reportlab/userguide/ch7_tables/)
- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 073, Download a report as a printable PDF table. Teach me the prerequisite ideas for in-memory documents, table pagination, and safe presentation. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 073, Download a report as a printable PDF table, using the acceptance checks I paste below. Check the output, multi-page headers, long text, font coverage, and access checks. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
