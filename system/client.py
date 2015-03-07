import socket
import sys
import threading
import struct
import string
import time
import re
import speedtest as speed
import sqlEngine as sql

# Does the control thread control the advertising
# Mutex type of lock? Check type of lock

# Look at read/write locks on the data?

# synchronize with the control thread so that it can wait before it at least
# advertise it's presence on the network before it starts
# synchonization of the boolean value for has sent advertisement

# look at what synchronization constructs python offers
# automatically setup the server through the control thread
# control channel setup between two threads
# add control channel message to the ssdp message
# figure out bandwidth test for next week

# figure out what happens behind the scenes on each of the tests 
# have a clear list of tesets to do.

# chokepoint
# bandwidth

# email different tests and what they entail 
# email when I've found out safe way to communicate details between threads.

# monitor on top of data


# 
# Potentially use a seperate pi as the "speedtest" style server.
# 
# Ensure that you are not fighting for a lock during a test so as to not
# mess up the timing. 

# Adding real time 

# don't limit the amount of test results shown.

# PRIORITIES

# - Add local Speedtest server
# - check functionality of the third data

# Add phone updates for data allowances
# Add functionality to see what application is using what

# check feasibility of capturing packets and analysing 
# check the legal feasibility. 
# 
class InfoClass():
    
    Discovered_Pis = []

# The DBThread will constantly update the 
class DBThread(threading.Thread):
    
    def __init__(self):
        super(DBThread, self).__init__()
    
    
class controlThread(threading.Thread):
    
    def initiateTCP(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 8105))
    
    def run(self):
        while(1):
            sock_data = self.sock.recv(10240)

            
class testThread(threading.Thread):
    
    connected = False
    connect_IP = ''
    isServer = 1
    
    def __init__(self, connected, connect_IP, isServer):
        super(testThread, self).__init__()
        self.connected = connected
        self.connect_IP = connect_IP
        self.isServer = isServer
        
    def run(self):
        while(1):
            if self.connected:
                self.testServer()
                
    def testServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 8105))
        s.listen(1)
        print 'Server ready...'
        while 1:
            conn, (host, remoteport) = s.accept()
            while 1:
                data = conn.recv(10240)
                if not data:
                    break
                del data
            conn.send('OK\n')
            conn.close()
            print 'Done with', host, 'port', remoteport
            break
    
    # This will run the test on the network.
    def testClient(self, str):
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
                
                
            
# The control thread deals with user command line input and will
# eventually interface with the webapp that is currently under 
# construction.
class Control(threading.Thread):
    
    dPis = []
    advertised = False
    connected = False
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com",80))
    IP_ADDRESS = s.getsockname()[0]
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    
    
    UDP_IP = '239.255.255.250'
    UDP_PORT = 1900
    
    connect_IP = ''
    
    CON_REQUEST = ('PiControl\r\n' +
             'IPNO: [%s]\r\n' % (IP_ADDRESS) + 
             'CON_REQUEST: 1\r\n' +
              '\r\n')
    
    def __init__(self, dPis, advertised,connected, connect_IP):
        super(Control, self).__init__()
        self.dPis = dPis
        self.advertised = advertised
        self.connect_IP = connect_IP
        self.connected = connected
    # The main desicion tree for the program.
    # Currently only accepts exact strings but might add some form of
    # leway.
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
    
    def sendConnectMessage(self):
        self.sock.sendto(self.CON_REQUEST, (self.UDP_IP, self.UDP_PORT))
            
        # This will run the test on the network.
    def testClient(self, str):
        try:
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
        except:
            print("Error %s:" % sys.exc_info()[0])
            sys.exit(1)

    # Simple help manual
    def printHelp(self):
        print("Network Monitor, version 0.1.1-release")
        print("These control commands are defined internally. Type 'Help' to see this list.")
        print("Type 'help name' to find out more about the function 'name'.")
        print("\n")
        print("'hello' : System responds with 'Hi'")
        print("'testServer' : \tThis starts the test Server on the current R-Pis" +
              "Node. Once this server has been set up the the second Pi can now perform" +
              "Throughput tests.")
        print("'testTarget IP_ADDRESS' : This will then initiate a udp stress test with a server" +
              "located at 'IP_ADDRESS'. Example usage: testTarget 192.168.1.104")
        print("'quit' : System shuts down all sockets and quits gracefully")
    
    
    def setConnect(self, str):
        self.connect_IP = str
        self.sendConnectMessage()
        
    def getConnectIP(self):
        print(self.connect_IP)
        
    # This will have a look at the global variable Discovered_Pis in the driver.py
    # file and then print out all corresponding IP Addresses as well their current
    # connection options
    def listDiscoveredPis(self):
        print("List of Available Pis")
        for pi in self.dPis:
            if self.IP_ADDRESS not in pi:
                print(pi)
    
    # This shuts down the current control thread. Should this thread
    # be shut down then the driver class picks up on this and subsequently
    # shuts down all other threads and sockets.
    def quitGracefully(self):
        sys.exit()
    
    # Basic command line interface.
    def run(self):
        while(1):
            var = raw_input("-> ")
            self.parseControl(var)
            
            
