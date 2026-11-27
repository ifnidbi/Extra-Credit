-- Include anyone who has posted a listing or sent an inquiry.
CREATE OR REPLACE VIEW v_active_students AS
SELECT student_id, full_name, email FROM Students
WHERE student_id IN (
    SELECT seller_id FROM Listings
    UNION
    SELECT buyer_id FROM Purchase_Inquiries
);
