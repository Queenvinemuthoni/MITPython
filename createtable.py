import sqlite3
conn=sqlite3.connect('MITmidmorning')
print("Open database successfully")
conn.execute("CREATE TABLE Wanafunzi("
             "ID INT PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "AGE INT NOT NULL,"
             "SCHOOL TEXT NOT NULL,"
             "GENDER TEXT NOT NULL)")
print("Table created successfully")
conn.close()
