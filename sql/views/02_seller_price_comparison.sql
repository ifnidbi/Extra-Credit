-- Compare each seller's average to at least one category average in the same currency.
CREATE OR REPLACE VIEW v_seller_price_comparison AS
SELECT s.student_id, s.full_name AS seller_name, l.currency_code,
       COUNT(*) AS listing_count, ROUND(AVG(l.price), 2) AS average_price
FROM Students s JOIN Listings l ON l.seller_id = s.student_id
GROUP BY s.student_id, s.full_name, l.currency_code
HAVING AVG(l.price) > ANY (
    SELECT AVG(other.price)
    FROM Listings other
    WHERE other.currency_code = l.currency_code
    GROUP BY other.category_id
);
