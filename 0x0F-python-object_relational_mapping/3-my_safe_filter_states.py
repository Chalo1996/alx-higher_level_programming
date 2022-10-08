#!/usr/bin/python3
""" safe from MySQL injections!
"""


import MySQLdb
from sys import argv


if __name__ == '__main__':
    arg = argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset='utf8'
    )

    cur = conn.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE %s\
        ORDER BY id ASC', (arg,))

    argsNames = cur.fetchall()

    for argsName in argsNames:
        print(argsName)

    cur.close()
    conn.close()
