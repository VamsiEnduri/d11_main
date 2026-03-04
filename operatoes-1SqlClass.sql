
create table products(
id int primary key auto_increment,
name varchar(50) not null,
category varchar(20) not null,
brand varchar(20) not null,
price decimal(10,2) not null check(price>=0),
stock_q int not null check(stock_q>=0),
is_available boolean default True ,
rating decimal(2,1) check (rating between 0 and 5),
description text
);


INSERT INTO products (name, category, brand, price, stock_q, is_available, rating, description)
VALUES
('Galaxy S23', 'Electronics', 'Samsung', 74999.00, 20, TRUE, 4.6, 'Flagship Samsung smartphone'),

('Samsung Smart TV 55', 'Electronics', 'Samsung', 62000.00, 10, TRUE, 4.5, '55 inch 4K UHD Smart TV'),

('Samsung Refrigerator', 'Appliances', 'Samsung', 35000.00, 8, TRUE, 4.4, 'Double door energy efficient refrigerator'),

('iPhone 14', 'Electronics', 'Apple', 79999.00, 15, TRUE, 4.8, 'Latest Apple smartphone'),

('MacBook Air M2', 'Electronics', 'Apple', 105000.00, 7, TRUE, 4.7, 'Lightweight Apple laptop with M2 chip'),

('Air Jordan Shoes', 'Footwear', 'Nike', 5999.00, 30, TRUE, 4.3, 'Comfortable sports shoes'),

('Gaming Laptop', 'Electronics', 'Asus', 95000.00, 5, TRUE, 4.7, 'High performance gaming laptop'),

('Bluetooth Speaker', 'Electronics', 'JBL', 3499.00, 25, TRUE, 4.2, 'Portable wireless speaker'),

('Office Chair', 'Furniture', 'Ikea', 8999.00, 12, TRUE, 4.1, 'Ergonomic office chair'),

('Backpack', 'Accessories', 'Skybags', 1499.00, 60, TRUE, 3.9, 'Durable travel backpack');




-- Get all products whose price is greater than 50,000.
select *
from products
where price>50000;

-- Get all products where brand is 'Samsung' AND price is greater than 30,000.
select *
from products
where brand ="Samsung" and price > 30000;

-- Get all products where category is 'Electronics' OR category is 'Appliances'.
select *
from products
where category="Electronics" or category = "Appliances";

-- Get all products whose price is between 3,000 and 10,000.
select *
from products
where price >=3000 and price <=10000;

-- Get all products where brand is either 'Apple' or 'Samsung'.

select *
from products
where brand = "Apple" or brand = "Samsung";

-- Get all products where the price is greater than 30,000 AND the rating is greater than 4.5.
select *
from products
where price > 30000 and rating > 4.5;

-- Get all products where the brand is NOT 'Samsung' AND the stock quantity is less than 20.
select *
from products
where brand = "Samsung" and stock_q <20;

-- Get all products where the price is between 3,000 and 80,000 AND the category is 'Electronics'.
select *
from products
where ( price >3000 and price <80000) and category ="Electronics";

-- Get all products where the brand is 'Apple' OR the rating is greater than or equal to 4.7.
select *
from products
where brand = "Apple" or rating >=4.7;


-- Get all products where the price is greater than 10,000 AND (brand is 'Samsung' OR brand is 'Apple').
select *
from products
where price > 10000 and (brand = "Samsung" or brand = "Apple");

-- 1️ Get all products where the price is greater than 30,000 AND stock quantity is less than 15 OR rating is greater than 4.5.
select *
from products
where (price > 30000 and stock_q <=15 ) or rating >4.5;

-- Get all products where the brand is not 'Apple' AND not 'Samsung' AND price is between 1,000 and 50,000.
select *
from products
where ( brand !="Apple" and brand != "Samsung")  and ( price >10000 and price <50000 );

-- Get all products where rating is greater than 4.0 AND price is less than 80,000 OR stock quantity is greater than 25.
select *
from products
where ( rating >4.0 and price <80000 )  or stock_q>=25;

 -- Get all products where the category is 'Electronics' AND price is greater than 50,000 OR category is 'Appliances' AND rating is greater than 4.3.
 select *
 from products 
 where (category = "Electronics" and price >50000) or(category = "Appliances" and rating >4.5);
 
 -- Get all products where price is greater than 10,000 AND stock quantity is not between 5 and 20 AND brand is either 'Samsung' or 'Apple'.
 select *
 from products
 where price >10000 and stock_q 