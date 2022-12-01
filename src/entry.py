from ThreadPool import ThreadPool
from time import sleep
from os import fork

def main():
    newpid = fork()
    if newpid == 0:
        print("Fork")
    else:
        t = ThreadPool()
        t.start()
        sleep(90)
        t.Stop()

main()
