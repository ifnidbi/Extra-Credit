# 076 · Store and retrieve pickup weather snapshots

**Estimate** 60 minutes · **Stage** Weather  
**Prerequisites** #15, #23, #37, #75

## In brief

Demonstrate two database queries tied to external REST data.

## Technical steps

1. Implement `insert_snapshot` and `find_recent_snapshots` in `weather_repo.py` with bound SQL. Implement `save_pickup_forecast(actor, data)` and `list_pickup_forecasts(actor)` in `weather.py`. Validate label and coordinates before making external requests and start the DB write after a usable forecast arrives.
2. Wire signed-in JSON GET places and GET/POST snapshots in `routes/weather_api.py`. Read ten latest snapshots ordered by fetched time and ID, restricted to the caller.

## In first-time-coder language

1. Save the weather you just looked up into that student's history. Give them another button that reads their ten latest lookups.
2. Check the city label and position before calling the weather service. Save nothing when the service fails.

## Check your work

- [ ] A POST makes the external request and inserts a valid parsed snapshot. GET reads it for its owner only.
- [ ] A failing API request or invalid location leaves snapshot counts unchanged. The two query shapes are clear to explain.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [Connector/Python parameter binding with cursor execute](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html)
- [MySQL INSERT statements and examples](https://dev.mysql.com/doc/refman/8.4/en/insert.html)
- [Open-Meteo interactive forecast documentation](https://open-meteo.com/en/docs)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 076, Store and retrieve pickup weather snapshots. Teach me the prerequisite ideas for INSERT then SELECT, scoped history, and separating network from DB writes. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 076, Store and retrieve pickup weather snapshots, using the acceptance checks I paste below. Check ownership, validation order, transaction scope, stable sort, and no saved result on failure. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
