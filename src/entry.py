from ThreadPool import ThreadPool
from time import sleep

def main():
    t = ThreadPool()
    t.start()
    sleep(7)
    t.Stop()

main()
