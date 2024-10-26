CREATE DATABASE Retail;
USE Retail;

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    stock_level INT,
    total_sales INT
);

select * from products;

