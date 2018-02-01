'''
Created on 31.01.2018

@author: Fynn
@version: 0.0.1
'''
from Phase import Phase
class Pflanze:
    
    def __init__(self,pflanzeId=0,m1=0.0,m2=0.0,avg=0.0,Phase): #Konstruktor
        self.id = pflanzeId #Eine einzigartige ID für jede Pflanze
        self.m1 = m1#Einen Feuchtigkeitswert #1
        self.m2 = m2#Einen Feuchtigkeitswert #2
        self.avg = avg#Einen berechneten Durchschnitt beider Werte
        self.phase = Phase(False,False) #Eine Pflanze hat eine Phase Vegi/Blüte
    def trinken(self):
        #Ansteuerung der Pumpe
        return #Ein Objekt Zeit
    
    def essen(self):
        # Ansteuerung der Pumpe
        return #Ein Objekt Zeit
    
   
    
