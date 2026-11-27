INSERT INTO Students (student_id, full_name, email, password_hash, school_name, role, is_active, email_verified) VALUES
(1, 'Alex Morgan', 'alex@example.com', 'disabled-until-seeded', 'Ontario Tech University', 'user', TRUE, TRUE),
(2, 'Priya Shah', 'priya@example.com', 'disabled-until-seeded', 'Ontario Tech University', 'user', TRUE, TRUE),
(3, 'Jordan Lee', 'jordan@example.com', 'disabled-until-seeded', 'Ontario Tech University', 'user', TRUE, TRUE),
(4, 'Maya Chen', 'maya@example.com', 'disabled-until-seeded', 'Ontario Tech University', 'user', TRUE, TRUE),
(5, 'Omar Hassan', 'omar@example.com', 'disabled-until-seeded', 'Ontario Tech University', 'user', FALSE, TRUE),
(6, 'Sofia Patel', 'admin@example.com', 'disabled-until-seeded', 'Ontario Tech University', 'admin', TRUE, TRUE);

INSERT INTO Categories (category_id, category_name) VALUES
(1,'Textbooks'), (2,'Electronics'), (3,'Furniture'), (4,'Clothing'),
(5,'Sports Equipment'), (6,'School Supplies');
