# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 11:47:01 2022

@author: bvergnou
"""
from math import log,ceil

def dichotomie(f, a, b, epsilon):
    # a < b
    x = a
    y = b
    while y - x > 2*epsilon:
        print(x,y)
        m = (x+y)/2
        if f(x)*f(m) <= 0:
            y = m
        else:
            x= m
    return (x+y) / 2

def dichotomie_extr(f, a, b, epsilon):
    # a < b
    x = a
    y = b
    while y - x > 2*epsilon:
        m = (x+y)/2
        if f(x)*f(m) <= 0:
            y = m
        else:
            x= m
    
    if abs(f(x)) < abs(f(y)):
        return x
    else :
        return y
    
def dichotomie_cond(f,a,b,epsilon):
    x = a
    y = b
    for _ in range(ceil(log(1/epsilon*(b-a),2))+1):
        m = (x+y)/2
        if f(x)*f(m) <= 0:
            y = m
        else:
            x= m
    return (x+y) / 2
        
        
carre = lambda x : x**2 - 2