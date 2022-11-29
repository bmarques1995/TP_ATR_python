from Engine import Engine

def EngineSimulator(id):
    engine = Engine(id)

def main():
    y = []

    e = Engine(0)
    e.SetOperationPoint(2)

    i = 0
    while (i < 600):
    
        e.RunClosedLoop()
        y.append(e.GetCurrentOutput()[1])
        i = i+1

    i = 0
    while (i < 600):
        print("%d -> %lf" % (i,y[i]) )
        i = i+1
    

main()
