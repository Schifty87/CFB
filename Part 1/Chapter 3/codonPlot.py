from starts import *
import matplotlib.pyplot as plt

myXcoords = [0, 0.5, 1.0, 1.5]
myYcoords = [10, 12, 6, 23]

plt.plot(myXcoords, myYcoords)
plt.show()


'''def plotStartCodons(length, trials, steps):
    myXcoords = []
    myYcoords = []
    step = 0
    for index in range(steps):
        step = step + index
        GCcontent = step / steps
        frequency = startCodons(0.5, length, trials)
        myXcoords.append(GCcontent)
        myYcoords.append(frequency)
    plt.plot(myXcoords, myYcoords)
    plt.show()

plotStartCodons(100,3,10)'''