import client
import time
import thread
from threading import Thread, Event
import socket
import sys


def main():
        
    # list of total discovered Raspberry Pis found on the network.
    dPis = []

    advertised = False
    
    # Starts the thread that constantly listens for new
    # additions to the network.
    listen = client.Listen(dPis)
    # Initializes the advertise thread
    advertise = client.Advertise(advertised)
    
    control = client.Control(dPis, advertised)
    
    info = client.InfoClass()
    
    # Starts the Listening Thread
    listen.start()
    # Starts the Advertising Thread
    advertise.start()
#    while(advertised):
        # Starts the Control Thread
    control.start()
    
    while(1):
        if (control.is_alive()) is False:
            listen.quit()
            advertise.quit()
            sys.exit()
    
#    listenThread = threading.Thread(c1.listenThread())
#    listenThread.start()
    
#    c1.discoverySend()
#    c1.listenThread()
    
if __name__ == "__main__":
    main()
