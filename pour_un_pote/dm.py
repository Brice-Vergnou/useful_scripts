# Nom, prénom et classe en dessous
# Nom : Hugo    
# Prénom : Barrat
# Classe :

# Importation des librairies
import numpy as np
from scipy.io import wavfile
from math import pi

# Votre dm ci-dessous ...

# ** Problème 1 - Mélodie MIDI



def freq_touche(n:int):
    if 0<n<89:
        return 2**((n-49)/12)*440
    else:
        return 0

def abs(x:float):
    if x<0:
        x=-x
    return x

def approx_pi(n):
    pn = 0
    for i in range(n+1):
        pn = pn + (-3)**(-i)/(2*i+1)
    pn = pn * 12**(0.5)
    return pn


def approx_sin(x, n):
    snx = x # s_0 = x
    result = snx
    for i in range(1, n+1):
        snx =  - snx*(x**2)/(2*n*(2*n+1))
        result = result + snx
    return result

def discretisation(a:float,b:float,n:int):
    if a>=b:
        return "a doit être strictement inférieur à b et n supérieur ou égal à 2"
    else:
        N=n-1
        c=(b-a)/N
        l=[a]
        for i in range (N):
            a=a+c
            l.append(a)
        return l
    
def echantillonnage_note(frequence,duree,hertz,amplitude):
    temps = discretisation(0,2, int(duree/hertz))
    print(temps)
    l = []
    for t in temps:
        l.append(amplitude*np.sin(2*approx_pi(40)*frequence*t))
    return l



print(approx_pi(40)) 
print(approx_pi(100)) 
print(approx_pi(1000))
print(approx_pi(100000))
y = echantillonnage_note(440, 2, 1/10, 2)

import matplotlib.pyplot as plt

x = list(range(len(y)))
plt.plot(x,y)
plt.show()



# ** Problème 2 - Chiffrement par Décalage
