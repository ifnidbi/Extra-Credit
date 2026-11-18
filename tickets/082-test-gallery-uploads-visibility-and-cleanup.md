# 082 · Test gallery uploads, visibility, and cleanup

**Estimate** 45 minutes · **Stage** Verification  
**Prerequisites** #61, #78

## In brief

Verify photo handling across the database and filesystem.

## Technical steps

1. Write `tests/test_images.py` for valid image upload/read/DELETE, bad bytes, owner checks and missing media. Use generated test images, fixture upload directory, and assert the row and file for each valid lifecycle step.
2. Simulate a DB failure after file write and verify cleanup. Check the five-photo limit and removed-listing visibility.

## In first-time-coder language

1. Have the tests send a small pretend picture and check both its saved file and row, then remove it and check both are gone.
2. Send a broken file or try as the wrong student. Make the database save fail once and check the new file did not get left around.

## Check your work

- [ ] Valid image lifecycle leaves the expected row and bytes at each step.
- [ ] Invalid files, access violations, limit and simulated DB failure leave no unintended rows or files.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Pillow tutorial on reading and saving images](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)
- [Flask tests and test client examples](https://flask.palletsprojects.com/en/stable/testing/)
- [pytest monkeypatch examples for dependencies](https://docs.pytest.org/en/stable/how-to/monkeypatch.html)
- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 082, Test gallery uploads, visibility, and cleanup. Teach me the prerequisite ideas for multipart testing, temp paths, and failure cleanup. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 082, Test gallery uploads, visibility, and cleanup, using the acceptance checks I paste below. Check tests use real encoded bytes, assert both storage layers, and include the right permission and count edges. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
