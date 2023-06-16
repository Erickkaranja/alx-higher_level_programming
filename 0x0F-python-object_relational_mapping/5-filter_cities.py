#!/usr/bin/python3
'''selects all cities from the database hbtn_0e_4_usa
   usage:./5-filter_cities.py  user passwd database state.
'''

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    c = db.cursor()
    c.execute("SELECT `c`.`name`, `c`.`id`, `s`.`name`\
              FROM `cities` as `c`\
              INNER JOIN `states` as `s`\
              ON `c`.`state_id` = `s`.`id`\
              ORDER BY `c`.`id`")
    print(",".join([val[1] for val in c.fetchall() if val[2] == sys.argv[4]]))
    c.close()
    db.close()
