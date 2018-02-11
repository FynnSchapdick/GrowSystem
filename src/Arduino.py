'''
Created on 04.02.2018

@author: Fynn
'''
import serial
import time
import xml.etree.cElementTree as ET
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
                if "Start" and "End" in response:
                    print(response)
                    break
        except KeyboardInterrupt:     
            board.close()
    except:
        board.close()

words = response.split('Start')
word = words[1]
words = word.split('End')
word = words[0]
words = word.split(' ')
root = ET.Element("root")
doc = ET.SubElement(root, "doc")
for i in range(0,len(words),2):
    ET.SubElement(doc,"data",name=words[i]).text = words[i+1]
tree = ET.ElementTree(root)
tree.write("data.xml")