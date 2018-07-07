import re
import os
import socket
import subprocess

def get_ip():
    '''retrieve local ip'''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def scan(device):
    result = subprocess.run(['nmap', device], stdout=subprocess.PIPE)
    out = result.stdout.decode('utf-8')
    address = re.search(r'' + device + ' \((.*?)\)', out).group(1)
    return address