class manageLeases(threading.Thread):
    
    dPis = []
    
    def __init__(self, dPis):
        super(manageLeases, self).__init__()
        print("Lease Manager Started.")
        self.dPis = dPis
        
    def run(self):
        while(1):
            for pi in self.dPis:
#                print(pi[0])
                sql.updateLease(str(pi[0]), "5")
                time.sleep(1)
                
            
class Advertise(threading.Thread):
    
    
    SSDP_MX = 1
    SSDP_ST = "ssdp:all"
    UDP_IP = '239.255.255.250'
    UDP_PORT = 1900
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com",80))
    IP_ADDRESS = s.getsockname()[0]
    
    LEASE_TIME = 1000   
    
    SSDP_REQUEST = ('Raspberry\r\n' +
             'M-SEARCH * HTTP/1.1\r\n' +
             'MAN: "ssdp:discover"\r\n' + 
             'MX: %d\r\n' % (SSDP_MX, ) +
             'ST: %s\r\n' % (SSDP_ST, ) +
             'HOST: 239.255.255.250:1900\r\n' + 
             'IPNO: [%s]\r\n' % (IP_ADDRESS) + 
             'LEASE: &100&\r\n' +
              '\r\n')
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    
    def __init__(self, advertised):
        super(Advertise, self).__init__()
        print("Advertising Thread Started")
        self.advertised = advertised
#        sql.insertPi(self.IP_ADDRESS, 1)
        
    def quit(self):
        self.s.close()
        self.sock.close()
#        sys.exit()
    
    def run(self):
        while(1):
            time.sleep(10)
            self.sock.sendto(self.SSDP_REQUEST, (self.UDP_IP, self.UDP_PORT))
            

        
class Listen(threading.Thread):
        
#    global Discovered_Pis 

    connected = False
    connect_IP = ''
    

    MCAST_GRP = '239.255.255.250'
    MCAST_PORT = 1900

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', MCAST_PORT))
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    
    def __init__(self, dPis, connected, connect_IP):
        super(Listen, self).__init__()
        print("Listen Thread Started")
        self.dPis = dPis
        self.connect_IP = connect_IP
        self.connected = connected
        
        
    def quit(self):
        self.sock.close()
#        sys.exit()
    
    def getIPAddress(self, request_text):
        if "Raspberry" in request_text:
            pattern = re.compile(r'(?<=\[)(.*?)(?=\])', flags = re.DOTALL)
            leaseTime = re.compile(r'(?<=\&)(.*?)(?=\&)', flags = re.DOTALL)
            lease = leaseTime.findall(request_text)
            results = pattern.findall(request_text)
            if results not in self.dPis:
                self.dPis.append(results)
                # Move this to another thread 
                # ensure that no packets are missed.
                sql.insertPi(results[0], 1, lease[0] )
            elif results in self.dPis:
                sql.equalsLease(results[0], "100")
                
        elif "PiControl" in request_text:
            print("PiControl Message Received")
            pattern = re.compile(r'(?<=\[)(.*?)(?=\])', flags = re.DOTALL)
            results = pattern.findall(request_text)
            if self.connected: 
                print("This Pi is already connected")
            else:
                self.connect_IP = results[0]
                self.connected = True
        else:
            continue
#        elif "LEASE-UPDATE" in request_text:
#            print(request_text)
#            print(results)
    
    # This is what I have to work on next, this will basically take in any
    # messages sent by other clients and then decide what actions to take 
    # based on those messages.
    def parseMessage(self, request_text):
        pattern = re.compile(r'IPNO', flags=re.DOTALL)
        results = pattern.findall(request_text)
#        print(results)
#        SERVICE_LOCS.append(results)
    
    def run(self):
        while(1):
            # Added for Debug Purposes.
#            print("Listening")
            sock_data = self.sock.recv(10240)
            self.getIPAddress(sock_data)
#            print(self.sock.recv(10240))
        return
    