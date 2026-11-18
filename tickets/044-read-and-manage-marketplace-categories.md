# 044 · Read and manage marketplace categories

**Estimate** 60 minutes · **Stage** Listings  
**Prerequisites** #15, #19, #37

## In brief

Expose category choices and admin changes with consistent errors.

## Technical steps

1. Create `category_repo.py` and `categories.py` with the read/create/rename/delete functions in the architecture. Validate trimmed names and map duplicate names or FK-in-use deletion to 409.
2. Wire GET and admin write methods in `routes/category_api.py`. Use bound SQL and return categories in name order.

## In first-time-coder language

1. Let everybody ask for the list of category labels. Let an admin add, rename, or remove a label.
2. If a category already exists or something is listed in it, explain why the requested change is refused.

## Check your work

- [ ] Guests can read categories, and only admins can write them.
- [ ] Create, rename, and deletion of an unused category persist. Duplicate names and deleting a used category return a stable conflict.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [ExtraCredit architecture and endpoint contracts](../docs/architecture.md)
- [MySQL foreign key constraints and actions](https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html)
- [Connector/Python parameter binding with cursor execute](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html)
- [MySQL DELETE syntax and conditions](https://dev.mysql.com/doc/refman/8.4/en/delete.html)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 044, Read and manage marketplace categories. Teach me the prerequisite ideas for read-only resources, validated writes, and foreign-key conflicts. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 044, Read and manage marketplace categories, using the acceptance checks I paste below. Check permissions on every method, error mapping, and behavior when a listing still references a category. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
