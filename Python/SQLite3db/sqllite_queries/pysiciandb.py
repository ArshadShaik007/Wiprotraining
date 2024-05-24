import sqlite3

connection=sqlite3.Connection('pysician.db')
cursor_obj=connection.cursor()

cursor_obj.execute("""create table physician(empId int primary key, name varchar,position varchar(255),snn int);""")
cursor_obj.execute("""create table department(deparmentId int primary key, name varchar(255),head int);""")

