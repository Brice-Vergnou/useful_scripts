from math import log, e

def logfx(u, x):
    return log(u(x))

def carre(x):
    return x**2

def logf(u):
    return lambda x: log(u(x))


print(logfx(carre,e))
print(logf(carre)(e))