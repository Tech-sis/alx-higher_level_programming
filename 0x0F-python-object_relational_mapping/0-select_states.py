#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
"""

import MySQLdb
MySQLdb.connect
db = MySQLdb.connect(host="localhost", port=3306,
                     user="root", passwd="root", db="hbtn_0e_0_usa")
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
