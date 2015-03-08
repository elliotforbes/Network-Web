import socket
import struct


def getSSDPSocket():
    SSDP_PORT = 1900
    SSDP_ADDR = '239.255.255.250'

    SSDP_SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    SSDP_SOCK.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    SSDP_SOCK.bind(('', SSDP_PORT))
    mreq = struct.pack("4sl", socket.inet_aton(SSDP_ADDR), socket.INADDR_ANY)
    SSDP_SOCK.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    return SSDP_SOCK

def getIPAddress():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("google.com",80))
    IP_ADDRESS = s.getsockname()[0]
    return IP_ADDRESS

def getTCPSock():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    return sock

def returnSSDPRequest(IP_ADDRESS):
    SSDP_MX = 1
    SSDP_ST = "ssdp:all"
    SSDP_REQUEST = ('Raspberry\r\n' +
             'M-SEARCH * HTTP/1.1\r\n' +
             'MAN: "ssdp:discover"\r\n' + 
             'MX: %d\r\n' % (SSDP_MX, ) +
             'ST: %s\r\n' % (SSDP_ST, ) +
             'HOST: 239.255.255.250:1900\r\n' + 
             'IPNO: [%s]\r\n' % (IP_ADDRESS) + 
             'LEASE: &100&\r\n' +
              '\r\n')
    return SSDP_REQUEST
    