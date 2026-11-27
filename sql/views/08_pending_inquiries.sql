-- List the pickup plans still waiting for a seller's reply.
CREATE OR REPLACE VIEW v_pending_inquiries AS
SELECT p.inquiry_id, l.title AS listing_title, buyer.full_name AS buyer_name,
       seller.full_name AS seller_name, p.pickup_location, p.preferred_date
FROM Purchase_Inquiries p
JOIN Listings l ON l.listing_id = p.listing_id
JOIN Students buyer ON buyer.student_id = p.buyer_id
JOIN Students seller ON seller.student_id = l.seller_id
WHERE p.inquiry_status = 'Pending';
