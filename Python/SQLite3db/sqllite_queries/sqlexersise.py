# create a connection to database
import sqlite3

connection = sqlite3.Connection('studentrepo.db')

#create cursor

cursor_obj = connection.cursor()

#updating the marks of arnold
# cursor_obj.execute("""update students set Mark = 70 where Name="arnold" """)

#deleting the rocord of the tesqry
#cursor_obj.execute("""delete from students where Name ="tesqruey" """)

#Ascending order
asc = cursor_obj.execute(""" select * from students order by Mark ASC""")
print("Ascending")
for row in asc:
    print(row)
#Decending order
desc = cursor_obj.execute(""" select * from students order by Mark DESC""")
print("Decending")
for row in desc:
    print(row)

cursor_obj.execute(""" select * from students order by Mark DESC LIMIT 1""")
result = cursor_obj.fetchall()
print("Higest marks: ", result[0])

cursor_obj.execute(""" select * from students order by Mark ASC LIMIT 1""")
result = cursor_obj.fetchall()
print("Lowest marks: ", result[0])

girls = cursor_obj.execute(""" select * from students where gender ="female" """)
for row in girls:
    print(row)

cursor_obj.execute(""" select count(*) from students where gender ="female" """)
result = cursor_obj.fetchone()
print("total girls", result[0])
connection.commit()