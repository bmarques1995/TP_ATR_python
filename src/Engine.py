from threading import Thread, Lock
from Clock import Clock

class Engine(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.ID = id
        self.ShouldClose = False

        self.InputVoltage = 0.0

        self.previousOutput_2 = 0.0
        self.previousOutput = 0.0
        self.previousInput_2 = 0.0
        self.previousInput = 0.0
    
        self.Output = 0.0

        self.closedLoopPreviousInput = 0.0
        self.closedLoopPreviousInput_2 = 0.0
        self.closedLoopPreviousInput_3 = 0.0
        self.closedLoopPreviousInput_4 = 0.0
        self.closedLoopPreviousOutput = 0.0
        self.closedLoopPreviousOutput_2 = 0.0
        self.closedLoopPreviousOutput_3 = 0.0
        self.closedLoopPreviousOutput_4 = 0.0

        self.CLOutput = 0.0

        self.CLClock = Clock()
        self.Clock = Clock()

    def run(self):
       self.RunClosedLoop()

    def Close(self):
        mutex = Lock()
        mutex.acquire()
        self.ShouldClose = True
        mutex.release()

    def RunOpenLoop(self):
        while(not self.ShouldClose):
            self.Clock.Start()
            self.RunSetpoint()
            self.previousOutput_2 = self.previousOutput
            self.previousInput_2 = self.previousInput
            
            mutex = Lock()
            mutex.acquire()
            self.previousOutput = self.Output
            self.previousInput = self.InputVoltage
            mutex.release()

            self.Clock.Wait(100)

    def RunClosedLoop(self):
        while(not self.ShouldClose):
            self.CLClock.Start()
            self.RunControllerSetpoint()
            self.closedLoopPreviousOutput_4 = self.closedLoopPreviousOutput_3
            self.closedLoopPreviousOutput_3 = self.closedLoopPreviousOutput_2
            self.closedLoopPreviousOutput_2 = self.closedLoopPreviousOutput
            

            self.closedLoopPreviousInput_4 = self.closedLoopPreviousInput_3
            self.closedLoopPreviousInput_3 = self.closedLoopPreviousInput_2
            self.closedLoopPreviousInput_2 = self.closedLoopPreviousInput

            mutex = Lock()
            mutex.acquire()
            self.closedLoopPreviousOutput = self.CLOutput
            self.closedLoopPreviousInput = self.InputVoltage
            mutex.release()
            self.CLClock.Wait(100)

    def SetOperationPoint(self, setpoint):
        mutex = Lock()
        mutex.acquire()
        self.InputVoltage = setpoint
        mutex.release()

    def GetCurrentOutput(self):
        mutex = Lock()
        mutex.acquire()
        returner = (self.Output, self.CLOutput)
        mutex.release()
        return returner

    def RunSetpoint(self):
        mutex = Lock()
        mutex.acquire()
        self.Output = 5.791e-3 * self.previousInput + 5.6e-3 * self.previousInput_2 + 1.881 * self.previousOutput - .9039 * self.previousOutput_2
        mutex.release()

    def RunControllerSetpoint(self):
        mutex = Lock()
        mutex.acquire()
        self.CLOutput = (3.016371462331317e-5 * self.closedLoopPreviousInput)-(2.779380572792714e-5 * self.closedLoopPreviousInput_2)-(2.755875792115101e-5 * self.closedLoopPreviousInput_3)+(2.660093181529176e-5 * self.closedLoopPreviousInput_4) +	(3.856305699571215 * self.closedLoopPreviousOutput) -(5.594856146288695 * self.closedLoopPreviousOutput_2) +(3.620215671198946 * self.closedLoopPreviousOutput_3) -(0.881668048647046 * self.closedLoopPreviousOutput_4)
        mutex.release()