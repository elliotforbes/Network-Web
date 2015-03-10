from modules import sqlEngine as sql
from modules import alertEngine as alert
import threading
import struct
import sys
import string
import urllib2


class testEngine(threading.Thread):
    
    connected_IP = None
    
    def __init__(self, connected_IP):
        super(testEngine, self).__init__()
        print("Test Engine Started")
        self.connected_IP = connected_IP
        
    
    def run(self):
        while(1):
            time.sleep(5)
            if not (self.testConnectivity()):
                alert.sendAlert()
            if self.connected_IP:
                self.testThroughput(self.connected_IP)
            
    
    def testConnectivity(self):
        try:
            response=urllib2.urlopen('http://74.125.228.100',timeout=1)
            return True
        except urllib2.URLError as err: pass
        return False
    
    
    def testThroughput(self, str):
        count = 100
        testdata = 'x' * (10240-1) + '\n'
        t1 = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        t2 = time.time()
        s.connect((str, 8105))
        t3 = time.time()
        i = 0
        while(1):
            data = raw_input('Enter No. of Packets: ')
            args = string.split(data)
            try:
                count = int(args[0])
            except:
                count = None
                print "Error, you need to specify number of packets you want to send."
            if not data:
                pass
            else:
                while i < count:
                    i = i+1
                    s.send(testdata)
                s.shutdown(1) # Send EOF
                t4 = time.time()
                data = s.recv(10240)
                t5 = time.time()
                print data
                print 'Raw timers:', t1, t2, t3, t4, t5
                print 'Intervals:', t2-t1, t3-t2, t4-t3, t5-t4
                print 'Total:', t5-t1
                print 'Throughput:', round((10240*count*0.001) / (t5-t1), 3),
                print 'K/sec.'
            break
