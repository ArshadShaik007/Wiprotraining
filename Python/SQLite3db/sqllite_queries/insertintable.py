import sqlite3

connection = sqlite3.Connection('studentrepo.db')
cursor_obj = connection.cursor()
# insert into table

cursor_obj.execute("""
INSERT INTO students(
Id,Name,Class,Mark,Gender) values(1,"jhon deo","four",75,"female")
""")

cursor_obj.execute("""
INSERT INTO students(
Id,Name,Class,Mark,Gender) values(2,"max ruin","three",85,"male")
""")

cursor_obj.execute("""
INSERT INTO students(
Id,Name,Class,Mark,Gender) values(3,"arnold","theree",55,"male")
""")

cursor_obj.execute("""
INSERT INTO students(
Id,Name,Class,Mark,Gender) values(4,"krish star","four",60,"female")
""")

cursor_obj.execute("""
INSERT INTO students(
Id,Name,Class,Mark,Gender) values(5,"jhon mike","four",60,"female")
""")

cursor_obj.execute("""
INSERT INTO students(
Id,Name,Class,Mark,Gender) values(6,"alex jhon","four",65,"male")
""")

cursor_obj.execute("""
INSERT INTO students(
Id,Name,Class,Mark,Gender) values(7,"my jhon rob","five",78,"male")
""")

cursor_obj.execute("""
INSERT INTO students(
Id,Name,Class,Mark,Gender) values(8,"asuruid","five",85,"male")
""")

cursor_obj.execute("""
INSERT INTO students(
Id,Name,Class,Mark,Gender) values(9,"tesqruey","six",78,"male")
""")
cursor_obj.execute("""
INSERT INTO students(
Id,Name,Class,Mark,Gender) values(10,"big john","four",65,"female")
""")

cursor=cursor_obj.execute("""select * from students""")

for row in cursor:
    print(row)
connection.commit()
