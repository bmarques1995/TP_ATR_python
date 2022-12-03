import socket
from threading import Thread, Lock
from Clock import Clock

class Server(Thread):
    def __init__(self, buf_len, host):
        print("Server mode")
        Thread.__init__(self)
        self.Host = host
        self.Port = 5985
        self.BufLen = int(buf_len)
        self.ShouldClose = False
        self.Clock = Clock()
        self.UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.UDP.bind((self.Host, self.Port))
    
    def Close(self):
        mutex = Lock()
        mutex.acquire()
        self.ShouldClose = True
        mutex.release()

    def run(self):
        self.Run()

    def Run(self):
        while(not self.ShouldClose):
            answer = self.UDP.recvfrom(self.BufLen)
            print(answer[0].decode())
            self.UDP.sendto("Returner".encode(), answer[1])