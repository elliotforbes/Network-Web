import threading
import string
from modules import speedtest
import commands

dPis = []
speedTest = False


def connect(dPis, connected_IP):
    if connected_IP is None:
        if not dPis:
            print("No Available Pis to Connect With")
        else:
            connected_IP = dPis[0]
            print("Connected with: %s", connected_IP)
    
    
        
# The main desicion tree for the program.
# Currently only accepts exact strings but might add some form of
# leway.
def parseControl(str):
    args = string.split(str)
    if args[0] == "hello":
        return 1
    elif args[0] == "quit":
        return 2
    elif args[0] == "speedtest":
        return 3
    elif args[0] == "TCPstress":
        self.setupTCPtest()
    elif args[0] == "list":
        return 5
    elif args[0] == "UDPTest":
        self.testClient(args[1])
    elif args[0] == "connect":
        self.setConnect(args[1])
    elif args[0] == "speedtest":
        speedtest.speedTest = True
    elif args[0] == "AllDevices":
        return 8
    elif args[0] == "quit":
        self.quitGracefully()
    else:
        return 0


# Simple help manual
def printHelp():
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


def getConnectIP():
    print(self.connect_IP)

# This will have a look at the global variable Discovered_Pis in the driver.py
# file and then print out all corresponding IP Addresses as well their current
# connection options
def listDiscoveredPis(dPis, IP_ADDRESS):
    print("List of Available Pis")
    for pi in dPis:
        if IP_ADDRESS not in pi:
            print(pi)
            
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
        
def listAllNetworkMachines():
    print(commands.getstatusoutput('wc -l file'))

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