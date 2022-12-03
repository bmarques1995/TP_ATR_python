from Controller import Controller
from Logger import Logger
from Client import Client
from Server import Server
from CLI import CLI
from threading import Thread, Lock

class ThreadPool(Thread):

    def __init__(self, isChild):
        Thread.__init__(self)
        self.IsChild = isChild
        if(self.IsChild):
            self.Controller = Controller()
            self.Controller.start()
            self.Logger = Logger(self.Controller.GetEngines())
            self.Logger.start()
            self.Client = Client(512, '127.0.0.1', 5985)
            self.CLI = CLI(self.Controller, self.Client)
            self.CLI.start()
        else:
            self.Server = Server(512, '127.0.0.1')
            self.Server.start()

    def run(self):
        pass

    def Stop(self):
        if(self.IsChild):
            self.CLI.Close()
            self.CLI.join()
            self.Logger.Close()
            self.Logger.join()
            self.Controller.Close()
            self.Controller.join()
        else:
            self.Server.Close()
            self.Server.join()
