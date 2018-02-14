'''
Created on 11.02.2018

@author: Fynn
'''

import Tkinter as tk
import Data
from Arduino import Arduino
from Data import Data

LARGE_FONT = ("Verdana", 12)

class GrowSystemapp(tk.Tk):
    
    def __init__(self,*args,**kwargs):
        
        tk.Tk.__init__(self,*args,**kwargs)
        
        #tk.Tk.iconbitmap(self, default="C:\Users\Fynn\Downloads\2014-11-13_15-23-06-546.png")
        tk.Tk.wm_title(self, 'GrowSystem 0.0.1')
        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageMeasurements):
                
            frame = F(container, self)
            
            self.frames[F] = frame
            
            frame.grid(row=0,column=0,sticky="nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        
        frame.tkraise()
                
                
           
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Grow System", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self,text="Measurements",command=lambda: controller.show_frame(PageMeasurements))
        button1.pack()
        
class PageMeasurements(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Measurements", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        #containerM = tk.Frame(self)
        
        button1 = tk.Button(self,text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button2 = tk.Button(self,text="Reading Data...",command=lambda: Arduino.readData(self))
        button3 = tk.Button(self,text="Write to XML",command=lambda: Data.prettyXml(self))
        

        button1.pack()
        button2.pack()
        button3.pack()
        
        
        
app = GrowSystemapp()
app.mainloop()
