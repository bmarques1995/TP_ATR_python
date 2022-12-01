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
        self.IsEngineActive = [False, True, False, True, False, False, True, False, True, False, False, True, False, True, False, False, True, False, True, False, False, True, False, True, False, False, True, False, True, False]
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
                if (self.IsEngineActive[i]):
                    self.Engines[i].SetOperationPoint(self.Setpoint)
                else:
                    self.Engines[i].SetOperationPoint(0.0)
            for i in range(30):
                activeEnginesCopy = self.IsEngineActive
                if(self.IsEngineActive):
                    self.IsEngineActive[i] = activeEnginesCopy[(i + 1) % 30]
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
    
    def GetEngines(self):
        return self.Engines
   