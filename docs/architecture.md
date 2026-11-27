# ExtraCredit architecture

ExtraCredit is a single Flask app for the course demo. Python handles routing, permissions, validation, and business rules. SQL runs directly through MySQL Connector/Python so students can see and explain their queries. Jinja builds pages on the server. Plain JavaScript uses Fetch for interactive listing, inquiry, report, and weather features. Chart.js draws one report chart. Pillow verifies and re-encodes uploaded photos, ReportLab creates PDF exports, the standard library creates CSV, Requests calls Open-Meteo, and pytest runs automated checks. Use Python 3.12 or 3.13 and MySQL 8.4 LTS. Dependency versions are pinned in the requirements files. [Flask tutorial](https://flask.palletsprojects.com/en/stable/tutorial/) · [Connector/Python](https://dev.mysql.com/doc/connector-python/en/) · [Chart.js](https://www.chartjs.org/docs/latest/getting-started/) · [ReportLab](https://docs.reportlab.com/reportlab/userguide/ch1_intro/)

## Architecture diagram

![The browser talks to Flask over HTTP. Flask talks to MySQL, Open-Meteo, email delivery, and local photo storage.](evidence/architecture-diagram.png)

## Where to find the code

| File | Responsibilities |
| --- | --- |
| `extracredit/__init__.py`, `routes/site.py` | App factory, Flask configuration, error handlers, CSRF, home redirect and health route. |
| `common.py`, `db.py`, `setup_db.py` | Shared validation and errors, bound SQL, per-request connections, transactions, and local database setup commands. |
| `accounts.py`, `verification.py` | Ontario Tech registration, email confirmation, sessions, role checks, profiles, and deactivation. |
| `campus.py` | Ontario Tech school, student email domain, campus places, and local demo accounts. |
| `catalog.py`, `photos.py` | Listing search and CRUD, category management, photo validation and access, and listing status updates. |
| `inquiries.py` | Participant-only inquiry data, pickup form validation, and seller decisions. |
| `reports.py` | Fixed registry for the ten views, chart data, and CSV/PDF exports. |
| `weather.py` | Open-Meteo Oshawa forecast requests and per-student snapshot history. |
| `templates/`, `static/` | Simple Jinja pages, shared CSS, Fetch handlers, and the bundled Chart.js asset. |
| `sql/`, `tests/` | Schema, demo rows, the ten views, and integration checks on isolated MySQL databases. |

Each feature file keeps its routes, rules, and SQL together so a reader can follow a request in one place.

## Configuration and startup

`SECRET_KEY`, `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_SOCKET`, `UPLOAD_DIR`, and `COOKIE_SECURE` come from environment variables. Default the database name to `extra_credit`. Integration tests create uniquely named databases with the `extra_credit_test_` prefix. The real local configuration is private. An example file holds placeholders only. Limit each photo to 3 MiB and place a 4 MiB request cap on the app to allow multipart overhead. Use 50 results per catalog page. Use MySQL InnoDB with utf8mb4 and set database connections to UTC. Use autocommit for standalone reads and open an explicit transaction for coordinated writes. Run the dev server on the developer machine for coursework. A deployed service would require HTTPS and production hosting configuration. [Flask configuration](https://flask.palletsprojects.com/en/stable/config/)

## Roles and permissions

- **Guest** can view sign-in, registration, and confirmation pages. Listings, categories, photos, and marketplace APIs require a session.
- **User** is an active Ontario Tech account. Public registration requires an exact `@ontariotechu.net` address and current student self-attestation. A signed link expires in 24 hours. Confirmation also requires the ExtraCredit password chosen at registration. Login reloads access from MySQL. Session cookies are HttpOnly and SameSite=Lax, with Secure on HTTPS.
- **Demo mode** enables only the fictional accounts from the seed and writes confirmation links to a private local outbox. With demo mode off, confirmation uses an HTTPS app URL and the configured STARTTLS mail service. Mailbox confirmation and current student self-attestation are separate checks.
- **Owner or buyer** is a relationship to a particular record. Owners maintain their own listings and photos. Buyers can read and maintain their own pending inquiries. A seller sees inquiries on their own listings and can decide them. Only inquiry participants see contact information for that exchange. Catalog responses omit student emails and account internals.
- **Admin** manages categories, views reports, and may remove listings for moderation. Role checks run on the server. Admin access to reporting does not confer buyer or seller actions on purchase inquiries.
- Cookie-backed write requests require Flask-WTF CSRF protection, including JSON and photo uploads. Standard HTML forms submit a token. JavaScript reads it from the page and sends `X-CSRFToken`. Use Jinja escaping, DOM text nodes for untrusted strings, and Connector/Python bound values. [Flask-WTF CSRF](https://flask-wtf.readthedocs.io/en/1.2.x/csrf/) · [Werkzeug password utilities](https://werkzeug.palletsprojects.com/en/stable/utils/#security-helpers)

## Web pages and endpoints

Server pages use GET unless shown otherwise. Account form POSTs use redirect-after-success and redisplay field errors. The browser uses same-origin Fetch for JSON. Routes that return JSON use an envelope with `data` on success and `error` containing `code`, `message`, and optional `fields` on failure. DELETE returns 204 with an empty body. Dates are ISO strings and currency amounts are decimal strings. Use 201 on create, 400 on bad input, 401 for anonymous JSON access, 403 for role denial, 404 for missing or intentionally hidden records, 409 for state conflicts, 413 for oversized input, 502 for provider failure, and 503 for database unavailability. Guests visiting protected HTML pages go to login. Issue checks should examine status codes and visible output.

Listing creation and edits use Fetch and stay in the editor. Creating a listing reveals photo controls and updates the address to the saved edit page so that a refresh can load it again. JavaScript checks price ranges, currency requirements, whole-yen prices and pickup dates before submitting. Flask repeats validation at the API boundary.

| Page or API | Methods and access | Contract |
| --- | --- | --- |
| `/`, `/health` | GET, everyone | Redirect root to the catalog, which sends guests to sign-in. Health returns simple app status with no DB requirement. |
| `/register`, `/verify-email/<token>`, `/login`, `/logout` | GET/POST, POST only for logout | Registration creates a pending account. A signed link and the ExtraCredit password confirm the mailbox before sign-in. Login opens the session. Logout clears it. |
| `/account`, `/api/account` | Page GET, API GET/PUT/DELETE, active user | Include own name, email, school and role. Profile edits the name. The school is fixed to Ontario Tech University. DELETE checks password, deactivates an ordinary user, and clears their session. Admin demo accounts stay managed locally. |
| `/listings`, `/listings/<listing_id>` | GET, signed in | Browse/filter, see an item, photo gallery, and role-appropriate controls. Available, Reserved, and Sold are visible in detail. Removed is visible only to its owner or admin. The searchable catalog defaults to Available. |
| `/dashboard`, `/listings/new`, `/listings/<listing_id>/edit` | GET, signed in, owner-only for edit | Owner's listings and listing editor. Photo upload follows initial creation. |
| `/api/listings`, `/api/listings/<listing_id>` | GET/POST collection, GET/PUT/DELETE single | GET returns browse or details. POST and PUT use `title`, `description`, `price`, `currency_code`, `item_condition`, `category_id`, and `campus_name`. Identity, status, and timestamps come from the server. DELETE marks Removed. |
| `/api/listings/<listing_id>/status` | PUT, owner | Accepts `listing_status` equal to Sold. Reservation happens on accepting an inquiry. |
| `/admin/categories`, `/api/categories`, `/api/categories/<category_id>` | Admin page GET, signed-in API list GET, admin POST/PUT/DELETE | Make, rename, and remove a category. Deleting a category in use returns 409. |
| `/api/listings/<listing_id>/images`, `/api/listings/<listing_id>/images/<image_id>`, `/media/listings/<listing_id>/<image_id>` | Owner POST/DELETE, signed-in media GET subject to listing visibility | Upload one JPEG or PNG in field `photo`. Return an image ID and media URL. Resolve the owned row and serve from the configured directory using its generated key. |
| `/inquiries`, `/api/inquiries`, `/api/inquiries/<inquiry_id>` | Page GET, API GET/POST collection, GET/PUT/DELETE single, active users | Collection GET accepts `direction=incoming` or `outgoing`. POST accepts `listing_id`, `pickup_location`, `payment_method`, `preferred_date`. PUT edits the buyer's pending request. DELETE withdraws it. |
| `/api/inquiries/<inquiry_id>/decision` | PUT, seller of associated listing | Accepts `decision` equal to Accepted or Declined. Returns resulting inquiry. |
| `/reports/catalog`, `/reports/activity` | GET, admin | Five catalog reports and five activity reports. All ten render in HTML tables and retain column labels for empty data. |
| `/api/reports/<report_key>`, `/api/reports/category-counts` | GET, admin | First returns ordered columns and rows for one view. Second returns category names and listing counts for the chart. |
| `/api/reports/<report_key>/export.csv`, `/api/reports/<report_key>/export.pdf` | GET, admin | Export the same registered rows and columns. Fixed per-report filenames. Neutralize spreadsheet formula-like text in CSV, escape untrusted display text in PDF, and paginate PDF tables. |
| `/pickup-weather`, `/api/weather/snapshots` | Page GET, snapshots GET/POST, active users | POST fetches and saves the Oshawa forecast. GET lists the student's latest 10 Oshawa snapshots. |

### Shared JSON field names

| Resource | Fields inside the `data` envelope |
| --- | --- |
| Account | `student_id`, `full_name`, `email`, `school_name`, `role`. |
| Category | `category_id`, `category_name`. The collection is an array. |
| Listing | `listing_id`, `title`, `description`, `category_id`, `category_name`, `campus_name`, `price`, `currency_code`, `item_condition`, `listing_status`, `date_posted`, `seller_name`. Listing search wraps the array as `items`, `page`, `has_next`. Use `currency` for the search parameter and `currency_code` for the listing field. |
| Photo | `image_id`, `media_url`. |
| Inquiry | `inquiry_id`, `listing_id`, `listing_title`, `buyer_name`, `seller_name`, `other_party_email`, `pickup_location`, `payment_method`, `preferred_date`, `inquiry_status`, `submitted_at`. Direction-filtered lists are arrays. |
| Report | `title`, `columns`, `rows`. Each column has `key` and `label`. Each row is keyed by column key. The chart uses an array of `category_name` and `listing_count` entries. |
| Weather | Snapshot entries use `snapshot_id`, `place_label`, `latitude`, `longitude`, `forecast_date`, `max_temp_c`, `precip_probability`, and `fetched_at`. The history response is an array. |

## Data rules

- Normalize account emails using trim and lowercase. Enforce unique normalized addresses, a required student attestation, a 12–128 character password, and lengths from the database. Deactivation keeps rows for foreign-key history, hides that seller's listings from marketplace search/detail, and blocks future sign-ins. Owner dashboard and inquiry history stay role scoped. Category names are trimmed and unique.
- Listing input uses `Decimal` and has at most two fractional digits. Reject negative, non-finite, or out-of-range amounts. The currency list for the demo is CAD, USD, EUR, GBP, and JPY. JPY requires a whole amount. Keep amount and currency together in HTML, API, and exports. Price bounds require a selected currency and must be ordered. Reject unknown conditions, currencies, and categories. Sort catalog results by newest time then descending ID for stable pages. The campus is selected from North Oshawa and Downtown Oshawa. A listing with a pending or accepted pickup keeps its campus.
- Valid conditions are New, Like New, Good, Fair, and Poor. An owner edits only Available or Reserved listing content. Only accepting an inquiry can change Available to Reserved. An owner can mark an Available or Reserved listing Sold. An owner or admin can mark a non-Removed listing Removed. Repeating a completed state action may return 409. Sold or Removed listings decline still-Pending inquiries in the same transaction.
- The buyer must differ from the seller and can have at most one Pending inquiry per Available listing. A buyer can edit or withdraw only their own Pending inquiry. Use ISO dates and reject dates before today's app date in UTC. Pay by Cash, E-transfer, or Other as a preference. The app records pickup plans at listed public campus spots. Payment preferences are informational. Seller acceptance reserves the listing and declines other Pending inquiries in one transaction. Lock the listing first, then read or lock inquiries for any write that depends on listing state. See the database guide for state and history.
- Images are verified with Pillow and re-encoded without metadata. Generate random file keys and confirm the row belongs to the requested listing. Limit to a small fixed maximum of five photos per listing, enforced under the listing lock. If DB insert fails after saving, clean up the new file. When deleting an image, commit row removal first, then unlink the file and log any orphan for cleanup. Invalid, missing, or invisible images use a placeholder or 404 as appropriate. [Flask upload guide](https://flask.palletsprojects.com/en/stable/patterns/fileuploads/) · [Pillow image API](https://pillow.readthedocs.io/en/stable/reference/Image.html)
- Weather uses a shared Oshawa forecast for both campuses. Flask supplies a fixed public city coordinate and requests the local date, daily high in Celsius, and rain probability from Open-Meteo. A bound INSERT stores the parsed result and a bound SELECT reads the signed-in student's history. [Forecast API](https://open-meteo.com/en/docs)
