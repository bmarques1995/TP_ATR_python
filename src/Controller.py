from time import sleep
from threading import Thread, Lock
from Engine import Engine
from Clock import Clock

class Controller(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.Setpoint = 0.0
        self.Engines = []
        self.Clock = Clock()
        self.ActiveEngines = [1, 3, 6, 8, 11, 13, 16, 18, 21, 23, 26, 28]
        self.ShouldClose = False
        for i in range(30):
            e = Engine(i)
            e.start()
            e.SetOperationPoint(1.0)
            self.Engines.append(e)

    def run(self):
       self.Run()

    def Run(self):
        while(not self.ShouldClose):
            self.Clock.Start()
            for i in range(30):
                self.Engines[i].SetOperationPoint(0.0)
            for i in range(12):
                self.Engines[self.ActiveEngines[i]].SetOperationPoint(self.Setpoint)
            for i in range(12):
                self.ActiveEngines[i] = (self.ActiveEngines[i] + 1) % 30
            self.Clock.Wait(200000)
        for e in self.Engines:
            e.Close()
            e.join()
            
    def SetOperationPoint(self, setpoint):
        self.Setpoint = setpoint
    
    def Close(self):
        self.ShouldClose = True
        for e in self.Engines:
            e.Close()
            e.join()
   