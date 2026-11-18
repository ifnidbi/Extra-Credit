# 014 · Connect Flask to MySQL per request

**Estimate** 60 minutes · **Stage** Foundation  
**Prerequisites** #10, #11, #13

## In brief

Give the backend a repeatable way to open and close DB connections.

## Technical steps

1. Install MySQL Connector/Python. Implement `get_db()` and `close_db(error=None)` in `extracredit/db.py`. Cache the connection in Flask `g` and register teardown.
2. Read only Config values, map unavailable DB connections to a stable 503, and demonstrate a bound-value read outside a real route using app context.

## In first-time-coder language

1. Make one phone line between Flask and the database for each request. Reuse it while that request is being answered and close it when done.
2. Try a tiny database question, then stop MySQL and see that the app gives a clear message when it needs the database.

## Check your work

- [ ] A DB-aware smoke check performs a trivial SELECT with MySQL running.
- [ ] Repeated calls in one context reuse the connection, teardown closes it, and health still works when the DB is down.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [MySQL Connector/Python developer guide and examples](https://dev.mysql.com/doc/connector-python/en/)
- [Connector/Python parameter binding with cursor execute](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html)
- [Flask app context and lifetime](https://flask.palletsprojects.com/en/stable/appcontext/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 014, Connect Flask to MySQL per request. Teach me the prerequisite ideas for Flask app context, connections, cursors, teardown, and bound parameters. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 014, Connect Flask to MySQL per request, using the acceptance checks I paste below. Check repeated calls and teardown, connection failure handling, and where settings enter the connector. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
