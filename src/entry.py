from ThreadPool import ThreadPool
from time import sleep
from os import fork

def main():
    newpid = fork()
    if newpid == 0:
        t = ThreadPool(True)
        t.start()
        sleep(90)
        t.Stop()
    else:
        t = ThreadPool(False)
        t.start()
        sleep(90)
        t.Stop()

main()
