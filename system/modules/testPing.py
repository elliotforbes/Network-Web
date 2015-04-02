import shlex
from subprocess import Popen, PIPE, STDOUT
import sys
import os

def get_simple_cmd_output(cmd, stderr=STDOUT):
    
    args = shlex.split(cmd)
    return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0]

def check_ping():
    hostname = "192.168.1.104"
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus

if __name__ == "__main__":
    check_ping()