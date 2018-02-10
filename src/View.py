'''
Created on 10.02.2018

@author: Fynn
'''

from tkinter import *
from tkinter import ttk

class Example(Frame):
  
    def __init__(self):
        super().__init__()   
         
        self.initUI()
        
    #def initUI(self):
      

def main():
    root = Tk() #Create Instance
    root.title('GrowSytem')
    root.geometry('{}x{}'.format(600,600)) #Sets geometry 'width,'height'
    tabcontrol = ttk.Notebook(root) #Create TabControl
    tabControl = ttk.Frame(tabcontrol) #create a tab
    tabHelp = ttk.Frame(tabcontrol)
    tabcontrol.add(tabControl,text='Control') # add a tab
    tabcontrol.add(tabHelp,text='Help')
    tabcontrol.pack(expand=1,fill='both') #pack to make visible
    
   

    root.mainloop()

if __name__ == '__main__':
    main()  