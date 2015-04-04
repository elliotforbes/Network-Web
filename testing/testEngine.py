from scapy.all import *

tcp_syn = IP(src="192.168.1.122", dst="192.168.1.104")/TCP(dport=9000, flags="S", seq=10000)