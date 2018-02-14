'''
Created on 14.02.2018

@author: Fynn
'''
import xml.etree.cElementTree as ET

class Data:
    
    #def __init__(self):
        
    
    response='Start m1 1233 t1 0.343 h1 0.923 time 08:33:24 date 11.02.2018'
    names = ['m1','t1','h1','l1','time','date']
    
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