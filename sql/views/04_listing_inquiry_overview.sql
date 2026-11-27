-- MySQL full outer join equivalent. The foreign key prevents unmatched inquiries.
CREATE OR REPLACE VIEW v_listing_inquiry_overview AS
SELECT l.listing_id, l.title, l.listing_status, p.inquiry_id, p.buyer_id, p.inquiry_status
FROM Listings l LEFT JOIN Purchase_Inquiries p ON p.listing_id = l.listing_id
UNION ALL
SELECT l.listing_id, l.title, l.listing_status, p.inquiry_id, p.buyer_id, p.inquiry_status
FROM Listings l RIGHT JOIN Purchase_Inquiries p ON p.listing_id = l.listing_id
WHERE l.listing_id IS NULL;
