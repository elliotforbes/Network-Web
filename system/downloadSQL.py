import sqlite3 as lite
import sys

class dlTestSQL():
    
    def __init__(self):
        print("Download/Upload Test Server Initiated")
        
    def createTable(self):
        try:
            con = lite.connect("dlul.db")
            cur = con.cursor()
            
            cur.execute('''CREATE TABLE testResults
                        (ID INT PRIMARY KEY AUTO_INCREMENT,
                         DL_SPEED 