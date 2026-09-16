CREATE DATABASE IF NOT EXISTS house_db;

USE house_db;

CREATE TABLE IF NOT EXISTS locations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL,
    rate_per_sqft DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(100),
    area INT,
    bedrooms INT,
    bathrooms INT,
    parking INT,
    property_age INT,
    estimated_price DECIMAL(15,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO locations (location_name, rate_per_sqft)
VALUES
('Delhi', 5000),
('Noida', 4000),
('Gurgaon', 7000),
('Ghaziabad', 3000);
