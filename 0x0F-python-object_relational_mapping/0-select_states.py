#!/usr/bin/python3
"""Import the required module"""
from MySQLdb import _mysql


db = _mysql.connect(host="localhost",port=3306,user="root",password="password",database="hbtn_0e_0_usa")
db.query("""SELECT id, name from states""")

r = db.use_result()
r.fetch_row()
