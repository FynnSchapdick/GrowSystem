'''
Created on 01.02.2018

@author: Fynn
@version: 0.0.1
'''
from Zeit import Zeit

class Phase(object):
    
    def __init__(self,v=False,b=False):
    
        self.vegi = v
        self.bluete = b
        self.vegiStart = Zeit()
        self.vegiEnde = Zeit()
        self.blueteStart = Zeit()
        self.blueteEnde = Zeit()
        
    
    
