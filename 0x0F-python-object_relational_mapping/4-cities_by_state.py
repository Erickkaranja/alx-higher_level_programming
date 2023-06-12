#!/usr/bin/python3

''' python script that lists all cities from a database.'''

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(user="root", passwd="Ei@G69!ka98m",
                         db="hbtn_0e_4_usa")
    cur = db.cursor()
    cur.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name` \
                FROM `cities` \
                INNER JOIN `states` \
                ON `cities`.`state_id`=`states`.`id` \
                ORDER BY `cities`.`id`")
    [print(city) for city in cur.fetchall()]
    cur.close()
    db.close()
