-- Find available listings without a linked photo.
CREATE OR REPLACE VIEW v_available_without_images AS
SELECT l.listing_id, l.title, s.full_name AS seller_name, l.price, l.currency_code
FROM Listings l JOIN Students s ON s.student_id = l.seller_id
WHERE l.listing_status = 'Available'
AND NOT EXISTS (SELECT 1 FROM Listing_Images i WHERE i.listing_id = l.listing_id);
