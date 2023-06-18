#!/usr/bin/python3
'''script that finds the string.
./2-my_filter_states.py user passwd database querystring
'''

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
