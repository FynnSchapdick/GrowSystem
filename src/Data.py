'''
Created on 14.02.2018

@author: Fynn
'''
import xml.etree.cElementTree as ET
from Arduino import Arduino
import os
import time

class Data:
    
    #def __init__(self):
        
    done = False
    names = ['m1','t1','h1','l1','time','date']
    #response = Arduino.response
    response = ['Start','m1','0.123','h1','0.134','date','3.34','t1','h1','l1','time','date']
    
    def prettyXml(self,response,names):
        data = []    
        responseList = response.split(sep=' ')
        for index in range(len(names)):
            for i in range(len(responseList)):
                if (names[index]==responseList[i]):
                    data.append(responseList[i+1])
                    index+1
    
        root = ET.Element("tent")
    
        for y in range(0,len(data)):
            ET.SubElement(root,"data",name=names[y]).text=data[y]
        
        tree = ET.ElementTree(root)
        path = os.environ()
        if os.path.exists(path) == True:
            tree.write(time.strftime("%d-%m-%Y", time.localtime())+' '+ time.strftime("%H:%M:%S" , time.localtime()))
            done = True
             
        