# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:11:35 2022

@author: bvergnou
"""

def racine(valeur ,epsilon=1e-12):
    a = 0
    b = 1e10
    f = lambda x: x**2 - valeur
    while b - a > 2*epsilon:
        m = (a+b)/2
        if f(m)*f(a) <= 0 :
            b = m
        else:
            a = m
    return (a+b)/2


            