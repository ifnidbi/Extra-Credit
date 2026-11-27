# Catalog query performance

The test used MySQL 8.4.11 on a local macOS socket. The database held the nine sample listings and 5,000 synthetic listings. Each synthetic listing used one of four sellers, one of five currencies, and price `n % 150`. One in four was Available. Posting times increased by one minute per row. The synthetic listings used North Oshawa.

The test used the app's listing query with Available state, an active and confirmed Ontario Tech seller, either Ontario Tech campus, CAD, and prices from 20 to 100. It sorted by posting time and listing ID, newest first, and fetched up to 51 results to tell whether there is a next page. Both plans returned the same listing IDs in the same order.

| Measurement | Before index | After index |
| --- | --- | --- |
| Join order | Students, Listings, Categories | Students, Listings, Categories |
| Listings access | `ref` using the `seller_id` foreign-key index | `ref` using the status, currency, date, and ID index |
| Sorting in EXPLAIN | Temporary table and filesort | Temporary table and filesort |
| Estimated Listings rows for each lookup | 983 | 254 |
| Median over 20 warm local reads | 4.199 ms | 1.835 ms |
| Range over those reads | 4.063–4.621 ms | 1.710–6.272 ms |

The measurement includes Connector/Python fetching the rows over the local socket. This is one synthetic workload. Both plans still sort. The new plan selects fewer listing candidates using the index. The index also takes storage and adds work to inserts and updates. The price condition is still applied after choosing matching status and currency records. The [Listings schema](../sql/03_listings.sql) includes the tested index.

## Reproduce

Create a separate disposable schema and load the schema and fictional seed. Generate the same 5,000 rows and run the query below. For the baseline, remove `idx_listing_status_currency_date` from the disposable schema. Run `ANALYZE TABLE Listings`, `EXPLAIN`, and 20 warmed reads. Recreate the index, refresh statistics, rerun the checks, and compare returned IDs. Keep that experiment out of the development database.

```sql
EXPLAIN SELECT l.listing_id, l.title, l.description, l.category_id, c.category_name,
       l.campus_name, l.price, l.currency_code, l.item_condition, l.listing_status,
       l.date_posted, l.seller_id, s.full_name AS seller_name, s.is_active AS seller_active
FROM Listings l
JOIN Students s ON s.student_id = l.seller_id
JOIN Categories c ON c.category_id = l.category_id
WHERE l.listing_status = 'Available' AND s.is_active AND s.email_verified
  AND s.school_name = 'Ontario Tech University'
  AND (SUBSTRING_INDEX(s.email, '@', -1) = 'ontariotechu.net'
       OR s.email IN ('alex@example.com', 'priya@example.com', 'jordan@example.com',
                      'maya@example.com', 'omar@example.com', 'admin@example.com'))
  AND l.campus_name IN ('North Oshawa', 'Downtown Oshawa')
  AND l.currency_code = 'CAD'
  AND l.price >= 20 AND l.price <= 100
ORDER BY l.date_posted DESC, l.listing_id DESC
LIMIT 51 OFFSET 0;
```
