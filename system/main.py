import socket
import sys
import threading
import struct
import string
import time
import re
import speedtest as speed
import sqlEngine as sql


class control(threading.Thread):
    
    def __init__(self):
        super(control, self).__init__()
        
    def parseControl(self, str):
        args = string.split(str)
        if args[0] == "hello":
            print("Hi, You can obtain a list of the systems functionality by typing 'help'.")
        elif args[0] == "bye":
            self.quitGracefully()
        elif args[0] == "help":
            self.printHelp()
        elif args[0] == "TCPstress":
            self.setupTCPtest()
        elif args[0] == "list":
            self.listDiscoveredPis()
        elif args[0] == "UDPTest":
            self.testClient(args[1])
        elif args[0] == "connect":
            self.setConnect(args[1])
        elif args[0] == "speedtest":
            speed.speedtest()
        elif args[0] == "quit":
            self.quitGracefully()
        else:
            print("Invalid Command")
    
    
    # Basic command line interface.
    def run(self):
        while(1):
            var = raw_input("-> ")
            self.parseControl(var)
              
class tests():
    
    def __init__():
        print("Test Engine Initialized")
    
    def speedtest(self):
        speed.speedtest()
        
    def tcpTest(self, serverIP):
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