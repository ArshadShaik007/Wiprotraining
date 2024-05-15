#assignment 1
create database emart;
use emart;
create table user_ac(usr_id varchar(50),usr_name varchar(50),emaiil varchar(100),pss varchar(50),address varchar(150),post_add varchar(150),pay_info varchar(25));
create table product(prod_id varchar(50),prod_name varchar(50),prod_desc varchar(200),prodprice int,category varchar(150),image varchar(150),review varchar(225),primary key(prod_id));
create table shp_cart(cart_id varchar(20),user_id varchar(50), product_id varchar(50),status varchar(20),quantity int,primary key(cart_id));
alter table user_ac add primary key(usr_id)