# 077 · Build the pickup-weather page

**Estimate** 45 minutes · **Stage** Weather  
**Prerequisites** #42, #76

## In brief

Show a city search, provider weather result, and saved history.

## Technical steps

1. Add signed-in GET `/pickup-weather`, `weather/index.html`, and `static/weather.js`. Query suggestions by Fetch, let the user pick a labeled global city, POST the selected label and coordinates, and refresh saved history. Ignore stale matches after a new query.
2. Add provider attribution near the displayed weather, loading/error states, and date, Celsius temperature and a rain percentage.

## In first-time-coder language

1. Make a page where a student types their campus city, picks the right match, and asks for weather. Show the answer and keep it on their lookup list.
2. Tell them where the forecast came from and explain when the provider is unavailable.

## Check your work

- [ ] A student can select a city and view a saved value on the page without reloading.
- [ ] Empty or failed external requests are readable, and provider attribution and units are visible.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Open-Meteo interactive geocoding documentation](https://open-meteo.com/en/docs/geocoding-api)
- [Open-Meteo interactive forecast documentation](https://open-meteo.com/en/docs)
- [Open-Meteo terms and data attribution](https://open-meteo.com/en/terms)
- [MDN Using Fetch with examples](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 077, Build the pickup-weather page. Teach me the prerequisite ideas for autocompletion, selection, asynchronous state, and attribution. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 077, Build the pickup-weather page, using the acceptance checks I paste below. Check selected labels, requests, stale matches, result fields and visible credit for the data. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
