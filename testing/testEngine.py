from scapy.all import *

def pkt_callback(pkt):
    pkt.show() # debug statement

sniff(iface="eth0", prn=pkt_callback, filter="ip", store=0)