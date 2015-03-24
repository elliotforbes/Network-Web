from scapy.all import *
import threading

class trafficAnalyser(threading.Thread):
    
    HTTPCount = 0
    FTPCount = 0
    DHCPCount = 0
    SMTPCount = 0
    BITCount = 0
    packetCount = 0
    SSDPCount = 0
    SSHCount = 0
    POPCount = 0
    MISCCount = 0
    
    def __init__(self):
        super(trafficAnalyser, self).__init__()
        print("Traffic Analysis Started")
    
    def customAction(self, packet):
        self.packetCount += 1
        if(packet.dport == 80):
            self.HTTPCount += 1
        elif(packet.dport == 22):
            self.SSHCount += 1
        elif(packet.dport == 109):
            self.POPCount += 1
        elif(packet.dport == 1900):
            self.SSDPCount += 1
        elif((packet.dport == 2525) or (packet.dport == 25)):
            self.SMTPCount += 1
        else:
            self.MISCCount += 1
#        if(packet.proto == 6):
#            self.TCPCount +=1
#        elif(packet.proto == 17):
#            self.SSDPCount += 1
        
#        return "Packet #" + str(self.packetCount) + ": " + packet[0][1].src + "==>" + packet[0][1].dst + "  :  PROTO: " + str(packet.dport)

    
    def run(self):
        while(1):
            try:
                sniff(prn=self.customAction)
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
        print("HTTP Count: " , self.HTTPCount)
        print("SMTP Count: " , self.SMTPCount)
        print("SSH Count: " , self.SSHCount)
        print("SSDP Count: " , self.SSDPCount)
        print("POP Count: " , self.POPCount)
        print("BitTorrent Count: " , self.BITCount)
        print("Misc Count: " , self.MISCCount)
    
    def expand(x):
        yield x
        while x.payload:
            x = x.payload
            yield x