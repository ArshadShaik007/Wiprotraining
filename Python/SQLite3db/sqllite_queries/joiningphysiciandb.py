import sqlite3

connection=sqlite3.Connection('pysician.db')
cursor_obj=connection.cursor()

innerjoin = cursor_obj.execute("""select p.name, p.position, d.name from physician as p inner join department as d 
on p.empId=d.head""")

for row in innerjoin:
    print(row)

leftjoin = cursor_obj.execute("""select p.name, p.position, d.name from physician as p left join department as d 
on p.empId=d.head""")

for row in leftjoin:
    print(row)

rightjoin = cursor_obj.execute("""select p.name, p.position, d.name from physician as p right join department as d 
on p.empId=d.head""")

for row in rightjoin:
    print(row)

fulljoin = cursor_obj.execute("""select p.name, p.position, d.name from physician as p full join department as d 
on p.empId=d.head""")

for row in fulljoin:
    print(row)
connection.commit()