def triangle1(c, taille):
    for i in range(taille):
        print(c*(taille-i))
    print()

def triangle2(c, taille):
    for i in range(taille):
        print(" "*(taille-i)+c*i)
    print()

def triangle3(c, taille):
    for i in range(1, taille):
        print(c*i)
    print(c*taille)
    for i in range(1, taille):
        print(c*(taille-i))
    print()

def triangle4(c, taille):
    for i in range(taille):
        print(" "*(taille-i)+c*(2*i+1))
    print()

triangle1("#",4)
triangle2("*",6)
triangle3("*",4)
triangle4("+",5)