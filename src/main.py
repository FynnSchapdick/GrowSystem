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
    
    p = Pflanze(1,200,300,250)
    print(p.id)
    print(p.m1)
    print(p.avg)
    print(p.phase.vegi)
    print(p.phase.bluete)
    print(p.phase.vegiStart.datum)
    print(p.phase.vegiEnde.datum)
    
    
    z = Zelt(1,0.9,0.8,500)
    print(z.id)
    print(z.listePflanzen)
    z.listePflanzen.append(p)
    print(z.listePflanzen)
    
    
    
    
    
    
  
  
    
    
    