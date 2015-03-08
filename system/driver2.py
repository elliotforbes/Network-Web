from modules import listen
from modules import sockets
from modules import control
from modules import speedtest
from modules import advertise
from modules import sqlEngine as sql
from modules import manageLeases
import socket
import struct
import threading
import sys
import string
from subprocess import call

class Driver():
    
    # GLOBAL VARIABLES
    isConnected = False
    dPis = []
    speedTest = False
    IP_ADDRESS = sockets.getIPAddress()
    SSDP_REQUEST = sockets.returnSSDPRequest(IP_ADDRESS)
    
    # THREADS
    listenThread = None
    controlThread = None
    advertiseThread = None
    leaseThread = None
    
    # SOCKETS
    SSDP_SOCK = sockets.getSSDPSocket()
    TCP_SOCK = sockets.getTCPSock()
    
    
    #
    # FUNCTIONS
    #
    def __init__(self):
        super(Driver, self).__init__()
        self.initThreads()
        self.runThreads()
        sql.install()
    
    def initThreads(self):
        self.listenThread = listen.listen(self.SSDP_SOCK, self.dPis)
        self.advertiseThread = advertise.advertise(self.TCP_SOCK, self.SSDP_REQUEST)
        self.leaseThread = manageLeases.manageLeases(self.dPis)
#        self.controlThread = control.control(self.dPis, self.speedTest)
    
    def runThreads(self):
        self.listenThread.start()
        self.advertiseThread.start()
        self.leaseThread.start()
#        self.controlThread.start()
        
    def run(self):
        while(1):
            var = raw_input("-> ")
            args = string.split(var)
            controlVar = control.parseControl(args[0])
            self.performTask(controlVar)
    
    def performTask(self, controlVar):
        if controlVar == 0:
            print("Invalid Command, Type help for a detailed list of instructions")
        elif controlVar == 1:
            print("hello")
        elif controlVar == 2:
            self.closeSockets()
        elif controlVar == 3:
            print("Speedtest Initializing")
            self.speedtest()
        elif controlVar == 4:
            control.testServer()
        elif controlVar == 5:
            control.listDiscoveredPis(self.dPis, self.IP_ADDRESS)
        elif controlVar == 6:
            control.testClient()
        elif controlVar == 7:
            control.listAllNetworkMachines()
            
    def speedtest(self):
        speedtest.speedtest()
    
    def closeSockets(self):
        self.SSDP_SOCK.close()
        sys.exit(1)
        
if __name__ == "__main__":
    
    
#    call(["ls", "-l"])
    
    driver = Driver()
    
    driver.run()
    