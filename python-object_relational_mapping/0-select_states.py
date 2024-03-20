#!/usr/bin/python3
"""
Script that lists all states from the databse hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    u_name = argv[1]
    psw = argv[2]
    base = argv[3]

    db = MySQLdb.connect(host="localhost", user=u_name, passwd=psw, db=base, port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()