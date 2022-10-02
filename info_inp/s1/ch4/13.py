def repete1(L):
    for i in range(len(L)): # on dit dès le début le nombre d'itérations à faire
        L.append(L[i])
    return None
#------------------------
def repete2(L):
    i=0
    while i<len(L): # on incrémente i, mais la len est augmenté d'autant
        L.append(L[i])
        i=i+1
    return None

def repete3(L):
    i=0
    n = len(L)
    while i<n: 
        L.append(L[i])
        i=i+1
    return None

L=[1,2,3]
repete1(L)
print(L)

L=[1,2,3]
repete3(L)
print(L)