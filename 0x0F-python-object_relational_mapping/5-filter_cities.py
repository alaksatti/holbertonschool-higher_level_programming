#!/usr/bin/python3
'''
lists cities from a state taken as an argument"
'''

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities"
                "AS a JOIN states AS states ON cities.state_id = states.id"
                "WHERE states.name = %s ORDER BY cities.id", (argv[4],))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    db.close()
