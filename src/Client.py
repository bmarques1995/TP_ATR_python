import socket
from threading import Thread, Lock
from Clock import Clock

class Client:
    def __init__(self, buf_len, host, port):
        self.Host = host
        self.Port = port
        self.BufLen = int(buf_len)
        self.UDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def Run(self,message):
        self.UDP.sendto(message.encode(), (self.Host, self.Port))
        answer = self.UDP.recvfrom(self.BufLen)
        print(answer[0].decode())