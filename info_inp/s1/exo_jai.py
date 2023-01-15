from random import sample
import numpy as np
import matplotlib.pyplot as plt

    

def jai(n, epsilon):
    """
    algo un peu foireux pour visualiser 
    la modélisation de l'exo avec la course de jai

    Args:
        2 <= n (int) <= 120 : nombre d'étapes en tout
    """
    x = [0]
    y = [0]
    y_range = sample(range(0,120), n-2)
    y_numbers = [e / 10 for e in y_range]
    y = [0] + sorted(y_numbers) + [12]
    x = np.linspace(0,60,n)
    
    def f(x, set_of_x, set_of_y):
        if x == 60:
            return 12
        elif x == 0:
            return 0
        else:
            i = 0
            while not(set_of_x[i+1] >= x >= set_of_x[i]):
                i += 1
            # print(f"{x} est entre {set_of_x[i]} et {set_of_x[i+1]} à {x/set_of_x[i+1]}%, donc on trouve {(set_of_y[i+1])*(x/set_of_x[i+1])} entre {set_of_y[i]} et {set_of_y[i+1]}")
            return (set_of_y[i+1])*(x/set_of_x[i+1])
     
    g = lambda a,b : f(b,x,y) - f(a,x,y) - 6
    
    
    a = 0
    b = 30
    while abs(g(a,b))> epsilon:
        a,b = a+ epsilon/10, b + epsilon/10
        print(g(a,b))
    
    abscisses = np.linspace(0,60,1000)
    ordo = [f(val,x,y) for val in abscisses]
    plt.plot(abscisses,ordo)
    plt.plot([b,b], [0, f(b,x,y)], 'k-', lw=2)
    plt.plot([0,b], [f(b,x,y), f(b,x,y)], 'k-', lw=2)
    plt.plot([a,a], [0, f(a,x,y)],'k-', lw=2)
    plt.plot([0,a], [f(a,x,y), f(a,x,y)],'k-', lw=2)
    plt.show()
    return a,b, g(a,b)

print(jai(60,0.01))