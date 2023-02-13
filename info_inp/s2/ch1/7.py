import matplotlib.pyplot as plt
import numpy as np

def puissance(p):
    x = np.linspace(0,5,500)
    y = np.power(x,p)
    plt.plot(x,y,"black")
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.show()

def monomes(L):
    x = np.linspace(0,2,500)
    for e in L:
        y = np.power(x,e)
        plt.plot(x,y,label="a = "+str(e))
        plt.legend()
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.show()

for e in [0.5,1,2]:
    puissance(e)

monomes([0.2,0.5,0.8,1,2,3])