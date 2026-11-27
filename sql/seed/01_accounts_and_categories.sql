INSERT INTO Students (student_id, full_name, email, password_hash, school_name, role, is_active) VALUES
(1, 'Alex Morgan', 'alex@example.com', 'disabled-until-seeded', 'Lakeview College', 'user', TRUE),
(2, 'Priya Shah', 'priya@example.com', 'disabled-until-seeded', 'Lakeview College', 'user', TRUE),
(3, 'Jordan Lee', 'jordan@example.com', 'disabled-until-seeded', 'Northfield Institute', 'user', TRUE),
(4, 'Maya Chen', 'maya@example.com', 'disabled-until-seeded', 'Brookside University', 'user', TRUE),
(5, 'Omar Hassan', 'omar@example.com', 'disabled-until-seeded', 'Northfield Institute', 'user', FALSE),
(6, 'Sofia Patel', 'admin@example.com', 'disabled-until-seeded', 'Lakeview College', 'admin', TRUE);

INSERT INTO Categories (category_id, category_name) VALUES
(1,'Textbooks'), (2,'Electronics'), (3,'Furniture'), (4,'Clothing'),
(5,'Sports Equipment'), (6,'School Supplies');
