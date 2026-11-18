# 057 · Validate and re-encode listing photos

**Estimate** 45 minutes · **Stage** Photos  
**Prerequisites** #10

## In brief

Turn a selected JPEG or PNG into a safe, bounded stored image.

## Technical steps

1. Add Pillow and implement `validate_photo(upload)` in `images.py`. Limit bytes to 3 MiB and reject empty, broken, animated, unsupported, or oversized-dimension input. Check decoded format and dimensions, then re-encode JPEG or PNG without copied metadata.
2. Return bytes, a safe extension and format to the upload path. Cover at least a valid JPEG and PNG, a disguised text file, and a malformed photo.

## In first-time-coder language

1. Look inside the actual file to see if it is a photo. A filename that ends with jpg is only a label. Make sure the photo is small enough to work with.
2. Save a fresh copy in a supported format so private photo details are left behind.

## Check your work

- [ ] Valid JPEG and PNG output can be opened again and contains no input metadata.
- [ ] Wrong bytes, excessive size or dimensions, and animated images are refused with clear errors.

## Learn or get unstuck

Read or watch the relevant part, then try a small practice example. Use the tutoring prompt when you want a hint or an explanation of an error.

- [Pillow Image documentation on opening and saving](https://pillow.readthedocs.io/en/stable/reference/Image.html)
- [Pillow tutorial on reading and saving images](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)
- [Flask file uploads and safe serving](https://flask.palletsprojects.com/en/stable/patterns/fileuploads/)

**Copy this tutoring prompt**

> I am a first-time programmer working on ExtraCredit ticket 057, Validate and re-encode listing photos. Teach me the prerequisite ideas for file content, image decoding, dimensions, and metadata. Start with a small unrelated example, explain each term, and ask one question to check my understanding. Then have me describe my approach and give me one hint at a time. Please leave the ticket implementation to me.

## Review before merging

Paste the prompt below along with this ticket's Check your work section, your relevant code diff or draft, and the results you actually observed. Remove secrets, private records, local config values, and real account details before sharing. Run any missing checks yourself and ask a teammate to review the pull request.

> Review my hand-written work for ExtraCredit ticket 057, Validate and re-encode listing photos, using the acceptance checks I paste below. Check inputs are bounded before expensive work, decoded instead of trusting filenames, and re-encoded without metadata. For each check, say Pass, Fail, or Unverified and cite the relevant line, result, or missing evidence. Identify merge blockers and suggest up to two small tests I can run. Explain fixes as hints so I can make them myself. Only report a test as run if I supplied its actual result.
