'''
Created on 14.02.2018

@author: Fynn
'''
import xml.etree.cElementTree as ET
from Arduino import Arduino

class Data:
    
    #def __init__(self):
        
    done = False
    names = ['m1','t1','h1','l1','time','date']
    response = Arduino.response
    
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
        tree.write("data.xml")
        done = True