import struct

class AckPacket():
    def __init__(self):
        self.ackNum = 0
        self.windowSize = 0
        
    def encode(self, inputString):
        temp = inputString.split('|')
        self.ackNum = int(temp[0])
        self.windowSize = int(temp[1])
    
    def decode(self):
        temp = ''
        temp = temp + str(self.ackNum)
        temp = temp + '|'
        temp = temp + str(self.windowSize)
        return temp