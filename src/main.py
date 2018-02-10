'''
Created on 31.01.2018

@author: Fynn
@version: 0.0.1
'''
import serial
import time

for com in range(0,4):
    try:
        PORT = '/dev/ttyACM' + str(com)
        BAUD = 9600
        board = serial.Serial(PORT,BAUD)
        print('Arduino erkannt an /dev/ttyACM' + str(com))
        print('Hardware: %s' % board.__str__())
        board.isOpen()
        time.sleep(5)
        board.write("Arduino")
        try:
            while True:
                response = board.readline()
                print(response)
        except KeyboardInterrupt:
            board.close()
    except:
        board.close()


    

    
    
    
    
    
    #t = Zeit()
    #print(t.datum.title())
    #print(t.datum)
    
    #p = Pflanze(1,200,300,250)
    #p.phase.startVegi()
   
    #p.phase.startBluete()
    #print(p.phase.bluete)

    
    
    
    
    #print(p.phase.vegi)
    #print(p.phase.bluete)
    #print(p.phase.vegiStart.datum)
    #print(p.phase.vegiEnde.datum)
    
    
    #z = Zelt(1,0.9,0.8,500)
    #print(z.id)
    #print(z.listePflanzen)
    #z.listePflanzen.append(p)
    #print(z.listePflanzen)