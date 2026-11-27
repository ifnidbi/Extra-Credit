-- Fictional history for the demo. Live lookups are saved separately by the app.
INSERT INTO Pickup_Forecasts (student_id, place_label, latitude, longitude, forecast_date,
    max_temp_c, precip_probability, fetched_at) VALUES
(3,'Oshawa, Ontario (sample)',43.9001,-78.8496,'2026-11-04',12.00,65,'2026-11-04 12:30:00'),
(3,'Oshawa, Ontario (sample)',43.9001,-78.8496,'2026-11-05',11.50,25,'2026-11-05 13:15:00'),
(3,'Oshawa, Ontario (sample)',43.9001,-78.8496,'2026-11-06',13.25,55,'2026-11-06 13:30:00'),
(4,'Oshawa, Ontario (sample)',43.9001,-78.8496,'2026-11-07',14.00,30,'2026-11-07 14:00:00'),
(4,'Oshawa, Ontario (sample)',43.9001,-78.8496,'2026-11-08',17.75,15,'2026-11-08 14:30:00'),
(4,'Oshawa, Ontario (sample)',43.9001,-78.8496,'2026-11-09',16.00,10,'2026-11-09 15:00:00');
