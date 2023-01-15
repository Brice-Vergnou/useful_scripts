# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 08:21:11 2022

@author: bvergnou
"""

def bin2int(binaire):
    s = 0
    for i, e in enumerate(binaire[::-1]):
        s += e * 2 ** i
    return s

def int2bin(entier):
    binaire = ()
    while entier != 0:
        entier, r = entier//2, entier%2
        binaire = (r,) + binaire
    while len(binaire) < 8:
        binaire = (0,) + binaire
    return binaire

def oppose(binaire):
    tuple_bin=()
    for e in binaire:
        tuple_bin =  tuple_bin + (abs(e-1),)
    carry = 1
    returned_tuple = ()
    for e in tuple_bin[::-1]:
        result = carry + e
        carry = 0
        if result == 2:
            result = 0
            carry = 1
        returned_tuple =  (result,) + returned_tuple
    return returned_tuple

def somme(binaire_1, binaire_2):
    carry = 0
    result = ()
    n = len(binaire_1)
    for i in range(n):
        indice = n-i-1
        digit_to_add = binaire_1[indice] + binaire_2[indice]+carry
        carry = 0
        if digit_to_add > 1:
            carry = 1
            digit_to_add -= 2
        result = (digit_to_add,) + result
    return result
        
def difference(binaire_1, binaire_2):
    binaire_2 = oppose(binaire_2)
    return somme(binaire_1, binaire_2)