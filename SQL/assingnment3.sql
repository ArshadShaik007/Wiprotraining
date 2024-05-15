/*
The ACID properties are
1.Atomicity
2.Concurrency
3.Isolation
*/
create database assignment3;
use assignment3;
start transaction;
create table books(
book_id int primary key,
title varchar(50) not null,
author varchar(50) not null,genre varchar(50),publication_year varchar(5),availability varchar(15) not null);
lock tables books write;
insert into books values(1,'telugu','sunny','lang','2021','yes'),(2,'hindi','arshad','lang','2011','no'),(3,'math','rash','sub','2022','yes');
commit;
start transaction;
select * from books;