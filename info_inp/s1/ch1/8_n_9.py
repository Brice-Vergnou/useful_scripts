# Script 8

secondes = int(input("Nombre de secondes : "))
heures = secondes//3600
secondes-= heures*3600
minutes = secondes//60
secondes-=minutes*60
print(f"{heures}h {minutes}min {secondes}s")

# Script 9 - v1

x=1
y=2
print("Initialement : ")
print(f'x "contient" {x}')
print(f'y "contient" {y}')

z=x
x=y
y=z

print("Après")
print(f'x "contient" {x}')
print(f'y "contient" {y}')

# Script 9 - v2

x=1
y=2
print("Initialement : ")
print(f'x "contient" {x}')
print(f'y "contient" {y}')

x,y = y,x

print("Après")
print(f'x "contient" {x}')
print(f'y "contient" {y}')