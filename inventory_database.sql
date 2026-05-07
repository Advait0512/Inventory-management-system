CREATE DATABASE inventory_db;

USE inventory_db;

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    quantity INT,
    price DECIMAL(10,2),
    threshold INT
);

select * from products

INSERT INTO products (name, quantity, price, threshold) VALUES
('Milk', 50, 30, 10),
('Bread', 40, 25, 10),
('Butter', 20, 50, 5),
('Cheese', 15, 80, 5),
('Eggs', 100, 6, 20),
('Rice', 200, 60, 50),
('Wheat', 150, 45, 30),
('Sugar', 80, 40, 20),
('Salt', 60, 20, 15),
('Oil', 70, 120, 20);

select * from products



