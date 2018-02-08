'''
Created on 31.01.2018

@author: Fynn
@version: 0.0.1
'''
import time


class Time(object):
    
    def __init__(self):  # Konstruktor
        
        self.datum = time.strftime("%d-%m-%Y", time.localtime())  # Attribut: Datum
        self.wochentag = time.strftime("%a", time.localtime())  # Attribut: Wochentag
        self.uhrzeit = time.strftime("%H:%M:%S" , time.localtime())  # Attribut: Uhrzeit

    
