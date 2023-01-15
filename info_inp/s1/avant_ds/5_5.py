def bin_to_int(mot):
    s = 0
    for i in range(1,len(mot)+1):
        s += mot[-i]*2**(i-1)
    return s

def int_to_bin(entier):
    t = ()
    while entier > 0:
        entier, t = entier //2,  (entier%2,) + t 
    return t
    
def oppose(mot):
    flipped_tuple = ()
    for i in range(len(mot)):
        flipped_tuple += (abs(mot[i]-1),)
    carry = 1
    returned_tuple = ()
    for ele in flipped_tuple[::-1]:
        result = ele + carry
        carry = 0
        if result > 1:
            result = 0
            carry = 1
        returned_tuple = (result,) + returned_tuple
    return returned_tuple

def somme(a,b):
    if len(a)>=len(b):
        n = len(a)
        b = (0,)*(len(a)-len(b)) + b
    else:
        n = len(b)
        a = (0,)*(len(b)-len(a)) + b
    carry = 0
    somme = ()
    for i in range(1,n+1):
        result = a[-i] + b[-i] + carry
        carry = 0
        if result > 1:
            result -= 2
            carry = 1
        somme = (result,) + somme
    return somme

def diff(a,b):
    return somme(a, oppose(b))

def signed_to_int(mot):
    return bin_to_int(mot) - 2**len(mot)
    
mot = (1,0,0,1,0,1,0,1)
mot2 = (1,0,1,1,0,1,0,0)
entier = 149
print(bin_to_int(mot), int("10010101",2))
print(int_to_bin(entier) == mot)
print(oppose(mot))
print(bin_to_int(somme(int_to_bin(84),int_to_bin(26))))
print(diff(mot,mot2))
print(signed_to_int((1, 1, 1, 0, 0, 0, 0, 1)))
print(diff((0, 0, 0, 1, 1, 0, 0, 0),(0, 0, 0, 0, 1, 1, 0, 0)))