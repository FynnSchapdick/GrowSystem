'''
Created on 01.02.2018

@author: Fynn
@version: 0.0.1
'''
from Time import Time

class Phase(object):
    
    def __init__(self,v=False,b=False):
    
        self.vegi = v
        self.bluete = b
        self.vegiStart = Time()
        self.vegiEnde = Time()
        self.blueteStart = Time()
        self.blueteEnde = Time()
        
    def startVegi(self):
        if self.bluete == False & self.vegi == False:
            self.vegi=True
            self.bluete=False
            self.vegiStart=Time()
        else:
            self.blueteEnde=Time()
            self.bluete=False
    
    def startBluete(self):
        if self.vegi==True & self.bluete==False:
            self.bluete=True
            self.vegi=False
            self.vegiEnde=Time()
            self.blueteStart=Time()
        
        
    
        
