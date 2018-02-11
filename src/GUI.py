'''
Created on 11.02.2018

@author: Fynn
'''
import Arduino as getData
import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class GrowSystemapp(tk.Tk):
    
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        
        container.pack(side="top",fill="both",expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        frame = StartPage(container, self)
        
        self.frames[StartPage] = frame
        
        frame.grid(row=0,column=0,sticky="nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        
        frame.tkraise()
                
                
    def qf(self):
        getData()
           
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="Grow System", font=LARGE_FONT)
        
        label.pack(pady=10,padx=10)
        
        button1 = tk.Button(self,text="Getting Values",command=GrowSystemapp.qf())
        button1.pack()
        
        
        
        
app = GrowSystemapp()
app.mainloop()
