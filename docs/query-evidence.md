# Query and demo evidence

Use these results with the [report checklist](report-checklist.md). The captures come from a running Flask app, MySQL 8.4.11, and Chrome. The marketplace records and email addresses are fictional. The weather capture uses a live forecast.

## Database, views, and chart

The fresh seed produced 6 Students, 6 Categories, 9 Listings, 7 Listing Images, and 8 Purchase Inquiries. Pickup Forecasts starts with 0 rows and gets its first row when a member saves a forecast. To reproduce the counts, run `SELECT COUNT(*) FROM Students` and repeat for the other tables. [Schema and ER diagram](database.md)

| View | MySQL view | Seed rows | App screenshot |
| --- | --- | ---: | --- |
| 1 | `v_listing_details` | 9 | [Three-table listing join](evidence/view-01.png) |
| 2 | `v_seller_price_comparison` | 4 | [Currency-scoped ANY and GROUP BY](evidence/view-02.png) |
| 3 | `v_above_category_average` | 3 | [Correlated category average](evidence/view-03.png) |
| 4 | `v_listing_inquiry_overview` | 11 | [MySQL full outer join equivalent](evidence/view-04.png) |
| 5 | `v_active_students` | 5 | [Nested UNION for students with activity](evidence/view-05.png) |
| 6 | `v_available_listings` | 6 | [Available items](evidence/view-06.png) |
| 7 | `v_category_summary` | 7 | [Categories and currency groups](evidence/view-07.png) |
| 8 | `v_pending_inquiries` | 4 | [Pending pickup plans](evidence/view-08.png) |
| 9 | `v_available_without_images` | 2 | [Available items with no image rows](evidence/view-09.png) |
| 10 | `v_student_selling_summary` | 6 | [Selling summary including zeroes](evidence/view-10.png) |

The screenshot run registered one extra fictional user before opening the reports. View 10 therefore shows seven rows in that capture, including the new student with zero listings. The other view counts matched the fresh seed. View 4 returned listings with no inquiry. An independent scratch check with left IDs 1–2 and right IDs 2–3 returned `(1, NULL)`, `(2, 2)`, and `(NULL, 3)`. The real inquiry foreign key prevents orphaned inquiries. TA acceptance of the equivalent is still unconfirmed.

The chart reads category counts from view 7, summed across currencies. Expected totals are Clothing 1, Electronics 2, Furniture 2, School Supplies 0, Sports Equipment 1, and Textbooks 3. [Chart screenshot](evidence/category-chart.png) · [Actual CSV download](evidence/listing-details.csv) · [Actual PDF download](evidence/listing-details.pdf)

## Browser flow

| Check | Observed result | Evidence |
| --- | --- | --- |
| Search and Fetch | Lakeview, CAD, and the 40–50 price range returned listing 1 without a page navigation. | [Catalog search](evidence/catalog-filter.png) |
| Registration and roles | A fictional Riverside student registered. A guest was directed to sign in for reports, a regular student received 403, and the admin opened both report pages. | Reproduce with separate browser sessions and the [demo accounts](../README.md#run-locally). |
| Listing CRUD | Seller created listing 10, read it, changed its price from 19.25 to 20.00 CAD, marked it Sold, and removed it. The guest detail endpoint then returned 404. | [After PUT](evidence/listing-after-update.png) · [After DELETE](evidence/listing-removed.png) |
| Buyer and seller inquiry | Buyer created inquiry 9 over Fetch. The seller accepted it, which reserved listing 10. The integration tests also demonstrated a rolled-back acceptance and a declined competing request. | [Buyer submits](evidence/pickup-request.png) · [Seller accepts](evidence/inquiry-accepted.png) |
| Live external API | A Toronto geocoding result was selected and a forecast was saved with HTTP 201. A separate GET returned the same snapshot from MySQL. | [Saved weather history](evidence/weather-live.png) |

## Queries to include in the report

- Read listings through `GET /api/listings` or `GET /api/listings/1`. Write with the collection POST, the item PUT, and the item DELETE. Show the record before and after updates, including the stored Removed state. The SQL uses a bound SELECT, INSERT, and UPDATE. [Listings code](../extracredit/catalog.py)
- Show the buyer's inquiry insert and the seller transaction. Acceptance updates the inquiry, reserves the listing, and declines other waiting requests for that listing in one transaction. [Inquiry code](../extracredit/inquiries.py)
- For the external data, show the provider call and the two DB operations separately. POST saves parsed fields with `INSERT INTO Pickup_Forecasts (...)`. GET uses a bound `SELECT … FROM Pickup_Forecasts WHERE student_id = %s ORDER BY fetched_at DESC, snapshot_id DESC LIMIT 10`. The browser capture shows the resulting history. [Weather code](../extracredit/weather.py)
- For reproducible view results, run `SELECT * FROM v_listing_details ORDER BY listing_id`, then substitute each view and its documented sort. Use the admin report page or MySQL query tool to capture a new screenshot if the seed changes. [View definitions and sorts](database.md#phase-ii-views)
- Include the measured query plan and timings, with dataset size and limits. [Performance results](performance.md)

## Verification notes

Fourteen tests passed against MySQL 8.4.11. They cover the database-independent health route, a database outage, registration, sessions and CSRF, role and ownership checks, listing CRUD and filters, category CRUD, private inquiries and rollback, photo upload and cleanup, the ten views, CSV/PDF output, and mocked weather errors. The browser run exercised registration, search, listings, inquiries, report tables, the chart, exports, and a live weather save and read. Runtime verification used macOS. The README also provides Windows and Linux setup commands.

One issue caught during visual review was chart animation showing interim bar heights during the capture. The report chart now renders immediately at the actual counts.
