#!/usr/bin/python3
"""Import the required module"""
import MySQLdb


db = MySQLdb.connect(user="root",password="password",db="hbtn_0e_0_usa8")
cur = db.cursor()
cur.execute("""SELECT id, name from states LIMIT 5""")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
