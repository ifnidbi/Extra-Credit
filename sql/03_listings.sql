CREATE TABLE IF NOT EXISTS Listings (
    listing_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    seller_id INT UNSIGNED NOT NULL,
    category_id INT UNSIGNED NOT NULL,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    currency_code CHAR(3) NOT NULL CHECK (currency_code IN ('CAD','USD','EUR','GBP','JPY')),
    item_condition ENUM('New','Like New','Good','Fair','Poor') NOT NULL,
    listing_status ENUM('Available','Reserved','Sold','Removed') NOT NULL DEFAULT 'Available',
    campus_name VARCHAR(150) NOT NULL,
    date_posted DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (currency_code <> 'JPY' OR price = FLOOR(price)),
    INDEX idx_listing_status_currency_date (listing_status, currency_code, date_posted, listing_id),
    FOREIGN KEY (seller_id) REFERENCES Students(student_id) ON UPDATE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON UPDATE CASCADE
) ENGINE=InnoDB;
