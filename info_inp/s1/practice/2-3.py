def demi(chaine):
    return chaine[:len(chaine)//2]

def censure(chaine):
    return chaine[0] + "#"*(len(chaine)-2) + chaine[-1]

def bidon(chaine):
    return chaine[0], chaine[-1], len(chaine)

chaine = "bonjour_à_tous"

print(demi(chaine))
print(censure(chaine))
print(bidon(chaine))