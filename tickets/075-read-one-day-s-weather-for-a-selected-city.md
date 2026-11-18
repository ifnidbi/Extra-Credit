# 075 · Read one day's weather for a selected city

**Estimate** 45 minutes · **Stage** Weather  
**Prerequisites** #74

## In brief

Fetch the forecast data the app will save and display.

## Technical steps

1. In `weather_client.py`, implement `fetch_forecast(latitude, longitude)`. Use the fixed Open-Meteo forecast endpoint with `timezone=auto`, Celsius, and one day of daily max temperature and precipitation probability.
2. Read the local forecast date and stable numeric fields from the returned data. Validate shape and plausible ranges. Map malformed responses, failures and timeout to 502.

## In first-time-coder language

1. Use the map position of a chosen city to ask for one day's weather. Take the date in that city, the highest temperature, and the rain chance from the answer.
2. Check the list and numbers exist before treating the answer as valid.

## Check your work

- [ ] A known or mocked response yields exactly the storage fields from the contract with the local date.
- [ ] Malformed dates, missing values, bad probabilities, and provider failure are reported as a stable 502.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Open-Meteo interactive forecast documentation](https://open-meteo.com/en/docs)
- [Requests Quickstart on JSON, errors, and timeouts](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Python dates and ISO strings](https://docs.python.org/3/library/datetime.html)
- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 075, Read one day's weather for a selected city. Teach me the prerequisite ideas for daily JSON arrays, local dates, numeric parsing, and error responses. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 075, Read one day's weather for a selected city, using the acceptance checks I paste below. Check the requested units and timezone, safe array handling, and that malformed data never becomes a forecast. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
