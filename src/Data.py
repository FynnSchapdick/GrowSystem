'''
Created on 31.01.2018

@author: Fynn
@version: 0.0.1
'''

"""
    Class Data
        recieveData() ***
        addData(time,temperature,humidity,light) ***
        getTemperature(datetime) ***
        getHumidity(datetime)
        getisLightON(datetime)
        getTime()
        getIsDry(datetime)
        deleteData(datetime) ***
        getList() ***

"""

import sqlite3
import RPi.GPIO as GPIO
import sys
import Adafruit_DHT
import datetime
import time


class Data:
   
    """
    
    Constructor which prepares access to Database
    
    """
    def __init__(self):
        
        path = "/home/pi/data.db"
        self.conn = sqlite3.connect(path)
        self.c = self.conn.cursor()
        

    """
    
    Destructor which closes access to database
    
    """    
    def __del__(self):
        self.conn.close()

    
    """
    
    Recieves data from Sensors
    
    """
    def recieveData(self):
        dht_PIN = 4
        lightisOn_PIN = 17
        isDry_PIN = 27
        
        #GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(dht_PIN,GPIO.IN)
        GPIO.setup(lightisOn_PIN,GPIO.IN)
        GPIO.setup(isDry_PIN,GPIO.IN)
        
        list = []
        d = time.strftime("%d-%m-%Y %a %H:%M:%S", time.localtime())
        #d = datetime.datetime.now()
        h, t = Adafruit_DHT.read_retry(11, dht_PIN)
        w = GPIO.input(isDry_PIN)
        l = GPIO.input(lightisOn_PIN)
        if(l!=1):
            l=1
        else:
            l=0
        #print('Datetime:',d,'Temp:',t,'Humidity:',h,'LightON:',l,'isDry:',w)
            
        list.append(d)
        list.append(h)
        list.append(t)
        list.append(l)
        list.append(w)    
        Data.addData(self,d,t,h,l,w)
        return list
    
        
    """
    
    Add data to database
    
    """
    def addData(self,datetime,temperature,humidity,light,water):
        #Checking params datatype
        assert(isinstance(datetime, str))
        assert(isinstance(temperature, float))
        assert(isinstance(humidity, float))
        assert(isinstance(light,int))
        assert(isinstance(water, int))
        
        params = (datetime,temperature,humidity,light,water)
        sql = "INSERT INTO Datalist VALUES (NULL,?,?,?,?,?)"
        self.c.execute(sql,params)
        self.conn.commit()
        
        
    """
    
    Get temperature by given datetime
    
    """        
    def getTemperature(self,datetime):
        assert(isinstance(datetime, str))
        list = []
        params = (datetime,)
        sql = "SELECT TEMPERATURE, DATE FROM \
        Datalist WHERE DATE = ?"
        self.c.execute(sql,params)
        for row in self.c.fetchall():
            list.append(str(row[0]))
        return list    
    
    
    """
    
    Deletes data on database by given datetime
    
    """
    def deleteData(self,datetime):
        #Checking params datatype
        assert(isinstance(datetime, str))
        params = (datetime,)
        sql = "DELETE FROM Datalist WHERE DATE = ? "
        self.c.execute(sql,params)
        self.conn.commit()
       
        
    """
    
    Returns all data from database
    
    """
    def getList(self):
        sql = "SELECT * FROM Datalist"
        self.c.execute(sql)
        return self.c.fetchall()