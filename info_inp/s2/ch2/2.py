def taille_mantisse(a):
  compteur = 0
  while a+1 != a:
    a *= 2
    compteur += 1
  return compteur 


def taille_exposant(a):
  compteur = 0
  while 2*a != a:
    a *= 2
    compteur += 1
  return compteur 


a = 1.0 
print(taille_mantisse(a))
print(taille_exposant(a))