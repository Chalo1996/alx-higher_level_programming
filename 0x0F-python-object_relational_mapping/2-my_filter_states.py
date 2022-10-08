#!/usr/bin/python3
"""that takes in an argument and displays all\
    values in the states table of hbtn_0e_0_usa\
    where name matches the argument.
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    arg = argv[4]
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset='utf8'
    )

    cur = conn.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "{:s}"\
        ORDER BY id ASC'.format(arg))
    vals = cur.fetchall()

    for val in vals:
        if val[1] == arg:
            print(val)

    cur.close()
    conn.close()
