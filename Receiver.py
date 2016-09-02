import ReceiverApp
#import threading

file = 'fileName.txt'

receiver = ReceiverApp.ReceiverApp(file)
receiver.start()
      
# opening file to be written to

        
#while True:
    #if(receiver.circ.hasLine()):
        #try:
            # print 'I at least tried'
            #line = receiver.circ.getLine()
            #print(line)
            #file.write(line)
        #except:
            #break
                