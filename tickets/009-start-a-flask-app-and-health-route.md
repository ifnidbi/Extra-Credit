# 009 · Start a Flask app and health route

**Estimate** 45 minutes · **Stage** Foundation  
**Prerequisites** None. Start any time.

## In brief

Create the smallest runnable version of ExtraCredit.

## Technical steps

1. Create `requirements.txt`, `extracredit/__init__.py`, and `routes/site.py` under the package. Put Flask in the environment and wire a site blueprint from `create_app(test_config=None)`.
2. Serve a temporary welcome at `/` and a JSON success body at `GET /health`. Run Flask locally from a clean virtual environment.

## In first-time-coder language

1. Start a tiny web server that says hello. Give it one special address called health where it can say it is running.
2. Start it in a clean Python environment and visit both addresses.

## Check your work

- [ ] Both paths respond with 200 and health has a JSON data envelope.
- [ ] The app factory can create two app instances, and health runs with MySQL stopped.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Flask quickstart with minimal examples](https://flask.palletsprojects.com/en/stable/quickstart/)
- [Flask application factory guide](https://flask.palletsprojects.com/en/stable/patterns/appfactories/)
- [Python virtual environments and pip](https://docs.python.org/3/tutorial/venv.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 009, Start a Flask app and health route. Teach me the prerequisite ideas for virtual environments, Flask app factories, routes, and JSON responses. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 009, Start a Flask app and health route, using the acceptance checks I paste below. Check that the app really starts, the two paths respond, and health does not reach into the DB. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
