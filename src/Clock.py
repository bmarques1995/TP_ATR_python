from time import time, sleep

class Clock:
    
    def Start(self):
        self.StartPoint = time()

    def Wait(self, waitTimeInMicroseconds):
        end = time()
        timeEllapsed = end - self.StartPoint
        while(timeEllapsed < waitTimeInMicroseconds/1000000.0):
            end = time()
            timeEllapsed = end - self.StartPoint
        
