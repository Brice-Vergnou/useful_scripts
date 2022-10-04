def derive(f,x):
    return (f(x+1e-6) - f(x))/1e-6

def carre(x):
    return x**2

print(derive(carre,3))