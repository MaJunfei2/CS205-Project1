import sqlite3
import csv

f1=open('Table-CarMake.csv','r') 
next(f1, None) 
reader = csv.reader(f1)

sql = sqlite3.connect('car.db')
sql.text_factory = str
cur = sql.cursor()
		 
for row in reader:
	cur.execute("INSERT INTO CarMake VALUES (?,?,?)", row)

f2=open('Table-Model.csv','r') 
next(f2, None) 
reader = csv.reader(f2)

for row in reader:
	cur.execute("INSERT INTO Model VALUES (?,?,?,?,?,?,?,?)", row)
	
f1.close()
f2.close
sql.commit()
sql.close()
