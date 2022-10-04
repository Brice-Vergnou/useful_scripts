def degree2(a,b,c):
    d = b**4 - 4*a*c
    if d > 0:
        return (-b-d**0.5)/(2*a) , (-b+d**0.5)/(2*a)
    if d == 0:
        return -b/(2*a)
    if d < 0:
        return complex(-b,-(abs(d)**0.5))/(2*a), complex(-b,+(abs(d)**0.5))/(2*a)

print("Nous allons calculer les racines d'un polynôme du second degré")
a = int(input("Coefficient du x² : "))
b = int(input("Coefficient du x : "))
c = int(input("Nombre réel : "))
print(degree2(a,b,c))