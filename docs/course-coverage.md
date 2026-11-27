# Course coverage

Use the course handout as the submission authority. The table maps its requirements to team work and evidence. The original PDFs belong in the team's private course files.

The progress audit found one implementation PR, [foundation #95](https://github.com/ifnidbi/Extra-Credit/pull/95), which added the Flask app factory and the health route. The app builds on that work. The [query and demo evidence](query-evidence.md) records the tested implementation. The [report checklist](report-checklist.md) covers the remaining course submission work.

| Course requirement | Work and evidence |
| --- | --- |
| Rebuild relational schema, sample data and ER diagram | Schema files, FK checks, six or more fictional records in each original table, updated relationship diagram, reproducible seed steps. |
| Ten Phase II views | Preserve each requested query pattern and show results on two report pages. Record the MySQL full outer join equivalent and any TA feedback. |
| Authentication, sessions, roles, input and errors | Demo guest, student and admin access. Show visible and refused actions, field messages, and stable responses during dependency failures. |
| Web service, JSON, CRUD, external REST API | Show local GET, POST, PUT and DELETE on records, an external pickup-weather fetch and save, and both snapshot INSERT and SELECT. |
| Frontend, forms, AJAX, charts, search | Browse listings and show multiple pages. Perform a filtered search and a form action without reloading, show the chart backed by MySQL, and render all ten views as labeled HTML tables. |
| CSV and PDF | Download, open, and check both formats for the same report data. |
| Installation and performance | Verified setup and application tests on macOS with MySQL 8.4.11. The README includes Windows and Linux commands. See the recorded EXPLAIN plans, local timings, and limitations. |
| Final report | Use the checklist and evidence to write 10–12 pages in Times 11. Add the contribution matrix and references. |
| Presentation, demo and evaluation | Team prepares PowerPoint slides for a 5–7 minute presentation, followed by two minutes for questions. Rehearse the demo and defend schema and implementation decisions. Complete the team evaluation through the course process. |
