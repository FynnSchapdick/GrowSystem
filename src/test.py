'''
Created on 04.02.2018

@author: Fynn
'''
from Pflanze import Pflanze

p = Pflanze() #Erzeugt ein Objekt Plfanze
#print(p.id)
#print(p.avg)
p.setId(1010101)
p.neuePflanze(Pflanze.liste, p)


for Pflanze in Pflanze.liste:
    print(Pflanze.id)
    




