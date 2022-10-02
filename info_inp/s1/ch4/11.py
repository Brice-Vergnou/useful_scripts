def fsom(liste):
    n = 0
    for ele in liste:
        n += ele
    return n


def fmoy(liste):
    return fsom(liste)/len(liste)

def fmax(liste):
    maxi = liste[0]
    for ele in liste[1:]:
        if ele > maxi:
            maxi = ele
    return maxi

def fmin(liste):
    mini = liste[0]
    for ele in liste[1:]:
        if ele < mini:
            mini = ele
    return mini

liste = list(range(15))
print(liste)
print(fsom(liste))
print(fmoy(liste))
print(fmax(liste))
print(fmin(liste))