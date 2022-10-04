from math import sqrt

def degree2C(a,b,c):
    delta = b**2-4*a*c
    print(delta)
    module = abs(delta)
    z_reel = sqrt((module+delta.real)/2)
    z_im = sqrt((module-delta.real)/2)
    if delta.real * delta.imag <= 0:
        z_im = -z_im
    racine_delta = complex(z_reel,z_im)
    print(racine_delta)
    if delta ==0:
        return -b/(2*a)
    else:
        return (-b+racine_delta)/(2*a), (-b-racine_delta)/(2*a)
    
a = complex(1,1)
b = complex(2,2)
c = complex(3,3)

result = degree2C(a, b, c)
z = result[0]
print(a*z**2+b*z+c)