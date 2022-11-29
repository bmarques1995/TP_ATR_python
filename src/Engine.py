class Engine:
    def __init__(self, id):
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

    def RunOpenLoop(self):
        self.RunSetpoint()
        self.previousOutput_2 = self.previousOutput
        self.previousOutput = self.Output
        self.previousInput_2 = self.previousInput
        self.previousInput = self.InputVoltage

    def RunClosedLoop(self):
        self.RunControllerSetpoint()
        self.closedLoopPreviousOutput_4 = self.closedLoopPreviousOutput_3
        self.closedLoopPreviousOutput_3 = self.closedLoopPreviousOutput_2
        self.closedLoopPreviousOutput_2 = self.closedLoopPreviousOutput
        self.closedLoopPreviousOutput = self.CLOutput

        self.closedLoopPreviousInput_4 = self.closedLoopPreviousInput_3
        self.closedLoopPreviousInput_3 = self.closedLoopPreviousInput_2
        self.closedLoopPreviousInput_2 = self.closedLoopPreviousInput
        self.closedLoopPreviousInput = self.InputVoltage

    def SetOperationPoint(self, setpoint):
        self.InputVoltage = setpoint

    def GetCurrentOutput(self):
        return (self.Output, self.CLOutput)

    def RunSetpoint(self):
        self.Output = 5.791e-3 * self.previousInput + 5.6e-3 * self.previousInput_2 + 1.881 * self.previousOutput - .9039 * self.previousOutput_2
    
    def RunControllerSetpoint(self):
        self.CLOutput = (3.016371462331317e-5 * self.closedLoopPreviousInput)-(2.779380572792714e-5 * self.closedLoopPreviousInput_2)-(2.755875792115101e-5 * self.closedLoopPreviousInput_3)+(2.660093181529176e-5 * self.closedLoopPreviousInput_4) +	(3.856305699571215 * self.closedLoopPreviousOutput) -(5.594856146288695 * self.closedLoopPreviousOutput_2) +(3.620215671198946 * self.closedLoopPreviousOutput_3) -(0.881668048647046 * self.closedLoopPreviousOutput_4)