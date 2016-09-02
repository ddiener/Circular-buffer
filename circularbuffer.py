class CircularBuffer:
    '''
    This bytes has an infinite address space but a finite size.
    Chars are inserted at position _tail_ and removed from position _head_.
    New chars can be inserted as long as tail-head < bufsize.
    This variant is adapted for use with a TCP simulator whose receiver
    extracts lines of text from the bytes.
    '''   
    def __init__(self, bufsize):
        '''
        Initialize the Circularbytes with no data but 'bufsize' slots
        for storing data
        '''
        # actual byte position the objects array
        self._head_ = 0
        self._tail_ = 0
        
        # head and tail for this stupid count
        self.head = 0
        self.tail = 0
        
        self.bufsize = bufsize
        
        # maybe this is not the best way to create a list of a certain size
        self.bytes = [''] * bufsize
        
        
    def getLine(self):
        '''
        If bytes contains newline character '\n' at position P, returns 
        the chars from _head_ to P-1 inclusive, and discards the newline. If there 
        are multiple newlines, the characters up to the first newline are returned.
        If there are no newlines in the bytes, returns None.
        '''
        if '\n' in self.bytes:
            # temporary variable to store the returned string
            retstr = ''
            while True:
                if self.bytes[self._head_] == '\n':
                    self.bytes[self._head_] = ''
                    self._head_ = self._head_ + 1
                    self.head = self.head + 1
                    break
                else:
                    retstr = retstr + str(self.bytes[self._head_])
                    self.bytes[self._head_] = ''
                    if self._head_ == self.bufsize - 1:
                        self._head_ = 0
                        self.head = self.head + 1
                    else:
                        self._head_ = self._head_ + 1
                        self.head = self.head + 1
            
            # out of loop so the string is ready to be returned
            return retstr
        # no newline character in the byte array    
        else:
            return None
          
        
        
    def hasLine(self):
        '''
        returns True if our bytes contains a newline char,
        False otherwise.
        '''
        if '\n' in self.bytes:
            return True
        else:
            return False
        
        
    def insert(self, newdata):
        '''
        If bytes contains enough empty cells to accomodate 'newdata',
        adds 'newdata' to bytes in positions _tail_..._tail_+len(newdata) and 
        returns True. Otherwise, returns False.
        '''
        # condition that items cannot be inserted
        if self.tail - self.head < self.bufsize and self.bufsize - (self.tail - self.head) > len(newdata):
            # there are enough spaces to insert the newdata
            for char in newdata:
                if char == '\r':
                    self.tail = self.tail + 1
                    continue
                self.bytes[self._tail_] = char
                
                if self._tail_ == self.bufsize - 1:
                    self._tail_ = 0
                else:
                    self._tail_ = self._tail_ + 1
                self.tail = self.tail + 1
                    
            # out of the for loop, all characters have been inserted
            return True
        else:
            return False
                