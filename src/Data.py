'''
Created on 14.02.2018

@author: Fynn
'''
import xml.etree.cElementTree as ET
import Arduino

class Data:
    
    #def __init__(self):
        
    done = False
   
    names = ['m1','t1','h1','l1','time','date']
    
    def prettyXml(self,Arduino.response,Data.names):
        
        data = []    
        responseList = Arduino.response.split(sep=' ')
        for index in range(len(Data.names)):
            for i in range(len(responseList)):
                if (Data.names[index]==responseList[i]):
                    data.append(responseList[i+1])
                    index+1
    
                    root = ET.Element("tent")
    
        for y in range(0,len(data)):
            ET.SubElement(root,"data",name=Data.names[y]).text=data[y]
        
        tree = ET.ElementTree(root)
        tree.write("data.xml")
        done = True