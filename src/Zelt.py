'''
Created on 31.01.2018

@author: Fynn
@version: 0.0.1
'''

from Pflanze import Pflanze

class Zelt:
    
    def __init__(self,zeltId=0,t=0.0,w=0.0,f=0,liste=[]):
        self.id = zeltId # Muss eindeutig sein
        self.raumtemperatur = t  # in Grad Celsius
        self.raumfeuchtigkeit =  w # in Prozent
        self.fanspeed =  f# in Umdrehungen pro Minute
        self.listePflanzen = liste
    
    def neuesZelt(self):
    
    
        
        
        