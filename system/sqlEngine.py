import sqlite3 as lite
import sys


def __init__(s):
    print("SQLite Engine Started.")


def conn():
    try:
        con = lite.connect("test.db")
        cur = con.cursor()
        cur.execute('SELECT SQLITE_VERSION()')

        data = cur.fetchone()

        con.commit()
        print("%s SQLite Version" % data)
    except lite.Error, e:

        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:

        if con:
            con.close()

def createDiscoveredTable():
    try:
        con = lite.connect("test.db")
        cur = con.cursor()

        cur.execute('''CREATE TABLE connected
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     IP_ADDRESS VARCHAR(128) NOT NULL,
                     CONNECTED INT NOT NULL,
                     LEASE_TIME INT NOT NULL);''')
        con.commit()
        print("Table Successfully Created")

    except lite.Error, e:
        print("Error %s:" % e.args[0])
        sys.exit(1)

def dropDiscoveredTable():
    try:
        con = lite.connect("test.db")
        cur = con.cursor()

        cur.execute('''DROP TABLE connected;''')

        con.commit()
    except lite.Error, e:
        print("Error %s:" % e.args[0])
        sys.exit(1)

def selectAll():
    try:
        con = lite.connect("test.db")
        cur = con.cursor()

        cur.execute('''SELECT * FROM connected;''')
        print("---------------------")
        for row in cur:
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[3])
            print("------------------\n")
        con.commit()

    except lite.Error, e:
        print("Error %s:" % e.args[0])
        sys.exit(1)

def insertPi(IP_ADDRESS, CONNECTED):
    try:
        con = lite.connect("test.db")

        query = "INSERT INTO connected (IP_ADDRESS,CONNECTED, LEASE_TIME)"
        query += "VALUES ('"
        query += IP_ADDRESS
        query += "',1,0)"
        print(query)

        con.execute(query);

        con.commit()

    except lite.Error, e:
        print("Error %s:" % e.args[0])
        print(e)
        sys.exit(1)



def updatePi(ID, IP_ADDRESS, CONNECTED):
    try:
        print("DB Updated")
        if ID is not None:
            con = lite.connect("test.db")
            cur = con.cursor()
            query = '''UPDATE connected 
                    SET CONNECTED = 0
                    WHERE ID = 1'''
            cur.execute(query)
            con.commit()
    except lite.Error, e:
        print("Error %s:" % e.args[0])
        sys.exit(1)

def removePi(ID):
    ID = int
    try:
        con = lite.connect("test.db")
        cur = con.cursor()

        cur.execute('''DELETE FROM connected WHERE ID = 1;''')
        con.commit()
        print("Successfully Deleted: 1 From the Databse")
    except lite.Error, e:
        print("Error %s:" % e.args[0])
        sys.exit(1)
    
#sql = sqlEngine()
#sql.dropDiscoveredTable()

#sql.conn()
#sql.createDiscoveredTable()
#sql.insertPi()
#sql.selectAll()
#sql.updatePi(1,1,1)
#sql.removePi()
#sql.selectAll()