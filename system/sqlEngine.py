import sqlite3 as lite
import sys


def install():
    try:
        con = lite.connect("main.db")
        cur = con.cursor()
        
        connected = open('scripts/create/createConnected.sql', 'r').read()
        data = open('scripts/create/createData.sql', 'r').read()
        throughput = open('scripts/create/createThroughput.sql', 'r').read()
        upload = open('scripts/create/createUpload.sql', 'r').read()
        download = open('scripts/create/createDownload.sql', 'r').read()
        
        cur.execute(connected);
        cur.execute(data);
        cur.execute(throughput);
        cur.execute(upload);
        cur.execute(download);
        
        print("SQLEngine Started.")
        
        con.commit()
        
    except lite.Error, e:
        print "Error shite %s:" % e.args[0]
        sys.exit(1)

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
        con = lite.connect("main.db")

        con.execute('''SELECT * FROM connected;''')
        
        print("---------------------")
        for row in con:
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[3])
            print("------------------\n")
        con.close()
        con.commit()

    except lite.Error, e:
        print("Error %s:" % e.args[0])
        sys.exit(1)

def insertPi(IP_ADDRESS, CONNECTED, LEASE_TIME):
    try:
        con = lite.connect("main.db")
        
        query = "INSERT INTO connected (IP_ADDRESS,CONNECTED, CONNECTED_IP, LEASE_TIME)"
        query += "VALUES ('"
        query += IP_ADDRESS
        query += "', 1, '"
        query += LEASE_TIME
        query += "',0)"
#        print(query)

        con.execute(query);
    
        con.commit()
    
    except lite.Error, e:
        print("Error %s:" % e.args[0])
        print(e)
        sys.exit(1)

def updateLease(IP, LEASE):
    try:
        con = lite.connect("main.db")

        query = "UPDATE connected "
        query += "SET LEASE_TIME = LEASE_TIME - "
        query += LEASE
        query += " WHERE IP_ADDRESS = '"
        query += IP
        query += "';"
        
        print(query)

#        con.execute('''UPDATE connected SET LEASE_TIME = 555 where ID = 1;''');
        con.execute(query)
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
    


#dropDiscoveredTable()
install()
#sql.createDiscoveredTabl   e()
#sql.insertPi()
#sql.selectAll()
#sql.updatePi(1,1,1)
#sql.removePi()
#sql.selectAll()