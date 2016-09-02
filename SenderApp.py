import threading


class SenderApp(threading.Thread):

    def __init__(self, fileName, senderevent):
        self.host = ''
        self.port = 69696
        self.data = ''
        self.temp = ''
        self.fileName = fileName

        threading.Thread.__init__(self)
        self.senderevent = senderevent

    def read(self):
        with open(self.fileName, 'r') as txtFile:
            self.data=txtFile.read()

    def run(self):
        self.read()

        for i in range(0, len(self.data)):
            if i % 10 == 0 and i != 0 or self.data[i] == '\n':
                self.senderevent.clear()
                self.senderevent.wait()
                self.temp = ''
            self.temp += self.data[i]
