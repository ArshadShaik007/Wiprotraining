import sqlite3

connection = sqlite3.Connection('studentrepo.db')
cursor_obj = connection.cursor()

# create table

cursor_obj.execute("""
CREATE TABLE students(
Id int primary key,
Name varchar(255) not null,
Class varchar(100) not null,
Mark int,
Gender varchar(50))
""")

connection.commit()