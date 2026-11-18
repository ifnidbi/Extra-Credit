# 084 · Test weather without depending on the live API

**Estimate** 45 minutes · **Stage** Verification  
**Prerequisites** #77, #78

## In brief

Make repeatable tests for saving and reading provider data.

## Technical steps

1. Write `tests/test_weather.py` using representative fake provider JSON and timeout/malformed responses. Assert valid snapshots save and are listed for their owner. Cover bad coordinates, API failure without a write, ordering, and access from another user.
2. Run one separately documented live smoke test for search and forecast when the provider is reachable.

## In first-time-coder language

1. Pretend the weather service gave a good answer, a broken answer, and no answer. Make sure the good one gets saved for the right student and the others do not.
2. Try one real city separately so you know the provider still speaks the same format.

## Check your work

- [ ] Normal automated tests run without external network and prove save/read isolation.
- [ ] Timeout and bad JSON produce stable responses with no new snapshot. Live smoke result is recorded separately.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [pytest monkeypatch examples for dependencies](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
- [Requests Quickstart on JSON, errors, and timeouts](https://requests.readthedocs.io/en/latest/user/quickstart/)
- [Open-Meteo interactive forecast documentation](https://open-meteo.com/en/docs)
- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 084, Test weather without depending on the live API. Teach me the prerequisite ideas for mocked network requests, fixtures, ownership checks, and live smoke testing. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 084, Test weather without depending on the live API, using the acceptance checks I paste below. Check that tests do not silently call real services or pass despite wrong ownership or partial writes. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
