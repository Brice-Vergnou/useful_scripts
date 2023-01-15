# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:17:06 2022

@author: bvergnou
"""
from math import exp
import scipy.optimize as sc

def dichotomie(f, a, b, epsilon):
    while b-a > 2* epsilon:
        x = (a+b)/2
        if f(x)*f(a) <=0:
            b = x
        else:
            a = x
    return (a+b)/2

f = lambda x : 3-2*x-exp(-x)
a = 0
b = 10
print(dichotomie(f, a, b, 1e-15))
print(sc.bisect(f,a, b, xtol=1e-16))