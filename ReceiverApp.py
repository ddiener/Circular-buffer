import socket
import circularbuffer
import threading

class ReceiverApp(threading.Thread):     
    def __init__(self, file):
        threading.Thread.__init__(self)
        self.circ = circularbuffer.CircularBuffer(5000)
        self.file = open(file, 'w')
        
    def run(self):
        UDP_IP = 'localhost'
        UDP_PORT = 6969
             
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.bind((UDP_IP, UDP_PORT))
        # circ = circularbuffer.CircularBuffer(500)
        
        while True:
            data = sock.recvfrom(1024) # buffer size is 1024 bytes
            # print "received message:", data
            self.circ.insert(data)
            
            if self.circ.hasLine():
                line = self.circ.getLine()
                #print(line)
                line = line + '\n'
                print(line)
                # split('1')[0] doesnt work!
                self.file.write(line)
            
            
            # message = 'Sending message back: ' + data
            # sock.sendto(message, (UDP_IP, UDP_PORT))