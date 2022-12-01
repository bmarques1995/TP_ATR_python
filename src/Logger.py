from time import sleep
from threading import Thread, Lock
from Clock import Clock
from datetime import datetime

class Logger(Thread):
    def __init__(self, engines):
        Thread.__init__(self)
        self.Engines = engines
        self.Log = open("Log.txt", "w")
        self.ShouldClose = False
        self.Clock = Clock()

    def run(self):
        self.Run()
    
    def Run(self):
        while (not self.ShouldClose):
            self.Clock.Start()
            self.WriteMessage()
            self.Clock.Wait(1000000)
        
    
    def Close(self):
        mutex = Lock()
        mutex.acquire()
        self.ShouldClose = True
        mutex.release()

    def WriteMessage(self):
        self.Log.write("[%s] Valor dos Motores\n" %datetime.now())
        for e in self.Engines:
            a, b = e.GetCurrentOutput()
            self.Log.write("Motor: %s -> %lf\n" % ((e.ID+1), b))