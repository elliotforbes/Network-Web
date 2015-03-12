from scapy.all import *

def pkt_callback(pkt):
    pkt.show() # debug statement
    
sniffList = []

sniffList = sniff(iface="eth0", prn=pkt_callback, filter="ip", store=0, count=10)

print(sniffList[4])