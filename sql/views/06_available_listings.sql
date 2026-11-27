-- Show information about available items for the admin report.
CREATE OR REPLACE VIEW v_available_listings AS
SELECT l.listing_id, l.title, c.category_name, l.price, l.currency_code, l.item_condition,
       s.full_name AS seller_name, s.email AS seller_email
FROM Listings l
JOIN Categories c ON c.category_id = l.category_id
JOIN Students s ON s.student_id = l.seller_id
WHERE l.listing_status = 'Available';
