import numpy as np
from scipy.io import wavfile

def touche_octave(note:str):
    l=["C","c","D","d","E","F","f","G","g","A","a","B"]
    L=len(l)
    for i in range (L):
        if note==l[i]:
            return i
    return -1
        
def touche_piano(s:str,k:int):
    t=touche_octave(s)
    if t==-1:
        n=-1
    else:
        n=t-8+k*12
    return n

def partition(PARTITION:str):
    i=0
    k=0
    l=[]
    for i in range(int(len(PARTITION)/3)):
        note=touche_piano(PARTITION[k],int(PARTITION[k+1]))                              
        duree=(int(PARTITION[k+2])/8)
        l=l+(note,duree)
        k=k+3
    return PARTITION

def  partition(PARTITION:str):
    i=0
    k=0
    l=[]
    for i in range (int(len(PARTITION)/3)):
        note=touche_piano(PARTITION[k],int(PARTITION[k+1]))                              
        duree=int(PARTITION[k+2])/8
        l.append((note,duree))
        k=k+3
    return l

print(partition("C41D41E41F41G41A41B41C51B41A41G41F41E41D41C41"))