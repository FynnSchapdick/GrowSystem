'''
Created on 25.03.2018

@author: Fynn
'''
import unittest
from Data import *


class TestData (unittest.TestCase):
    
    def setUp(self):
        self.testObject = Data()
        
    def testAddData(self):
        self.testObject.addData("2018,03,25,04,36", 0.24, 0.60, False,False)
        self.assertEqual(self.testObject.getTemperature("2018,03,25,04,36")[0],"0.24")
    
    def testDeleteData(self):
        self.assertEqual(self.testObject.getTemperature("2018,03,25,04,36")[0],"0.24")
        #Delete Data
        list = []
        self.testObject.deleteData("2018,03,25,04,36")
        self.assertEqual(self.testObject.getTemperature("2018,03,25,04,36"),list)
        
    def testGetList(self):
        self.testObject.addData("2018,03,25,04,36", 0.24, 0.6, False, False)
        self.testObject.addData("2018,03,25,04,37", 0.24, 0.6, True, True)
        self.testObject.addData("2018,03,25,06,36", 0.2, 0.7, True, False)
        self.testObject.addData("2018,03,26,04,36", 0.34, 0.9, False, True)
        print self.testObject.getList()
        
    def testRecieveData(self):
        self.testObject.recieveData()
        
        
        
        
if __name__ == "__main__":
    unittest.main()
    
    
