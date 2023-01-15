from math import log, e

def logfx(u,x):
    return log(u(x))

carre = lambda x : x**2

print(logfx(carre,e)) 

def logf(u):
    return lambda x : log(u(x))

print(logf(carre)(1))
print(logf(carre)(e))

n = 2
while n <= 20:
    print(n**2)
    n = n+1
    
m = 4
n = 3

for i in range(2,n+1):
    print(f"Table de {i}")
    for j in range(1,m+1):
        print("----------")
        print(f"{i} x {j} = {i*j}")
    
for i in range(2,n+1):
    print(f"Table de {i}")
    print("----------")
    for j in range(1,m+1):
        
        print(f"{i} x {j} = {i*j}")