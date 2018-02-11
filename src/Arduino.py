'''
Created on 04.02.2018

@author: Fynn
'''
import serial
import time
from Time import Time
for com in range(0, 4):
    try:
        PORT = '/dev/ttyACM' + str(com)
        BAUD = 9600
        board = serial.Serial(PORT, BAUD)
        print('Arduino erkannt an /dev/ttyACM' + str(com))
        print('Hardware: %s' % board.__str__())
        board.isOpen()
        time.sleep(5)
        board.write("test")
        response = ''
        try:
            while True:  
                response += board.readline() + '\n'
                if "Light:" in response:
                    print(response)
                    break
        except KeyboardInterrupt:     
                board.close()
    except:
            board.close()

