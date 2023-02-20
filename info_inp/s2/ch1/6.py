import matplotlib.pyplot as plt
from math import pi, cos, sin

def polygone(n):
    old = [0,0]
    somme_angle = (n-2)*pi
    angle_par_sommet  = somme_angle / n
    theta = (pi)-angle_par_sommet
    for i in range(1,n+1):
        new = [old[0]+cos(i*theta),old[1]+sin(i*theta)]
        plt.plot([old[0],new[0]],[old[1],new[1]], "black")
        print(theta,old,new)
        old = new
    plt.axis("off")
    plt.show()

polygone(4)