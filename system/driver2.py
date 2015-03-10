from modules import listen
from modules import sockets
from modules import control
from modules import speedtest
from modules import advertise
from modules import sqlEngine as sql
from modules import manageLeases
from modules import alertEngine as alert
from modules import testEngine
from modules import deviceDiscover as device
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
    connected_IP = None
    alertPhone = None
    
    # THREADS
    listenThread = None
    controlThread = None
    advertiseThread = None
    leaseThread = None
    alertThread = None
    testThread = None
    
    # SOCKETS
    SSDP_SOCK = sockets.getSSDPSocket()
    TCP_SOCK = sockets.getTCPSock()
    
    
    #
    # FUNCTIONS
    #
    def __init__(self):
        self.initThreads()
        self.runThreads()
        sql.install()
    
    def initThreads(self):
        self.listenThread = listen.listen(self.SSDP_SOCK, self.dPis, self.isConnected)
        self.advertiseThread = advertise.advertise(self.TCP_SOCK, self.SSDP_REQUEST)
        self.leaseThread = manageLeases.manageLeases(self.dPis)
        self.testThread = testEngine.testEngine(self.connected_IP, self.isConnected)
#        self.alertThread = alert.alertEngine()
#        self.controlThread = control.control(self.dPis, self.speedTest)
    
    def runThreads(self):
        self.listenThread.start()
        self.advertiseThread.start()
        self.leaseThread.start()
        self.testThread.start()
#        self.alertThread.start()
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
            device.returnDevices()
        elif controlVar == 7:
            # Connects the Pi to the first available Pi
            control.connect(self.dPis, self.connected_IP, self.SSDP_SOCK)
        elif controlVar == 8:
            # Lists all machines on the local network
            control.listAllNetworkMachines()
        elif controlVar == 9:
            # get's the phone number for which you want alert
            # messages sent
            self.alertPhone = control.getPhoneNumber()
        elif controlVar == 10:
            # Prints phone number connected with the alert Engine
            print(self.alertPhone)
        elif controlVar == 11:
            control.testClient(self.connected_IP)
            
    def speedtest(self):
        speedtest.speedtest()
    
    def closeSockets(self):
        self.SSDP_SOCK.close()
        sys.exit(1)
        
if __name__ == "__main__":
    
    
#    call(["ls", "-l"])
    
    driver = Driver()
    
    driver.run()
    