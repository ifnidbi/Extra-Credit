# Build tickets

The original tickets record the build plan. The [current architecture](../docs/architecture.md) describes the implemented Ontario Tech scope, including account confirmation, campus pickup, and Oshawa weather.

Tickets 001–006 are individual exercises that use a scratch folder or practice repo. Everybody can do them. The table shows the estimated time for one person's work, including their first check. If you're new to a topic, take an extra learning pass with the linked material. A dependency is complete when the change it needs is merged and verified, or when a local-only setup step works for the person taking the next ticket.

## Start in parallel

- Everybody can do a short practice exercise while one person starts the Flask app (009) and another sets up MySQL (011).
- The diagram (007) and demo outline (008) can be drafted before any app code.
- After the Students and Categories tables land, start listing schema, forecast schema, and account fixtures in parallel. Write separate view files as their fixtures become available.
- During the app build, one person can work on identity and permissions, one on catalog and photos, and one on the view/report contracts. Add weather and inquiry work as their prerequisites land. Keep one branch for one ticket and coordinate if two issues touch the same file.
- Any three available tasks can be taken in parallel. Use the prerequisite column to decide what is actually ready.

| ID | Ticket | Stage | Estimate | Prerequisites | GitHub |
| --- | --- | --- | ---: | --- | --- |
| 001 | [Run your first terminal commands](001-run-your-first-terminal-commands.md) | Practice | 15 min | None | [#1](https://github.com/ifnidbi/Extra-Credit/issues/1) |
| 002 | [Write a tiny Python price label](002-write-a-tiny-python-price-label.md) | Practice | 30 min | None | [#2](https://github.com/ifnidbi/Extra-Credit/issues/2) |
| 003 | [Build a one-page practice item card](003-build-a-one-page-practice-item-card.md) | Practice | 30 min | None | [#3](https://github.com/ifnidbi/Extra-Credit/issues/3) |
| 004 | [Ask a practice database two questions](004-ask-a-practice-database-two-questions.md) | Practice | 30 min | None | [#4](https://github.com/ifnidbi/Extra-Credit/issues/4) |
| 005 | [Make a branch and a practice pull request](005-make-a-branch-and-a-practice-pull-request.md) | Practice | 30 min | None | [#5](https://github.com/ifnidbi/Extra-Credit/issues/5) |
| 006 | [Read a JSON response in the browser](006-read-a-json-response-in-the-browser.md) | Practice | 30 min | None | [#6](https://github.com/ifnidbi/Extra-Credit/issues/6) |
| 007 | [Update the marketplace relationship diagram](007-update-the-marketplace-relationship-diagram.md) | Practice | 45 min | None | [#7](https://github.com/ifnidbi/Extra-Credit/issues/7) |
| 008 | [Draft the screens and demo path](008-draft-the-screens-and-demo-path.md) | Practice | 30 min | None | [#8](https://github.com/ifnidbi/Extra-Credit/issues/8) |
| 009 | [Start a Flask app and health route](009-start-a-flask-app-and-health-route.md) | Foundation | 45 min | None | [#9](https://github.com/ifnidbi/Extra-Credit/issues/9) |
| 010 | [Keep secrets and settings local](010-keep-secrets-and-settings-local.md) | Foundation | 45 min | 009 | [#10](https://github.com/ifnidbi/Extra-Credit/issues/10) |
| 011 | [Set up MySQL locally](011-set-up-mysql-locally.md) | Foundation | 45 min | None | [#11](https://github.com/ifnidbi/Extra-Credit/issues/11) |
| 012 | [Make the shared page layout](012-make-the-shared-page-layout.md) | Foundation | 45 min | 009 | [#12](https://github.com/ifnidbi/Extra-Credit/issues/12) |
| 013 | [Standardize app and API errors](013-standardize-app-and-api-errors.md) | Foundation | 60 min | 009 | [#13](https://github.com/ifnidbi/Extra-Credit/issues/13) |
| 014 | [Connect Flask to MySQL per request](014-connect-flask-to-mysql-per-request.md) | Foundation | 60 min | 010, 011, 013 | [#14](https://github.com/ifnidbi/Extra-Credit/issues/14) |
| 015 | [Wrap multi-step writes in a transaction](015-wrap-multi-step-writes-in-a-transaction.md) | Foundation | 45 min | 014 | [#15](https://github.com/ifnidbi/Extra-Credit/issues/15) |
| 016 | [Run your first app test](016-run-your-first-app-test.md) | Foundation | 30 min | 009 | [#16](https://github.com/ifnidbi/Extra-Credit/issues/16) |
| 017 | [Create a fresh development database](017-create-a-fresh-development-database.md) | Database | 30 min | 011 | [#17](https://github.com/ifnidbi/Extra-Credit/issues/17) |
| 018 | [Create the Students table](018-create-the-students-table.md) | Database | 45 min | 017 | [#18](https://github.com/ifnidbi/Extra-Credit/issues/18) |
| 019 | [Create the Categories table](019-create-the-categories-table.md) | Database | 30 min | 017 | [#19](https://github.com/ifnidbi/Extra-Credit/issues/19) |
| 020 | [Create the Listings table](020-create-the-listings-table.md) | Database | 60 min | 018, 019 | [#20](https://github.com/ifnidbi/Extra-Credit/issues/20) |
| 021 | [Create the Listing Images table](021-create-the-listing-images-table.md) | Database | 30 min | 020 | [#21](https://github.com/ifnidbi/Extra-Credit/issues/21) |
| 022 | [Create the Purchase Inquiries table](022-create-the-purchase-inquiries-table.md) | Database | 45 min | 020, 018 | [#22](https://github.com/ifnidbi/Extra-Credit/issues/22) |
| 023 | [Create the Pickup Forecasts table](023-create-the-pickup-forecasts-table.md) | Database | 45 min | 018 | [#23](https://github.com/ifnidbi/Extra-Credit/issues/23) |
| 024 | [Seed fictional students and categories](024-seed-fictional-students-and-categories.md) | Database | 45 min | 018, 019 | [#24](https://github.com/ifnidbi/Extra-Credit/issues/24) |
| 025 | [Seed listings across campuses and currencies](025-seed-listings-across-campuses-and-currencies.md) | Database | 45 min | 020, 024 | [#25](https://github.com/ifnidbi/Extra-Credit/issues/25) |
| 026 | [Seed photos and purchase inquiries](026-seed-photos-and-purchase-inquiries.md) | Database | 45 min | 021, 022, 025 | [#26](https://github.com/ifnidbi/Extra-Credit/issues/26) |
| 027 | [Create view 1 for listing details](027-create-view-1-for-listing-details.md) | Views | 30 min | 025 | [#27](https://github.com/ifnidbi/Extra-Credit/issues/27) |
| 028 | [Create view 2 for seller price comparisons](028-create-view-2-for-seller-price-comparisons.md) | Views | 60 min | 025 | [#28](https://github.com/ifnidbi/Extra-Credit/issues/28) |
| 029 | [Create view 3 for above-average listing prices](029-create-view-3-for-above-average-listing-prices.md) | Views | 45 min | 025 | [#29](https://github.com/ifnidbi/Extra-Credit/issues/29) |
| 030 | [Create view 4 for listings with or without inquiries](030-create-view-4-for-listings-with-or-without-inquiries.md) | Views | 60 min | 026 | [#30](https://github.com/ifnidbi/Extra-Credit/issues/30) |
| 031 | [Create view 5 for students with activity](031-create-view-5-for-students-with-activity.md) | Views | 45 min | 026 | [#31](https://github.com/ifnidbi/Extra-Credit/issues/31) |
| 032 | [Create view 6 for available listings](032-create-view-6-for-available-listings.md) | Views | 30 min | 025 | [#32](https://github.com/ifnidbi/Extra-Credit/issues/32) |
| 033 | [Create view 7 for category totals and averages](033-create-view-7-for-category-totals-and-averages.md) | Views | 45 min | 025 | [#33](https://github.com/ifnidbi/Extra-Credit/issues/33) |
| 034 | [Create view 8 for pending pickup requests](034-create-view-8-for-pending-pickup-requests.md) | Views | 45 min | 026 | [#34](https://github.com/ifnidbi/Extra-Credit/issues/34) |
| 035 | [Create view 9 for available listings missing photos](035-create-view-9-for-available-listings-missing-photos.md) | Views | 30 min | 026 | [#35](https://github.com/ifnidbi/Extra-Credit/issues/35) |
| 036 | [Create view 10 for student selling summaries](036-create-view-10-for-student-selling-summaries.md) | Views | 45 min | 025 | [#36](https://github.com/ifnidbi/Extra-Credit/issues/36) |
| 037 | [Add session identity and permission checks](037-add-session-identity-and-permission-checks.md) | Accounts | 90 min | 010, 012, 013, 014, 018 | [#37](https://github.com/ifnidbi/Extra-Credit/issues/37) |
| 038 | [Validate and store a student registration](038-validate-and-store-a-student-registration.md) | Accounts | 60 min | 015, 037 | [#38](https://github.com/ifnidbi/Extra-Credit/issues/38) |
| 039 | [Build the student signup page](039-build-the-student-signup-page.md) | Accounts | 45 min | 012, 037, 038 | [#39](https://github.com/ifnidbi/Extra-Credit/issues/39) |
| 040 | [Sign in and sign out with a session](040-sign-in-and-sign-out-with-a-session.md) | Accounts | 60 min | 039 | [#40](https://github.com/ifnidbi/Extra-Credit/issues/40) |
| 041 | [Add account read, edit, and deactivation endpoints](041-add-account-read-edit-and-deactivation-endpoints.md) | Accounts | 90 min | 015, 040 | [#41](https://github.com/ifnidbi/Extra-Credit/issues/41) |
| 042 | [Make a shared browser Fetch helper](042-make-a-shared-browser-fetch-helper.md) | Foundation | 45 min | 012, 013, 037 | [#42](https://github.com/ifnidbi/Extra-Credit/issues/42) |
| 043 | [Build the account settings page](043-build-the-account-settings-page.md) | Accounts | 45 min | 041, 042 | [#43](https://github.com/ifnidbi/Extra-Credit/issues/43) |
| 044 | [Read and manage marketplace categories](044-read-and-manage-marketplace-categories.md) | Listings | 60 min | 015, 019, 037 | [#44](https://github.com/ifnidbi/Extra-Credit/issues/44) |
| 045 | [Give admins a category management page](045-give-admins-a-category-management-page.md) | Listings | 45 min | 042, 044 | [#45](https://github.com/ifnidbi/Extra-Credit/issues/45) |
| 046 | [Validate catalog search and price filters](046-validate-catalog-search-and-price-filters.md) | Listings | 45 min | 020 | [#46](https://github.com/ifnidbi/Extra-Credit/issues/46) |
| 047 | [Read catalog and listing details from MySQL](047-read-catalog-and-listing-details-from-mysql.md) | Listings | 60 min | 014, 025, 046 | [#47](https://github.com/ifnidbi/Extra-Credit/issues/47) |
| 048 | [Expose listing reads as JSON](048-expose-listing-reads-as-json.md) | Listings | 45 min | 037, 044, 047 | [#48](https://github.com/ifnidbi/Extra-Credit/issues/48) |
| 049 | [Build the catalog and listing detail pages](049-build-the-catalog-and-listing-detail-pages.md) | Listings | 60 min | 012, 037, 044, 047 | [#49](https://github.com/ifnidbi/Extra-Credit/issues/49) |
| 050 | [Refresh catalog results without reloading](050-refresh-catalog-results-without-reloading.md) | Listings | 45 min | 042, 048, 049 | [#50](https://github.com/ifnidbi/Extra-Credit/issues/50) |
| 051 | [Create a listing through the API](051-create-a-listing-through-the-api.md) | Listings | 60 min | 015, 044, 048 | [#51](https://github.com/ifnidbi/Extra-Credit/issues/51) |
| 052 | [Update a listing as its owner](052-update-a-listing-as-its-owner.md) | Listings | 60 min | 051 | [#52](https://github.com/ifnidbi/Extra-Credit/issues/52) |
| 053 | [Share the listing lock and pending-close query](053-share-the-listing-lock-and-pending-close-query.md) | Listings | 45 min | 015, 022, 052 | [#53](https://github.com/ifnidbi/Extra-Credit/issues/53) |
| 054 | [Mark listings sold or remove them](054-mark-listings-sold-or-remove-them.md) | Listings | 60 min | 053 | [#54](https://github.com/ifnidbi/Extra-Credit/issues/54) |
| 055 | [Build a seller dashboard](055-build-a-seller-dashboard.md) | Listings | 45 min | 042, 049, 054 | [#55](https://github.com/ifnidbi/Extra-Credit/issues/55) |
| 056 | [Connect the listing editor to POST and PUT](056-connect-the-listing-editor-to-post-and-put.md) | Listings | 60 min | 042, 044, 052, 055 | [#56](https://github.com/ifnidbi/Extra-Credit/issues/56) |
| 057 | [Validate and re-encode listing photos](057-validate-and-re-encode-listing-photos.md) | Photos | 45 min | 010 | [#57](https://github.com/ifnidbi/Extra-Credit/issues/57) |
| 058 | [Save a listing photo for its owner](058-save-a-listing-photo-for-its-owner.md) | Photos | 60 min | 021, 037, 051, 053, 057 | [#58](https://github.com/ifnidbi/Extra-Credit/issues/58) |
| 059 | [Serve listing photos in a gallery](059-serve-listing-photos-in-a-gallery.md) | Photos | 45 min | 049, 058 | [#59](https://github.com/ifnidbi/Extra-Credit/issues/59) |
| 060 | [Remove an owned listing photo](060-remove-an-owned-listing-photo.md) | Photos | 45 min | 059 | [#60](https://github.com/ifnidbi/Extra-Credit/issues/60) |
| 061 | [Add photo upload and removal controls](061-add-photo-upload-and-removal-controls.md) | Photos | 45 min | 042, 056, 060 | [#61](https://github.com/ifnidbi/Extra-Credit/issues/61) |
| 062 | [Validate a purchase inquiry](062-validate-a-purchase-inquiry.md) | Inquiries | 45 min | 022 | [#62](https://github.com/ifnidbi/Extra-Credit/issues/62) |
| 063 | [Create a buyer's purchase inquiry](063-create-a-buyer-s-purchase-inquiry.md) | Inquiries | 60 min | 037, 053, 062 | [#63](https://github.com/ifnidbi/Extra-Credit/issues/63) |
| 064 | [Show only inquiries the student participates in](064-show-only-inquiries-the-student-participates-in.md) | Inquiries | 60 min | 040, 063 | [#64](https://github.com/ifnidbi/Extra-Credit/issues/64) |
| 065 | [Edit or withdraw a waiting inquiry](065-edit-or-withdraw-a-waiting-inquiry.md) | Inquiries | 60 min | 064 | [#65](https://github.com/ifnidbi/Extra-Credit/issues/65) |
| 066 | [Accept or decline an inquiry as the seller](066-accept-or-decline-an-inquiry-as-the-seller.md) | Inquiries | 90 min | 054, 065 | [#66](https://github.com/ifnidbi/Extra-Credit/issues/66) |
| 067 | [Build buyer and seller inquiry screens](067-build-buyer-and-seller-inquiry-screens.md) | Inquiries | 60 min | 042, 049, 066 | [#67](https://github.com/ifnidbi/Extra-Credit/issues/67) |
| 068 | [Register and read the ten database views](068-register-and-read-the-ten-database-views.md) | Reports | 60 min | 014, 027, 028, 029, 030, 031, 032, 033, 034, 035, 036, 037 | [#68](https://github.com/ifnidbi/Extra-Credit/issues/68) |
| 069 | [Show five catalog views in HTML tables](069-show-five-catalog-views-in-html-tables.md) | Reports | 45 min | 012, 068 | [#69](https://github.com/ifnidbi/Extra-Credit/issues/69) |
| 070 | [Show five activity views in HTML tables](070-show-five-activity-views-in-html-tables.md) | Reports | 45 min | 069 | [#70](https://github.com/ifnidbi/Extra-Credit/issues/70) |
| 071 | [Draw a category counts chart](071-draw-a-category-counts-chart.md) | Reports | 45 min | 042, 069 | [#71](https://github.com/ifnidbi/Extra-Credit/issues/71) |
| 072 | [Download a report as CSV](072-download-a-report-as-csv.md) | Reports | 45 min | 070 | [#72](https://github.com/ifnidbi/Extra-Credit/issues/72) |
| 073 | [Download a report as a printable PDF table](073-download-a-report-as-a-printable-pdf-table.md) | Reports | 60 min | 072 | [#73](https://github.com/ifnidbi/Extra-Credit/issues/73) |
| 074 | [Find cities with the external geocoding API](074-find-cities-with-the-external-geocoding-api.md) | Weather | 45 min | 009 | [#74](https://github.com/ifnidbi/Extra-Credit/issues/74) |
| 075 | [Read one day's weather for a selected city](075-read-one-day-s-weather-for-a-selected-city.md) | Weather | 45 min | 074 | [#75](https://github.com/ifnidbi/Extra-Credit/issues/75) |
| 076 | [Store and retrieve pickup weather snapshots](076-store-and-retrieve-pickup-weather-snapshots.md) | Weather | 60 min | 015, 023, 037, 075 | [#76](https://github.com/ifnidbi/Extra-Credit/issues/76) |
| 077 | [Build the pickup-weather page](077-build-the-pickup-weather-page.md) | Weather | 45 min | 042, 076 | [#77](https://github.com/ifnidbi/Extra-Credit/issues/77) |
| 078 | [Build isolated integration test fixtures](078-build-isolated-integration-test-fixtures.md) | Verification | 60 min | 016, 023, 026, 068 | [#78](https://github.com/ifnidbi/Extra-Credit/issues/78) |
| 079 | [Test signup, sessions, and account roles](079-test-signup-sessions-and-account-roles.md) | Verification | 45 min | 043, 078 | [#79](https://github.com/ifnidbi/Extra-Credit/issues/79) |
| 080 | [Test listing CRUD and search behavior](080-test-listing-crud-and-search-behavior.md) | Verification | 60 min | 050, 054, 056, 078 | [#80](https://github.com/ifnidbi/Extra-Credit/issues/80) |
| 081 | [Test inquiry decisions and transaction rollback](081-test-inquiry-decisions-and-transaction-rollback.md) | Verification | 60 min | 066, 078 | [#81](https://github.com/ifnidbi/Extra-Credit/issues/81) |
| 082 | [Test gallery uploads, visibility, and cleanup](082-test-gallery-uploads-visibility-and-cleanup.md) | Verification | 45 min | 061, 078 | [#82](https://github.com/ifnidbi/Extra-Credit/issues/82) |
| 083 | [Test report tables and both downloads](083-test-report-tables-and-both-downloads.md) | Verification | 60 min | 071, 073, 078 | [#83](https://github.com/ifnidbi/Extra-Credit/issues/83) |
| 084 | [Test weather without depending on the live API](084-test-weather-without-depending-on-the-live-api.md) | Verification | 45 min | 077, 078 | [#84](https://github.com/ifnidbi/Extra-Credit/issues/84) |
| 085 | [Walk through the app and its error states](085-walk-through-the-app-and-its-error-states.md) | Verification | 60 min | 045, 050, 061, 067, 070, 077, 078 | [#85](https://github.com/ifnidbi/Extra-Credit/issues/85) |
| 086 | [Measure query performance with EXPLAIN](086-measure-query-performance-with-explain.md) | Verification | 60 min | 054, 068, 076, 078 | [#86](https://github.com/ifnidbi/Extra-Credit/issues/86) |
| 087 | [Write and verify a fresh-install README](087-write-and-verify-a-fresh-install-readme.md) | Delivery | 60 min | 016, 061, 067, 073, 077, 078 | [#87](https://github.com/ifnidbi/Extra-Credit/issues/87) |
| 088 | [Capture query results and screenshots](088-capture-query-results-and-screenshots.md) | Delivery | 60 min | 070, 072, 073, 076, 085 | [#88](https://github.com/ifnidbi/Extra-Credit/issues/88) |
| 089 | [Draft the final report's problem and design sections](089-draft-the-final-report-s-problem-and-design-sections.md) | Delivery | 60 min | 007, 027, 030, 033 | [#89](https://github.com/ifnidbi/Extra-Credit/issues/89) |
| 090 | [Draft the final report's implementation and results](090-draft-the-final-report-s-implementation-and-results.md) | Delivery | 60 min | 083, 084, 086, 088 | [#90](https://github.com/ifnidbi/Extra-Credit/issues/90) |
| 091 | [Assemble and proofread the final report](091-assemble-and-proofread-the-final-report.md) | Delivery | 60 min | 089, 090 | [#91](https://github.com/ifnidbi/Extra-Credit/issues/91) |
| 092 | [Build the presentation slides](092-build-the-presentation-slides.md) | Delivery | 60 min | 008, 085, 088 | [#92](https://github.com/ifnidbi/Extra-Credit/issues/92) |
| 093 | [Rehearse and defend the demo](093-rehearse-and-defend-the-demo.md) | Delivery | 45 min | 085, 087, 091, 092 | [#93](https://github.com/ifnidbi/Extra-Credit/issues/93) |
| 094 | [Check course deliverables and team evaluation](094-check-course-deliverables-and-team-evaluation.md) | Delivery | 30 min | 091, 093 | [#94](https://github.com/ifnidbi/Extra-Credit/issues/94) |
