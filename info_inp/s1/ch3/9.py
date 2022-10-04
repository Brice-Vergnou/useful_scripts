def count(chaine):
    s = 0
    for char in chaine:
        if "a" == char:
            s+= 1
    return s


def count_ones(nombre):
    s = 0
    for char in str(nombre):
        if "1" == char:
            s+= 1
    return s


def count_ones_suite(n):
    chaine = ''
    for nombre in range(1,n+1):
        chaine+= str(nombre)
    return count_ones(chaine)



print(count("Happy new year"))
print(count_ones(21561141))
print(count_ones_suite(9999))