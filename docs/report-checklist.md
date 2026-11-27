# Final report checklist

Prepare a 10–12 page report in Times 11. Use your actual screenshots, test outcomes, and contributions. The [course coverage table](course-coverage.md) maps the app to the handout.

| Section | What to include |
| --- | --- |
| Abstract | Summarize the student marketplace, the database design, and one measured or demonstrated result. |
| Introduction and goals | Explain the problem with finding and selling secondhand goods around campus, who ExtraCredit is for, and the project goals. |
| Related work | Compare the concept to the related projects in the proposal. Check your references before submitting. |
| Design and schematics | Include the [ER diagram](database.md#entity-relationship-diagram), six tables, keys, major constraints, schema changes since Phase II, and the Flask–MySQL request flow. Explain why prices are grouped by currency. |
| Implementation and course connection | Show registration, sessions and roles, listing CRUD, photo uploads, filters, buyer and seller inquiries, Fetch, Chart.js, both exports, and the Open-Meteo integration. Explain the transaction used to accept an inquiry and reserve the listing. |
| Results and analysis | Include one clearly labeled result screenshot for each of the ten views. Also show sample row counts, key CRUD outcomes, search, chart, exports, and the weather INSERT and SELECT. Add actual correctness checks and performance measurements. |
| Conclusions, problems, and future work | State what worked, a bug you reproduced and fixed, test limits, and what you would add next. Good future-work examples are student verification, a campus directory, and deployment. Explain View 4's MySQL equivalent and document any TA response you have. |
| References and contributions | Cite sources and libraries, include the contribution matrix, and describe the foundation PR and AI-assisted implementation accurately. Record each team member's actual work and follow your course's AI disclosure requirements. |

Use the [query and demo evidence](query-evidence.md) to locate captures and reproduce them. For the separate presentation, prepare 5–7 minutes of PowerPoint slides and practice two minutes of questions. The team evaluation uses the course's submission process.
