import mysql.connector

# connecing to database

database = mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="orcl",
                                   database="wipronewb")

# preparing cursor object

cursorobj = database.cursor()

print("inner join")
cursorobj.execute("""select p.name, p.position, d.name from physician as p inner join department as d 
on p.empId=d.head""")
for row in cursorobj:
    print(row)

print("left join")
cursorobj.execute("""select p.name, p.position, d.name from physician as p left join department as d 
on p.empId=d.head""")
for row in cursorobj:
    print(row)

print("right join")
cursorobj.execute("""select p.name, p.position, d.name from physician as p right join department as d 
on p.empId=d.head""")

for row in cursorobj:
    print(row)

database.commit()
