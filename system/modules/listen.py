import threading
import re
import sqlEngine as sql
import control

class listen(threading.Thread):
    
    SSDP_SOCK = None
    dPis = None
    isConnected = None
    IP_ADDRESS = None
    
    def __init__(self, SSDP_SOCK, dPis, isConnected, IP_ADDRESS):
        super(listen, self).__init__()
        self.SSDP_SOCK = SSDP_SOCK
        self.dPis = dPis
        self.isConnected = isConnected
        self.IP_ADDRESS = IP_ADDRESS
        
    def run(self):
        while(1):
            sock_data = self.SSDP_SOCK.recv(10240)
            self.parseSocketData(sock_data)
            
    def parseSocketData(self, socketData):
        if "Raspberry" in socketData:
            pattern = re.compile(r'(?<=\[)(.*?)(?=\])', flags = re.DOTALL)
            leaseTime = re.compile(r'(?<=\&)(.*?)(?=\&)', flags = re.DOTALL)
            lease = leaseTime.findall(socketData)
            results = pattern.findall(socketData)
            if results not in self.dPis:
                self.dPis.append(results)
                # Move this to another thread 
                # ensure that no packets are missed.
                sql.insertPi(results[0], 1, lease[0])
            elif results in self.dPis:
                sql.equalsLease(results[0], "100")
        elif "PiControl" in socketData:
            print("PiControl Message Received")
            pattern = re.compile(r'(?<=\[)(.*?)(?=\])', flags = re.DOTALL)
            results = pattern.findall(socketData)
            if self.isConnected: 
                print("This Pi is already connected")
                return
            else:
                
                if results[0] not in self.IP_ADDRESS:
                    self.connect_IP = results[0]
                    self.isConnected = True
                    control.testServer()
                    return
#        elif "Message" in socketData:
#            print("Message Received")
#            print(socketData)
#        else:
#            print(socketData)