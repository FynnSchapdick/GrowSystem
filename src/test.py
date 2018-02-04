'''
Created on 04.02.2018

@author: Fynn
'''
import serial
import time

s = serial.Serial('/dev/ttyACM0', 9600) # Namen ggf. anpassen
s.isOpen()
time.sleep(5) # der Arduino resettet nach einer Seriellen Verbindung, daher mus$

s.write("test")
try:
    while True:
        response = s.readline()
        print(response)
except KeyboardInterrupt:
    s.close()
