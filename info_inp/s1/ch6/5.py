# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 14:20:07 2022

@author: bvergnou
"""

import matplotlib . pyplot as plt
import numpy as np


"""

def dichotomie_n(f, a, b, n):
    for _ in range(i):
        m = (a+b)/2
        if f(a)*f(m) <= 0 :
            b = m
        else :
            a = m
    return m

a = 0
b = 100
n = 50
f = lambda x : x**2-2
N = []
precisions_eff = []
precisions_th = []
for i in range(1,n):
    N.append(i)
    resultat = dichotomie_n(f, a, b, i)
    precisions_eff.append(abs(resultat -2**0.5))
    precisions_th.append(abs(a-b)/2**i)

plt.plot(N, precisions_th , "r", label =" Precision theorique ")
plt.plot(N, precisions_eff , "b", label =" Precision effective ")
plt.grid()
plt.yscale('log')
plt.legend()
plt.show()

"""

def dichotomie_extr_n(f, a, b, n):
    for _ in range(i):
        m = (a+b)/2
        if f(a)*f(m) <= 0 :
            b = m
        else :
            a = m
    if abs(f(a)) < abs(f(b)):
        return a
    else:
        return b

a = 0
b = 100
n = 50
f = lambda x : x**2-2
N = []
precisions_eff = []
precisions_th = []
for i in range(1,n):
    N.append(i)
    resultat = dichotomie_extr_n(f, a, b, i)
    precisions_eff.append(abs(resultat -2**0.5))
    precisions_th.append(abs(a-b)/2**i)

plt.plot(N, precisions_th , "r", label =" Precision theorique ")
plt.plot(N, precisions_eff , "b", label =" Precision effective ")
plt.grid()
plt.yscale('log')
plt.legend()
plt.show()