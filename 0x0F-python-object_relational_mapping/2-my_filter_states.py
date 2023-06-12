#!/usr/bin/python3

''' lists all states from hbtn_0e_0_usa database.
 usage: ./0-select_states.py <mysql username>
                              <mysql password>
                              <mysql database>
'''
import sys
import MySQLdb
if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE \
                `name` LIKE sys.argv[4]")
    [print(state) for state in cur.fetchall()]
    """closes the cursor connection."""
    cur.close()
    """closes the database connection."""
    db.close()
