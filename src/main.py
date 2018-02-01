'''
Created on 31.01.2018

@author: Fynn
@version: 0.0.1
'''
from Zelt import Zelt
from Zeit import Zeit
from Pflanze import Pflanze

class main():
    
    t = Zeit()
    print(t.datum.title())
    print(t.datum)
    
    p = Pflanze(1,200,300,250,(True,False))
    print(p.id)
    print(p.m1)
    print(p.avg)
    print(p.phase.vegi)
    print(p.phase.bluete)
    print(p.phase.blueteStart.datum)
    print(p.phase.blueteEnde)
    
    z = Zelt(1,0.9,0.8,500)
    print(z.id)
    
    
    
    
    
    
  
  
    
    
    