#!/usr/bin/python3

# lists all states from hbtn_0e_0_usa database.
# usage: ./0-select_states.py <mysql username>
#                             <mysql password>
#                             <mysql database>

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `STATES`")
    [print(state) for state in c.fetchall()]
