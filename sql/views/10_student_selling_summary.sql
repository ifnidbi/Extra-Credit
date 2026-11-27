-- Count each student's listings by status, including students with zero listings.
CREATE OR REPLACE VIEW v_student_selling_summary AS
SELECT s.student_id, s.full_name, COUNT(l.listing_id) AS total_listings,
       SUM(CASE WHEN l.listing_status = 'Available' THEN 1 ELSE 0 END) AS available_listings,
       SUM(CASE WHEN l.listing_status = 'Sold' THEN 1 ELSE 0 END) AS sold_listings
FROM Students s LEFT JOIN Listings l ON l.seller_id = s.student_id
GROUP BY s.student_id, s.full_name;
