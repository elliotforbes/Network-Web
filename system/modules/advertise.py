import threading
import time 

class advertise(threading.Thread):
    
    SSDP_SOCK = None
    SSDP_REQUEST = None
    
    def __init__(self, ADVERTISE_SOCK, SSDP_REQUEST):
        super(advertise, self).__init__()
        self.SSDP_SOCK = ADVERTISE_SOCK
        self.SSDP_REQUEST = SSDP_REQUEST
        
    def run(self):
        while(1):
            time.sleep(5)
            self.SSDP_SOCK.sendto(self.SSDP_REQUEST, ("239.255.255.250", 1900))