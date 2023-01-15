from math import log

def dichotomie(f, a, b, epsilon):
    if a >= b:
        a,b = b,a
    while b-a > epsilon:
        m = (a+b)/2
        if f(m)*f(a) < 0:
            b = m
        else :
            a = m
    return (a+b)/2

carre = lambda x : x**2 - 2

def dichotomie_cond(f, a, b, epsilon):
    if a > b :
        a,b = b,a
    n = int(log((b-a)/epsilon)/log(2)) + 1
    for _ in range(n):
        m = (a+b)/2
        if f(a)*f(m) < 0:
            b = m
        else :
            a = m
    return (a+b)/2


print(dichotomie(carre, 0, 5, 1e-5))
print(dichotomie_cond(carre, 0, 5, 1e-5))