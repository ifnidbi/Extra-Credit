-- List items alongside the seller and category.
CREATE OR REPLACE VIEW v_listing_details AS
SELECT l.listing_id, l.title, s.full_name AS seller_name, c.category_name,
       l.price, l.currency_code, l.item_condition, l.listing_status
FROM Listings l
JOIN Students s ON s.student_id = l.seller_id
JOIN Categories c ON c.category_id = l.category_id;
