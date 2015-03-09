from modules import sqlEngine as sql
from modules import alertEngine as alert
import threading
import struct
import sys
import string
import urllib2


class testEngine(threading.Thread):
    
    def __init__(self):
        super(testEngine, self).__init__()
        print("Test Engine Started")
        
    
    def run(self):
        while(1):
            time.sleep(5)
            if not (self.testConnectivity()):
                alert.sendAlert()
    
    def testConnectivity(self):
        try:
            response=urllib2.urlopen('http://74.125.228.100',timeout=1)
            return True
        except urllib2.URLError as err: pass
        return False
    
    