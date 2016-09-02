import SenderApp
import datapacket
import threading
import socket

currentData = ''

chokingEvent = threading.Event()
sender = SenderApp.SenderApp('CountOfMonteChristoCh1.txt', chokingEvent)
chokingEvent.set()
sender.start()
packet = datapacket.DataPacket()

UDP_IP = "localhost"
UDP_PORT = 6969

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind((UDP_IP, UDP_PORT))
# the bind is completely unnecessary?

while(1):
    if currentData != sender.temp:
        currentData = sender.temp
        packet.data = currentData
        packet.numBytes = str(len(currentData))
        packet.sequence = '69696'
        print(packet.decode())
        
        # print (sender.temp)
        sock.sendto(packet.data, (UDP_IP, UDP_PORT))
        
        # d = sock.recv(1024)
        # print(d)

    sender.senderevent.set()
