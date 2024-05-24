# create a connection to database
import sqlite3

connection = sqlite3.Connection('employee.db')

#create cursor

cursor_obj = connection.cursor()

#create table

# insert into tabel

cursor_obj.execute("""insert into employee(
        empname,
        empid,
        empsal) values("afsar",1,20000)""")
cursor_obj.execute("""insert into employee(
        empname,
        empid,
        empsal) values("arshad",1,35000)""")
cursor_obj.execute("""insert into employee(
        empname,
        empid,
        empsal) values("sami",1,30000)""")
cursor_obj.execute("""insert into employee(
        empname,
        empid,
        empsal) values("sahil",1,25000)""")
cursor_obj.execute("""insert into employee(
        empname,
        empid,
        empsal) values("loki",1,26000)""")

cursor=cursor_obj.execute("""select * from employee""")

for row in cursor:
    print(row)

connection.commit()
connection.close()