import mysql.connector

# connecing to database

database = mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="orcl",
                                   database="wipromysql")

# preparing cursor object

cursor_obj=database.cursor()

cursor_obj.execute("""create table student(
name varchar(20) not null,
branch varchar(50),
roll int not null,
section varchar(50),
age int) """)

database.close()