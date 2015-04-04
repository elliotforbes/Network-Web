from scapy.all import *

for i in range(10000):
    send(IP(dst="192.168.1.104")/ICMP())
