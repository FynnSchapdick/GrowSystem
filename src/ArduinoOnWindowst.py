'''
Created on 08.03.2018

@author: Fynn
'''

import serial
import time
from pip._vendor.distlib.compat import raw_input

class test:
    
    while True:
        
        
        serial1 = serial.Serial('COM3', 9600)
        val = raw_input("Enter from 0 to 3 to control LED u want:")
        serial1.write(val.encode())
        serial1.close()
    
    