CREATE TABLE IF NOT EXISTS Pickup_Forecasts (
    snapshot_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    student_id INT UNSIGNED NOT NULL,
    place_label VARCHAR(150) NOT NULL,
    latitude DECIMAL(7,4) NOT NULL CHECK (latitude BETWEEN -90 AND 90),
    longitude DECIMAL(7,4) NOT NULL CHECK (longitude BETWEEN -180 AND 180),
    forecast_date DATE NOT NULL,
    max_temp_c DECIMAL(5,2) NOT NULL,
    precip_probability TINYINT UNSIGNED NOT NULL CHECK (precip_probability <= 100),
    fetched_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON UPDATE CASCADE
) ENGINE=InnoDB;
