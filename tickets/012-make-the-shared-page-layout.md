# 012 · Make the shared page layout

**Estimate** 45 minutes · **Stage** Foundation  
**Prerequisites** #9

## In brief

Give new pages a consistent title, navigation, and content area.

## Technical steps

1. Create `extracredit/templates/base.html` and `static/site.css`. Add Jinja title and content blocks, semantic header/main/footer, and links that resolve to existing routes only.
2. Render the welcome through a small template extending the base. Include keyboard focus styling and a readable narrow layout.

## In first-time-coder language

1. Make one page frame for the whole site. Give every page a place for its own title and contents.
2. Use the frame on the welcome page. Open it on a narrow window and check you can see the focused link when using Tab.

## Check your work

- [ ] The welcome inherits one shared frame and styles load.
- [ ] Keyboard navigation and a narrow viewport still make the title and content easy to use.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Flask tutorial on writing templates](https://flask.palletsprojects.com/en/stable/tutorial/templates/)
- [Jinja inheritance, loops, and escaping](https://jinja.palletsprojects.com/en/stable/templates/)
- [MDN CSS first steps](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 012, Make the shared page layout. Teach me the prerequisite ideas for Jinja inheritance, semantic HTML, and keyboard focus. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 012, Make the shared page layout, using the acceptance checks I paste below. Check the inheritance, existing route links, semantic structure, and focus styling. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
