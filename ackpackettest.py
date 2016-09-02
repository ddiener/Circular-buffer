import ackpacket
import unittest
import struct

class ackpackettest(unittest.TestCase):
    '''Tests encoding and decoding in a data packet as well
    as failures associated with each call.
    '''

    def test_initialization(self):
        '''Tests initialization of the ack packet
        '''
        temp = ackpacket.AckPacket()
        self.assertEquals(temp.ackNum,0)
        self.assertEquals(temp.windowSize,0)
        
    def test_encode(self):
        temp = ackpacket.AckPacket()
        tempstr = '1|8'
        temp.encode(tempstr)
        self.assertEquals(temp.ackNum, 1)
        self.assertEquals(temp.windowSize, 8)
        
    def test_decode(self):
        temp = ackpacket.AckPacket()
        tempstr = '1|8'
        temp.encode(tempstr)
        self.assertEquals(temp.ackNum, 1)
        self.assertEquals(temp.windowSize, 8)
        retstr = temp.decode()
        self.assertEquals(tempstr, retstr)
        
if __name__ == '__main__':
    unittest.main()