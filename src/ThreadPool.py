from Controller import Controller
from threading import Thread, Lock

class ThreadPool(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.Controller = Controller()
        self.Controller.start()

    def run(self):
        pass

    def Stop(self):
        self.Controller.Close()
        self.Controller.join()
