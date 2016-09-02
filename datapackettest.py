import datapacket
import unittest
import struct

class datapackettest(unittest.TestCase):
    '''Tests encoding and decoding in a data packet as well
    as failures associated with each call.
    '''

    def test_initialization(self):
        temp = datapacket.DataPacket()
        self.assertEquals(temp.sequence,0)
        self.assertEquals(temp.dataBytes,0)
        self.assertEquals(temp.appData,'')
        
    def test_encode(self):
        temp = datapacket.DataPacket()
        tempstr = '0|9|abcdefghi'
        temp.encode(tempstr)
        self.assertEquals(temp.sequence,0)
        self.assertEquals(temp.dataBytes,9)
        self.assertEquals(temp.appData,'abcdefghi')
        
    def test_decode(self):
        temp = datapacket.DataPacket()
        compstr = '0|5|abcde'
        temp.encode(compstr)
        retstr = temp.decode()
        self.assertEquals(temp.sequence, 0)
        self.assertEquals(temp.dataBytes, 5)
        self.assertEquals(temp.appData, 'abcde')
        self.assertEquals(retstr, compstr)
        
if __name__ == '__main__':
    unittest.main()
        