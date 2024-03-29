#!/usr/bin/python3
'''lists all states in hbtn_oe_0_usa database.
   usage: ./0-select_states.py host passwd database.
'''

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY id ASC")
    [print(state) for state in c.fetchall()]
    c.close()
    db.close()
