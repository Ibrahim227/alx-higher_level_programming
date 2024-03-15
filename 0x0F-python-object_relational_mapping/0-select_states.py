#!/usr/bin/python3
"""Import the required module"""
import MySQLdb


db = MySQLdb.connect(host="localhost",port=3306,user="root",password="password",db="hbtn_0e_0_usa")
cur = db.cursor()
cur.execute("""SELECT * from states""")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
