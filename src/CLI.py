from time import sleep
from threading import Thread, Lock
from Controller import Controller
from Clock import Clock

class CLI(Thread):
    def __init__(self, controller, client):
        Thread.__init__(self)
        self.Controller = controller
        self.ShouldClose = False
        self.Client = client

    def run(self):
        self.Run()

    def Run(self):
        while (not self.ShouldClose):
            newSetpoint = float(input("Digite o novo setpoint do motor: "))
            self.Controller.SetOperationPoint(newSetpoint)

    def Close(self):
        mutex = Lock()
        mutex.acquire()
        self.ShouldClose = True
        mutex.release()
    