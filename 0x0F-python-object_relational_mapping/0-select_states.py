#!/usr/bin/python3
"""Import the required module"""
from MySQLdb import _mysql


db = _mysql.connect(host="localhost",port=3306,user="mysql",password="password",database="hbtn_0e_0_usa")

db.query("""SELECT name from states ORDER BY id""")
