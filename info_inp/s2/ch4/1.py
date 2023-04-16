####### Q1 #########

def rectg(f,n,a,b):
  h = (b-a)/n
  s= 0
  for i in range(n):
    s += f(a+i*h)
  return h*s

def rectd(f,n,a,b):
  h = (b-a)/n
  s= 0
  for i in range(1,n+1):
    s += f(a+i*h)
  return h*s

def rectm(f,n,a,b):
  h = (b-a)/n
  s= 0
  for i in range(1,n+1):
    s += f(a+i*h+h/2)
  return h*s

def trap(f,n,a,b):
  h = (b-a)/n
  s = 0
  for i in range(1,n):
    s+= f(a+i*h)
  return h*(f(a)/2+s+f(b)/2)

def simp(f,n,a,b):
  h = (b-a)/n
  s1 = 0
  s2 = f(a+h/2)
  for i in range(1,n):
    s1 += f(a+i*h)
    s2 += f(a+i*h+h/2)
  return h/6*(f(a)+2*s1+4*s2+f(b))

def integrale(meth,f,N,a,b):
  n = 1
  result = meth(f,n,a,b)
  while abs(result-meth(f,2*n,a,b)) > 10**-N:
    n *= 2
    result = meth(f,n,a,b)
  return meth(f,2*n,a,b)

########  Q2 #################
 
carre=lambda x: x**2
print(round(integrale(trap,carre,5,3,5.5),6), round(1/3*(5.5**3-3**3),6))

####### Q3 ###########

# ln 2 
from math import log

f= lambda x : 1/x
n= 15

abs( integrale(simp,f,n,1,2)- log(2) )