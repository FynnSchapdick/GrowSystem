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

a = response.find('m1')
b = response.find('t1')
c = response.find('h1')
d = response.find('l1')
e = response.find('time')
f = response.find('date')

a2 = response.find('m1:') + 1

print(a+b+c+d+e+f+a2)


    
#root = ET.Element("root")
#doc = ET.SubElement(root, "doc")

#ET.SubElement(doc, "field1", name="blah").text = "some value1"
#ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

#tree = ET.ElementTree(root)
#tree.write("filename.xml")