CREATE DATABASE trip_db;

USE trip_db;

CREATE TABLE trips (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

INSERT INTO trips (name, location, price) VALUES 
('Trip A', 'Location A', 100.00),
('Trip B', 'Location B', 200.00),
('Trip C', 'Location C', 300.00);
