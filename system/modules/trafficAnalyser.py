from scapy.all import *
import threading

class trafficAnalyser(threading.Thread):
    
    TCPCount = 0
    IPCount = 0
    UDPCount = 0
    SSDPCount = 0
    MiscCount = 0
    
    def __init__(self):
        super(trafficAnalyser, self).__init__()
        print("Traffic Analysis Started")
        
    def run(self):
        while(1):
            for pkt in sniff(iface='eth1'):
                if IP in pkt:
                    self.IPCount += 1
                elif UDP in pkt:
                    self.UDPCount += 1
                elif TCP in pkt:
                    self.TCPCount += 1
                elif SSDP in pkt:
                    self.SSDPCount += 1
                else:
                    self.MiscCount += 1
            printAll()

    def printAll(self):
        print("TCP Count: " ,TCPCount)
        print("IP Count: " ,IPCount)
        print("UDP Count: " ,UDPCount)
        print("SSDP Count: " ,SSDPCount)
        print("Misc Count: " ,MiscCount)
    
    
    def expand(x):
        yield x
        while x.payload:
            x = x.payload
            yield x