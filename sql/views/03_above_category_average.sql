-- Find items priced above their own category and currency average.
CREATE OR REPLACE VIEW v_above_category_average AS
SELECT l.listing_id, l.title, c.category_name, l.price, l.currency_code
FROM Listings l JOIN Categories c ON c.category_id = l.category_id
WHERE l.price > (
    SELECT AVG(other.price) FROM Listings other
    WHERE other.category_id = l.category_id AND other.currency_code = l.currency_code
);
