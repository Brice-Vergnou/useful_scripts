import numpy as np

def pivot(systeme, valeurs):
  """
  systeme et valeurs sont des matrices qui représente l'équation sous la forme suivante :

  si on a 3x + 2y = 5
          -2x + 8y = 6
  systeme = [[3, 2],
             [-2, 8]]
  valeurs = [5,6] 

  systeme est une matrice carré d'ordre n 
  valeur est une liste de longueur n
  """
  systeme = np.array(systeme).astype(float)
  n = len(valeurs)

  for i in range(1, n): # etape 1 : échalonnage
    for j in range(i): # on fait en sorte que tous les coef avant la diagonale de gauche soient à 0
      alpha = systeme[i][j] / systeme[j][j] # on retire alpha fois la ligne j si on change le j^eme coefficient de la ligne i, car la ligne j est la seule avec un coefficient d'indice j différent de 0 
      systeme[i] = systeme[i] - alpha * systeme[j]
      valeurs[i] -= alpha * valeurs[j]
  for i in range(n): # diagonale de 1
    # on divise la ligne par son premier coef
    valeurs[i] /= systeme[i][i]
    systeme[i] /= systeme[i][i]
  for i in range(n-2,-1,-1): # résolution
    # on part de la derniere ligne, car la premiere à etre composé de 1 et 0
    for j in range(i+1, n):
      # on remonte pour utiliser les lignes en dessous pour "soustraire" les coef à droite de la diagonale pour n'avoir plus que des 1 et 0
      alpha = systeme[i][j]
      systeme[i] = systeme[i] - alpha * systeme[j]
      valeurs[i] = valeurs[i] - alpha * valeurs[j]
  return systeme, valeurs
    
  

def dichotomie(f,a, b):
  """
  f est la fonction définie dans main ( si si)
  a et b sont des bornes telle que f(k)=0 avec a<k<b (k unique)

  On renvoie une valeur proche de k

  le but va être de couper l'intervalle en deux (en m) et de changer l'une des deux borns :
    - celle de gauche si f(m) < 0
    - celle de droite si f(m) > 0

  On répète un certain nombre de fois jusqu'à que b-a < e , e étant une valeur qu'on aura   définie en avance ( non passée en paramètre )
  """
  xg = a
  xd = b
  e = 1e-30
  while xd - xg > e:
    m = (xg + xd)/2
    result = f(m)
    if result > 0:
      xd = m
    elif result < 0 :
      xg = m
    else:
      return m
  return (xg + xd)/2

def f_p(f, a):
  """
  dérivée ( approximative ) de f en a
  """
  d_a = a + 1e-10 # valeur proche de a 
  return (f(d_a) - f(a)) / (d_a - a) # pas la formule standarde de la dérivée, 
                                      # mais un calcul de pente comme au collège

def methode_newtown(f,a):
  """
  on regarde la tangente en a et où elle coupe l'axe des abcisses ( en b ), et même chose   pour b

  On a y = f'(a)(x-a) + f(a)
  Comme on cherche b qui se situe sur l'axe des abcisses, on a :
  0 = f'(a)(b-a) + f(a)
  Ou encore
  b = -f(a)/f'(a) + a

  On transforme en suite:
  x_n+1 =  x_n - f(x_n)/f'(x_n)

  On répète ça k fois, k étant assez grand pour simuler une limite et laisser la suite converger ( dans le meilleur des cas)
  On renverra le resulter et f(resultat) pour constater si le résultat est satisfaisant ou non
  """
  for _ in range(1000):
    a = a - f(a)/f_p(f, a)
  return a, f(a)
  
