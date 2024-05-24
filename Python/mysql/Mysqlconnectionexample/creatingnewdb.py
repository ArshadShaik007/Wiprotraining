import mysql.connector

# connecing to database

database = mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="orcl",
                                   database="wipronewb")

# preparing cursor object

cursorobj=database.cursor()

cursorobj.execute("""create table physician(empId int primary key, name varchar(255),position varchar(255),snn int)""")
cursorobj.execute("""create table department(deparmentId int primary key, name varchar(255),head int)""")



database.commit()