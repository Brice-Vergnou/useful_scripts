def compte(liste, e):
    s = 0
    for ele in liste:
        if e == ele:
            s+=1
    return s

liste=["pomme","pomme","poire","pomme"]
e = "pomme"

print(compte(liste, e) == liste.count(e))