#!/usr/bin/python3

# lists all states from hbtn_0e_0_usa database.
# usage: ./0-select_states.py <mysql username>
#                             <mysql password>
#                             <mysql database>

import sys
import MySQLdb
db = MySQLdb.connect(user="sys.argv[1]", passwd="sys.argv[2]",
                     db="sys.argv[3]")
cur = db.cursor()
cur.execute("SELECT * FROM `STATES` WHERE BINARY
            `name` = `{}`".format(sys.argv[4])
[print(state) for state in cur.fetchall()]