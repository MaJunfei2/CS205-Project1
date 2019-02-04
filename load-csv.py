import csv
import sqlite3

f1 = open('Table-CarMake.csv')
next(f1, None)
csv_f1 = csv.reader(f1)
sql = sqlite3.connect('car.db')
sql.text_factory = str
cur = sql.cursor()


for row in csv_f1:
    cur.execute(''' INSERT INTO CarMake(Make,CEO,country) VALUES(?,?,?) ''', row)

f2 = open('Table-Model.csv')
next(f2, None)
csv_f2 = csv.reader(f2)

for row in csv_f2:
    
    cur.execute(''' INSERT INTO Model(id, Make, Model, Year, Engine_HP,
    Engine_Cylinders, Highway_MPG, City_MPG) VALUES(?,?,?,?,?,?,?,?) ''', row)

f1.close()
f2.close()
sql.commit()
sql.close()



