# 083 · Test report tables and both downloads

**Estimate** 60 minutes · **Stage** Verification  
**Prerequisites** #71, #73, #78

## In brief

Check the ten admin views and CSV/PDF match their SQL source.

## Technical steps

1. Create `tests/test_reports.py` for all ten report keys, both page table sets, unknown key, chart counts, CSV and PDF. Compare a few fixture results directly to expected rows and query results. Assert guest/user refusals and stable attachment headers.
2. Include empty report export, CSV punctuation and spreadsheet text, and a long/multipage PDF. Open a PDF manually to confirm repeated headers and readability.

## In first-time-coder language

1. Have the checker visit both admin report pages, make sure ten tables are represented, and compare some rows with the database.
2. Try downloading both file types, including as a normal student. Open a long PDF and see whether the next page still makes sense.

## Check your work

- [ ] API, table routes and exports agree with fixture records. Chart counts handle multiple currencies and a zero category.
- [ ] Private views and files are refused for non-admins, and an opened PDF passes the manual check.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)
- [MDN HTML table basics and examples](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_table_basics)
- [Python CSV writer and quoting](https://docs.python.org/3/library/csv.html)
- [ReportLab table and pagination guide](https://docs.reportlab.com/reportlab/userguide/ch7_tables/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 083, Test report tables and both downloads. Teach me the prerequisite ideas for asserting tabular content, exports, access checks, and combined automated/manual verification. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 083, Test report tables and both downloads, using the acceptance checks I paste below. Check SQL spot comparisons, the ten keys, both table pages, and both export types, and proof that exports are valid and access-scoped. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
