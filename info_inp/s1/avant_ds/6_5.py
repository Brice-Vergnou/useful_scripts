import matplotlib.pyplot as plt
import numpy as np

def dichotomie_n(f,a,b,n):
    for i in range(n):
        m = (a+b)/2
        if f(m)*f(a) < 0:
            b = m
        else:
            a= m
    return (a+b)/2


def dichotomie_2(f, a, b, n):
    for _ in range(n):
        m = (a+b)/2
        if f(a)*f(m) < 0:
            b = m
        else :
            a = m
    if abs(f(a)) < abs(f(b)):
        return a
    else:
        return b

carre = lambda x : x**2 -2


N = []
precisions_th = []
precisions_eff = []

for i in range(1,51):
    N.append(i)
    resultat = dichotomie_n(carre,0,4,i)
    precisions_th.append(4/2**i)
    precisions_eff.append(abs(2**0.5-resultat))

plt.plot(N, precisions_th , "r", label="Precision theorique")
plt.plot(N, precisions_eff , "b", label="Precision effective")
plt.grid()
plt.yscale('log')
plt.legend ()
plt.show()