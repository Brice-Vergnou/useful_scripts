from math import log, exp

def somme(f,g):
    s=lambda x : f(x)+g(x)
    return s

i = lambda x:x

d = somme(i,i)
print(d(1),d(2)) # x-> 2x

f1 = lambda x:x/2
f2 = d


def produit(f,g):
    return lambda x:f(x)*g(x)
produit = lambda f,g : lambda x: f(x)*g(x)

print(produit(f1,f2)(3))

def compose(f,g):
    return lambda x: f(g(x))

test = compose(exp, log)
print(test(5))