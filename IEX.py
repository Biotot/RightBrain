import matplotlib.pyplot as plt
import numpy as np
import pprint as pp


def LoadCSV(tPath):
    #Load this path of a CSV.
    print("Loading: " + tPath)

    
    inputs = np.loadtxt(tPath, delimiter=',', skiprows=1, usecols=(3,4,5,6,7,8))
    #pp.pprint(inputs)
    
    plt.figure()
    plt.plot(inputs[:,2], label="gen")
    avgList = {}
    
    for i in [5, 15, 30]:
        
        movingAvg = np.convolve(inputs[:,2], np.ones(i)/i, mode='valid')
        plt.plot(range(i, i+len(movingAvg)), movingAvg, label=i)
        avgList[i]=movingAvg
        #pp.pprint(movingAvg)

    pp.pprint(avgList)

    plt.legend(loc='upper right')
    plt.show()



