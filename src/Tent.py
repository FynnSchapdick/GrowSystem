'''
Created on 31.01.2018

@author: Fynn
@version: 0.0.1
'''

from Plant import Plant

class Tent:
    
    
    def __init__(self,tentID=0,t=0.0,h=0.0,f=0,plist=[]):
        self.id = tentID # Muss eindeutig sein
        self.temperature = t  # in Grad Celsius
        self.humidity =  h # in Prozent
        self.fanspeed =  f# in Umdrehungen pro Minute
        self.list = plist
    
    
    def newPlant(self):
        self.list.append(Plant)
    
    
        
    
    
        
        
        
