INSERT INTO Listing_Images (listing_id, image_path) VALUES
(1,'sample-textbook.jpg'), (1,'sample-back.jpg'), (2,'sample-mouse.jpg'),
(3,'sample-desk.jpg'), (4,'sample-jacket.jpg'), (5,'sample-ball.jpg'), (6,'sample-monitor.jpg');

INSERT INTO Purchase_Inquiries (inquiry_id, listing_id, buyer_id, pickup_location, payment_method,
    preferred_date, inquiry_status, submitted_at) VALUES
(1,1,2,'Campus Library','Cash','2026-11-10','Pending','2026-11-07 09:00:00'),
(2,1,3,'Shawenjigewining Hall','E-transfer','2026-11-11','Pending','2026-11-07 10:00:00'),
(3,2,4,'Campus Library','Cash','2026-11-10','Pending','2026-11-07 11:00:00'),
(4,3,5,'Charles Hall','E-transfer','2026-11-12','Accepted','2026-11-07 12:00:00'),
(5,3,1,'Charles Hall','Cash','2026-11-12','Declined','2026-11-07 13:00:00'),
(6,4,1,'Bordessa Hall','E-transfer','2026-11-06','Accepted','2026-11-05 14:00:00'),
(7,6,2,'Campus Library','E-transfer','2026-11-13','Pending','2026-11-08 15:00:00'),
(8,5,4,'Bordessa Hall','Cash','2026-11-11','Withdrawn','2026-11-08 16:00:00');
