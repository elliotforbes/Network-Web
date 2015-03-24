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
        speeds = open('scripts/create/createSpeeds.sql', 'r').read()
        latency = open('scripts/create/createLatency.sql', 'r').read()
        
        cur.execute(connected);
        cur.execute(data);
        cur.execute(throughput);
        cur.execute(upload);
        cur.execute(download);
        cur.execute(speeds);
        cur.execute(latency);
        
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
        cur.execute('''DROP TABLE throughtputResults''')
        cur.execute('''DROP TABLE downloadResults''')
        cur.execute('''DROP TABLE uploadResults''')
        cur.execute('''DROP TABLE dataResults''')
        
        con.commit()
    except lite.Error, e:
        print("Error %s:" % e.args[0])
        sys.exit(1);

        
        
def insertLatency(RESULT):
    try:
        con = lite.connect("main.db")
        
        query = "INSERT INTO latency (RESULT)"
        query += "VALUES ('"
        query += str(RESULT)
        query += "');"
        
        con.execute(query);
        
        con.commit()
        
    except Exception,e:
        print(e)
    
def insertThroughput(RESULT):
    try:
        con = lite.connect("main.db")
        
        query = "INSERT INTO throughputResults (RESULT)"
        query += "VALUES ('"
        query += str(RESULT)
        query += "');"
        
        con.execute(query);
        
        con.commit()
        
    except Exception,e:
        print(e)

def insertSpeeds(DOWNLOAD, UPLOAD):
    try:
        con = lite.connect("main.db")
        
        query = "INSERT INTO speeds (DOWNLOAD, UPLOAD)"
        speed += "VALUES ('"
        query += DOWNLOAD
        query += "', '"
        query += UPLOAD
        query += "');"
        
        con.execute(query);
        
        con.commit()
        
    except Exception,e:
        print(e)
        
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
        
        query = "INSERT INTO connected (IP_ADDRESS,CONNECTED, LEASE_TIME)"
        query += "VALUES ('"
        query += IP_ADDRESS
        query += "', 1, '"
        query += LEASE_TIME
        query += "') ;"
#        query += " WHERE NOT EXISTS ( SELECT * FROM connected WHERE"
#        query += " IP_ADDRESS = '"
#        query += IP_ADDRESS
#        query += "' );"
#        print(query)

        con.execute(query);
    
        con.commit()
    
    except lite.Error, e:
        print("Error %s:" % e.args[0])
        print(e)
        sys.exit(1)


def updateConnect(IP, CONNECT):
    try:
        con = lite.connect("main.db")

        query = "UPDATE connected "
        query += "SET CONNECTED = "
        query += LEASE
        query += " WHERE IP_ADDRESS = '"
        query += IP
        query += "';"
        
#        print(query)

#        con.execute('''UPDATE connected SET LEASE_TIME = 555 where ID = 1;''');
        con.execute(query)
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
        
#        print(query)

#        con.execute('''UPDATE connected SET LEASE_TIME = 555 where ID = 1;''');
        con.execute(query)
        con.commit()
    
    except lite.Error, e:
        print("Error %s:" % e.args[0])
        print(e)
        sys.exit(1)

def equalsLease(IP, LEASE):
    try:
        con = lite.connect("main.db")

        query = "UPDATE connected "
        query += "SET LEASE_TIME = "
        query += LEASE
        query += " WHERE IP_ADDRESS = '"
        query += IP
        query += "';"
        
#        print(query)

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
#install()
#sql.createDiscoveredTabl   e()
#sql.insertPi()
#sql.selectAll()
#sql.updatePi(1,1,1)
#sql.removePi()
#sql.selectAll()