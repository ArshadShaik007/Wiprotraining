import mysql.connector

# connecing to database

database = mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="orcl",
                                   database="wipronewb")

# preparing cursor object

cursorobj=database.cursor()

cursorobj.execute("""insert into physician(empId,name,position,snn) values(1,"john","staff interniens",1111111)""")
cursorobj.execute("""insert into physician(empId,name,position,snn) values(2,"elliot",
"attending physician",22222222)""")
cursorobj.execute("""insert into physician(empId,name,position,snn) values(3,"chris","surgerical attendee",33333333)""")
cursorobj.execute("""insert into physician(empId,name,position,snn) values(4,"cox","seniow interniens",44444444)""")
cursorobj.execute("""insert into physician(empId,name,position,snn) values(5,"bob","head chief",55555555)""")
cursorobj.execute("""insert into physician(empId,name,position,snn) values(6,"tod","surgrical atendee",66666666)""")
cursorobj.execute("""insert into physician(empId,name,position,snn) values(7,"wen","surgrical atendee",77777777)""")
cursorobj.execute("""insert into physician(empId,name,position,snn) values(8,"keith","md resident",88888888)""")
cursorobj.execute("""insert into physician(empId,name,position,snn) values(9,"molly","atd phys",99999999)""")
cursorobj.execute("""insert into department(deparmentId,name,head) values(1,"genral medicine",4)""")
cursorobj.execute("""insert into department(deparmentId,name,head) values(2,"surgery",7)""")
cursorobj.execute("""insert into department(deparmentId,name,head) values(3,"psychiarty",9)""")

database.commit()