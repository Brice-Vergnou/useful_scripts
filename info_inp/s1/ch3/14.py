def ordre(x):
    n = 0
    while not(10**n <= abs(x) < 10**(n+1)):
        n+=1
    return n

x = 1e39
print(ordre(x))
