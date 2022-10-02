from math import cos, pi

def coord(liste):
    return [(x, cos(x)) for x in liste]

liste=[0, pi/2, pi/3, pi]
print(coord(liste))
