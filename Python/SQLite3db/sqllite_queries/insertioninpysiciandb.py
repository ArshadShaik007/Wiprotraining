import sqlite3

connection=sqlite3.Connection('pysician.db')
cursor_obj=connection.cursor()

cursor_obj.execute("""insert into physician(empId,name,position,snn) values(4,"cox","seniow interniens",44444444)""")
cursor_obj.execute("""insert into physician(empId,name,position,snn) values(5,"bob","head chief",55555555)""")
cursor_obj.execute("""insert into physician(empId,name,position,snn) values(6,"tod","surgrical atendee",66666666)""")
cursor_obj.execute("""insert into physician(empId,name,position,snn) values(7,"wen","surgrical atendee",77777777)""")
cursor_obj.execute("""insert into physician(empId,name,position,snn) values(8,"keith","md resident",88888888)""")
cursor_obj.execute("""insert into physician(empId,name,position,snn) values(9,"molly","atd phys",99999999)""")

connection.commit()