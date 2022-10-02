def is_in(liste, e):
    for ele in liste:
        if ele == e:
            return True
    return False

e = 12
liste = list(range(11))
print(is_in(liste, e) == (e in liste))
