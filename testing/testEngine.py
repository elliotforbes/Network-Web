from scapy.all import *

sniffList = []

def pkt_callback(pkt):
    pkt.show() # debug statement
    print(str(pkt.getLayer(ICMP)))
    sniffList.append(pkt)

sniffList = sniff(iface="eth0", prn=pkt_callback, filter="ip", store=0, count=10)

print(sniffList[4])