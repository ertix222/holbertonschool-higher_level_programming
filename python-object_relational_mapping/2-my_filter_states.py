#!/usr/bin/python3
"""list states corresponding to names passed as arg and display values
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

    name = sys.argv[4]
    query = "SELECT * FROM states WHERE name =" \
        " '{}' ORDER BY id ASC;".format(name.replace("'", "''"))

    cur = conn.cursor()
    cur.execute(query)
    states = cur.fetchall()

    for state in states:
        print(state)
    
    cur.close()
    conn.close()
