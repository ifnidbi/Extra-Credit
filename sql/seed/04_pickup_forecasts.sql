-- Fictional history for the demo. Live lookups are saved separately by the app.
INSERT INTO Pickup_Forecasts (student_id, place_label, latitude, longitude, forecast_date,
    max_temp_c, precip_probability, fetched_at) VALUES
(3,'Vancouver, Canada (sample)',49.2827,-123.1207,'2026-11-04',12.00,65,'2026-11-04 12:30:00'),
(3,'Boston, United States (sample)',42.3601,-71.0589,'2026-11-05',11.50,25,'2026-11-05 13:15:00'),
(3,'Dublin, Ireland (sample)',53.3498,-6.2603,'2026-11-06',13.25,55,'2026-11-06 13:30:00'),
(4,'Paris, France (sample)',48.8566,2.3522,'2026-11-07',14.00,30,'2026-11-07 14:00:00'),
(4,'Tokyo, Japan (sample)',35.6762,139.6503,'2026-11-08',17.75,15,'2026-11-08 14:30:00'),
(4,'Madrid, Spain (sample)',40.4168,-3.7038,'2026-11-09',16.00,10,'2026-11-09 15:00:00');
