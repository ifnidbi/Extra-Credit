-- Count items and average prices without mixing currencies or hiding empty categories.
CREATE OR REPLACE VIEW v_category_summary AS
SELECT c.category_id, c.category_name, l.currency_code,
       COUNT(l.listing_id) AS listing_count, ROUND(AVG(l.price), 2) AS average_price
FROM Categories c LEFT JOIN Listings l ON l.category_id = c.category_id
GROUP BY c.category_id, c.category_name, l.currency_code;
