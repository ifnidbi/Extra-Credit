# 072 · Download a report as CSV

**Estimate** 45 minutes · **Stage** Reports  
**Prerequisites** #70

## In brief

Export the same data shown in a report table.

## Technical steps

1. Implement `render_csv(report)` in `exports.py` with Python's CSV writer, UTF-8, ordered headers and stable rows. Neutralize spreadsheet formula-like text safely and preserve searchable punctuation and numbers.
2. Add the admin CSV export route and download links. Use predictable names and content type. Keep empty exports valid with headers.

## In first-time-coder language

1. Give admins a Download CSV link that packs the same table into a file for spreadsheets. Keep each column separate even when a name has a comma or quote.
2. Save text so a spreadsheet treats a field as text when it could look like a calculation.

## Check your work

- [ ] Downloaded CSV retains headers, row order, commas, and money strings. An empty report exports headers.
- [ ] Formula-looking text stays inert, and non-admins cannot download the data.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Python CSV writer and quoting](https://docs.python.org/3/library/csv.html)
- [Harvard CS50 Python file I/O and CSV lecture materials](https://cs50.harvard.edu/python/weeks/6/)
- [OWASP guidance on spreadsheet formula interpretation](https://owasp.org/www-community/attacks/CSV_Injection)
- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 072, Download a report as CSV. Teach me the prerequisite ideas for CSV quoting, export headers, and spreadsheet-safe text. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 072, Download a report as CSV, using the acceptance checks I paste below. Check the report and CSV agree, filename/type are correct, and untrusted text is treated as text. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
