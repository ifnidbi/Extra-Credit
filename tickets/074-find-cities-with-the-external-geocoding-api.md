# 074 · Find cities with the external geocoding API

**Estimate** 45 minutes · **Stage** Weather  
**Prerequisites** #9

## In brief

Turn a typed city into a few unambiguous place suggestions.

## Technical steps

1. In `weather_client.py`, write `search_places(query)` with Requests using Open-Meteo's fixed geocoding endpoint, a length check, five results, a finite timeout, and stable error mapping. Return display labels with available city, region, and country plus normalized coordinates.
2. Try a city with multiple matches, no results, and a mocked provider failure.

## In first-time-coder language

1. Ask an outside service where a city is when a student types its name. Give back a few matches with enough region or country information to choose the right one.
2. If the service is slow or gives a broken answer, report the problem without showing its raw response.

## Check your work

- [ ] A recognized city produces up to five sensible places and no results yields an empty list.
- [ ] Too-short input, timeout and malformed upstream data are handled without crashing.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Open-Meteo interactive geocoding documentation](https://open-meteo.com/en/docs/geocoding-api)
- [Requests Quickstart on JSON, errors, and timeouts](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [MDN overview of HTTP diagrams and examples](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)
- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 074, Find cities with the external geocoding API. Teach me the prerequisite ideas for external APIs, query parameters, timeouts, and JSON parsing. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 074, Find cities with the external geocoding API, using the acceptance checks I paste below. Check we use a fixed endpoint, validate shape and coordinates, and handle empty and failed provider responses. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
