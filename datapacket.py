import struct

class DataPacket():
    def __init__(self):
        self.sequence = 0
        self.numBytes = 0
        self.data = ''
        
    def encode(self, inputString):
        retstr = inputString.split('|')
        self.sequence = int(retstr[0]) # casts to an integer
        self.numBytes = int(retstr[1]) # casts to integer
        self.data = retstr[2]
        return True
    
    def decode(self):
        retstr = ''
        retstr = retstr + str(self.sequence)
        retstr = retstr + '|'
        retstr = retstr + str(self.numBytes)
        retstr = retstr + '|'
        retstr = retstr + self.data
        return retstr
        