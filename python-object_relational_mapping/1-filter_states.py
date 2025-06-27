#!/usr/bin/python3
"""list states starting by `N`
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
