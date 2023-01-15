def ppcm(a,b):
    n = 1
    while n / a != n // a or n / b != n // b:
        n+=1
    return n

"""
a = int(input("Pour le calcul d'un ppcm, donnez un premier naturel : "))
b = int(input("Et un deuxième : "))
print(ppcm(a,b))
"""

def pgcd(a,b):
    while a%b !=0:
        a,b = b, a%b
    return b

print(pgcd(36,4521266666226666666666666666666666666666))