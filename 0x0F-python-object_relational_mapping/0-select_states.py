#!/usr/bin/python3
"""
List all states from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host="localhost", port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    allstates = cur.fetchall()

    for state in allstates:
        print(state)
    cur.close()
    db.close()
