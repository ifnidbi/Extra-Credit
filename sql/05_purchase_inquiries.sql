CREATE TABLE IF NOT EXISTS Purchase_Inquiries (
    inquiry_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    listing_id INT UNSIGNED NOT NULL,
    buyer_id INT UNSIGNED NOT NULL,
    pickup_location VARCHAR(150) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    preferred_date DATE NOT NULL,
    inquiry_status ENUM('Pending','Accepted','Declined','Withdrawn') NOT NULL DEFAULT 'Pending',
    submitted_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (listing_id) REFERENCES Listings(listing_id) ON UPDATE CASCADE,
    FOREIGN KEY (buyer_id) REFERENCES Students(student_id) ON UPDATE CASCADE
) ENGINE=InnoDB;
