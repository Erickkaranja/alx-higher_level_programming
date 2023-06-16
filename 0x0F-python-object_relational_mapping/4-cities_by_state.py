#!/usr/bin/python3
'''selects all cities from the database hbtn_0e_4_usa
   usage:./4-cities_by_state.py user passwd database.
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
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name`\
              FROM `cities` as `c`\
              INNER JOIN `states` as `s`\
              ON `c`.`state_id` = `s`.`id`\
              ORDER BY `c`.`id` ASC")
    [print(city) for city in c.fetchall()]
    c.close()
    db.close()
