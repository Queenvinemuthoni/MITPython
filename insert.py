import sqlite3
conn=sqlite3.connect('MITmidmorning')
print("Open database successfully")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(7,'Mary',18,'eMobilis','Female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(8,'Ezra',20,'eMobilis','Male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(9,'Masika',19,'eMobilis','Female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(10,'Chris',18,'eMobilis','Male')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(11,'Makena',20,'eMobilis','Female')")
conn.execute("INSERT INTO Wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES(12,'Makani',19,'eMobilis','Female')")

conn.commit()
print("records added successfully")
conn.close()