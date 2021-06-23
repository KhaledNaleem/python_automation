import sys
import subprocess
import os
from decouple import config

Network_IP = config('__netword_IP__')
Device_IP = config('__device_IP__')

proc = subprocess.Popen(['ping', Network_IP], stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    if not line:
        break
    connected_ip = line.decode('utf-8').split()[3]

    if connected_ip == Device_IP:
        subprocess.Popen(['say', 'Device Connected'])