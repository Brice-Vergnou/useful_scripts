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

x=1
y=2
print("Initialement : ")
print(f'x "contient" {x}')
print(f'y "contient" {y}')

x,y = y,x

print("Après")
print(f'x "contient" {x}')
print(f'y "contient" {y}')
