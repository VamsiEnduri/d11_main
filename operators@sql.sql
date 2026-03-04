use d11__;

create table products(
id int primary key,
name varchar(50) not null,
category varchar(30) not null,
brand varchar(20) not null,
price decimal(8,2) not null check(price >=0),
stock int not null check(stock>=0),
is_available boolean default True,
rating decimal(2,1) not null check (rating>=1 and rating <=5),
description text
);

select *
from products;

insert into products(id,name,category,brand,price,stock,is_available,rating,description)
values (1,"Redmi 12 5G","Electronics","MI","12000.00",22,True,3.7,"redmi mobilewith 6.24inches length 128gb ram and 6g rom and snapdargon octocore");


insert into products (id, name, category, brand, price, stock, is_available, rating, description) values
(2, 'iPhone 14', 'Electronics', 'Apple', 79999.00, 15, true, 4.8, 'Latest Apple smartphone with A15 chip'),

(3, 'Galaxy S23', 'Electronics', 'Samsung', 74999.00, 20, true, 4.7, 'Samsung flagship smartphone'),

(4, 'Redmi Note 13', 'Electronics', 'Xiaomi', 17999.00, 35, true, 4.3, 'Budget friendly smartphone'),

(5, 'Air Conditioner 1.5 Ton', 'Appliances', 'LG', 42999.00, 10, true, 4.5, 'Energy efficient AC'),

(6, 'Refrigerator 260L', 'Appliances', 'Samsung', 28999.00, 8, true, 4.4, 'Double door refrigerator'),

(7, 'LED TV 55 inch', 'Electronics', 'Sony', 64999.00, 5, true, 4.6, 'Ultra HD Smart TV'),

(8, 'Washing Machine 7kg', 'Appliances', 'Whirlpool', 21999.00, 12, true, 4.2, 'Fully automatic washing machine'),

(9, 'MacBook Air M2', 'Computers', 'Apple', 114999.00, 7, true, 4.9, 'Lightweight laptop with M2 chip'),

(10, 'Inspiron 15', 'Computers', 'Dell', 58999.00, 14, true, 4.3, '15 inch performance laptop'),

(11, 'ThinkPad E14', 'Computers', 'Lenovo', 62999.00, 9, true, 4.5, 'Business series laptop'),

(12, 'Bluetooth Speaker', 'Accessories', 'JBL', 4999.00, 40, true, 4.4, 'Portable wireless speaker'),

(13, 'Smart Watch 5', 'Accessories', 'Apple', 39999.00, 18, true, 4.7, 'Advanced health tracking watch'),

(14, 'Gaming Mouse', 'Accessories', 'Logitech', 2499.00, 50, true, 4.3, 'High precision gaming mouse'),

(15, 'Office Chair', 'Furniture', 'Ikea', 8999.00, 22, true, 4.1, 'Ergonomic office chair'),

(16, 'Study Table', 'Furniture', 'UrbanWood', 11999.00, 16, true, 4.2, 'Wooden study table'),

(17, 'Mixer Grinder', 'Appliances', 'Philips', 3499.00, 30, true, 4.0, '3 jar mixer grinder'),

(18, 'Ceiling Fan', 'Appliances', 'Havells', 2999.00, 25, true, 4.1, 'Energy saving ceiling fan'),

(19, 'Tablet S9', 'Electronics', 'Samsung', 69999.00, 11, true, 4.6, 'High performance Android tablet'),

(20, 'DSLR Camera D7500', 'Electronics', 'Nikon', 84999.00, 6, true, 4.8, 'Professional DSLR camera');



-- Get all products where the price is greater than 50000.
select *
from products
where price >50000;

-- Get all products where the brand is equal to 'Apple'.
select *
from products
where brand="Apple";

-- Get all products where the stock is less than 10.
select *
from products
where stock <10;

-- Get all products where the rating is greater than or equal to 4.5.
select *
from products
where rating >=4.5;

-- Get all products where the category is not equal to 'Electronics'.


select *
from products
where category <> "Electronics";



-- > < >= <= = !=

-- and opeartor with conditions on single column 

-- Get all products where the price is greater than 20000 and less than 80000.
select *
from products
where price >20000 and price <80000;


select *
from products;

select *
from products
where price = 12000 and price =79999;


select *
from products
where brand= "Apple" and brand="Samsung";


select *
from products
where brand = "Apple" and price >45000;

select *
from products
where rating >4 and rating <5;





