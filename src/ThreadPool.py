from Controller import Controller
from Logger import Logger
from CLI import CLI
from threading import Thread, Lock

class ThreadPool(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.Controller = Controller()
        self.Controller.start()
        self.Logger = Logger(self.Controller.GetEngines())
        self.Logger.start()
        self.CLI = CLI(self.Controller)
        self.CLI.start()

    def run(self):
        pass

    def Stop(self):
        self.CLI.Close()
        self.CLI.join()
        self.Logger.Close()
        self.Logger.join()
        self.Controller.Close()
        self.Controller.join()
