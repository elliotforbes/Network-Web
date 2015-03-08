import threading
import time
import sqlEngine as sql

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
                