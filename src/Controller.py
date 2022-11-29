import time
from Engine import Engine

class Controller:
    def __init__(self):
        self.Engines = []
        for i in range(30):
            e = Engine(i)
            e.start()
            e.SetOperationPoint(1.0)
            self.Engines.append(e)


    def Run(self):
        time.sleep(30)
        for e in self.Engines:
            e.Close()
            e.join()
            
    def SetOperationPoint(self, setpoint):
        for e in self.Engines:
            e.SetOperationPoint(setpoint)
   