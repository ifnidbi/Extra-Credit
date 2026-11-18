# 085 · Walk through the app and its error states

**Estimate** 60 minutes · **Stage** Verification  
**Prerequisites** #45, #50, #61, #67, #70, #77, #78

## In brief

Catch gaps between backend checks and actual browser behavior.

## Technical steps

1. In `docs/smoke-checks.md`, record steps/results for guest browse, category administration, student signup/login, listing editor, photos, buyer/seller inquiry flow, charts, exports, and weather. Try a DB outage locally and a bad form, then restore configured services.
2. Check keyboard paths and narrow layout. Open small follow-up bug issues with reproducible steps if anything is off, and attach sanitized evidence.

## In first-time-coder language

1. Use the app with three pretend roles and write down what happens. Try happy paths and a few wrong inputs, then see how the app acts when its database is off.
2. Check that the pages still work with Tab and a small window. Record any issue a teammate can reproduce.

## Check your work

- [ ] Evidence lists expected and actual results, including database unavailable and user input errors.
- [ ] A second person can reproduce important flows and any reported bug from the notes.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [SOFE 3700U coverage and evidence checklist](../docs/course-coverage.md)
- [Chrome DevTools Network panel screenshot walkthrough](https://developer.chrome.com/docs/devtools/network/)
- [Flask error handling reference and examples](https://flask.palletsprojects.com/en/stable/errorhandling/)
- [GitHub linking pull requests and issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 085, Walk through the app and its error states. Teach me the prerequisite ideas for end-to-end checks, error troubleshooting, and reproducible bug reports. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 085, Walk through the app and its error states, using the acceptance checks I paste below. Read my smoke evidence and call out missing roles, untested journeys, or reports too vague to reproduce. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
