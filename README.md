# house-price-prediction
Dockerized 3-tier house price estimation application deployed on AWS EC2















docker run -d \
  --name house-price-mysql \
  -e MYSQL_ROOT_PASSWORD=rootpassword \
  -e MYSQL_DATABASE=house_db \
  -e MYSQL_USER=houseuser \
  -e MYSQL_PASSWORD=housepassword \
  -v house_mysql_data:/var/lib/mysql \
  mysql:8.4

  MySQL ke andar login
  docker exec -it house-price-mysql mysql -uroot -prootpassword
  SHOW DATABASES;
  USE house_db;
  CREATE TABLE locations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(100) NOT NULL,
    rate_per_sqft DECIMAL(10,2) NOT NULL
);


CREATE TABLE predictions (
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

SELECT * FROM locations;
