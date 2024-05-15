create database assignment4;
use assignment4;
create table books(
book_id int primary key,
title varchar(50) not null,
author varchar(50) not null,genre varchar(50),publication_year varchar(5),availability varchar(15) not null);
create table students(stud_id int primary key, name varchar(50) not null,email varchar(50) unique);
create table issues(
issue_id int primary key,
book_id int unique,
stud_id int unique,issuedate varchar(25),foreign key(book_id) references books(book_id));
alter table issues add foreign key(stud_id) references students(stud_id);
alter table students add column(age int check (age>19));
#Assignment
create table students_1(stud_id int primary key, name varchar(50) not null,email varchar(50) unique);
alter table issues add column(returndate varchar(25));
drop table students_1