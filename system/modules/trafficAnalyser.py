from scapy.all import *
import threading

class trafficAnalyser(threading.Thread):
    
    TCPCount = 0
    IPCount = 0
    UDPCount = 0
    SSDPCount = 0
    MiscCount = 0
    packetCount = 0
    
    
    def __init__(self):
        super(trafficAnalyser, self).__init__()
        print("Traffic Analysis Started")
    
    def customAction(self, packet):
        self.packetCount += 1
        if(packet.proto == 6):
            self.TCPCount +=1
        elif(packet.proto == 17):
            self.SSDPCount += 1
        
        return "Packet #" + str(self.packetCount) + ": " + packet[0][1].src + "==>" + packet[0][1].dst + "  :  PROTO: " + str(packet.proto[0][1])

    
    def run(self):
        while(1):
            try:
                sniff(filter="ip",prn=self.customAction)
            except Exception, e:
                print(e)
#            for pkt in sniff():
#                print(pkt)
#                if IP in pkt:
#                    self.IPCount += 1
#                elif UDP in pkt:
#                    self.UDPCount += 1
#                elif TCP in pkt:
#                    self.TCPCount += 1
#                elif SSDP in pkt:
#                    self.SSDPCount += 1
#                else:
#                    self.MiscCount += 1
        

    def printAll(self):
        print("TCP Count: " , self.TCPCount)
        print("IP Count: " , self.IPCount)
        print("UDP Count: " , self.UDPCount)
        print("SSDP Count: " , self.SSDPCount)
        print("Misc Count: " , self.MiscCount)
    
    
    def expand(x):
        yield x
        while x.payload:
            x = x.payload
            yield x