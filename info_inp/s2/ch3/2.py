def f(k):
    epsilon = 10**-k
    u = 1
    v = u-1/3*u**4
    while abs(u-v) > epsilon:
        u = v
        v = v-1/3*u**4
    return v

for k in range(1,7):
    print(f"k={k}, valeur retournée : {f(k)}\n")
