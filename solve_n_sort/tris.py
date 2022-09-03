def tri_insertion(liste):
  """
  Insère le première élément trié dans la zone non triée
  """
  for i in range(1, len(liste)):
    key_index = i
    while key_index>=1 and liste[key_index] < liste[key_index-1]:
      liste[key_index] , liste[key_index-1] = liste[key_index-1] , liste[key_index]
      key_index -=1

def tri_selection(liste):
  """
  Place la plus petite valeur de la zone non triée à la fin de la zone triée
  """
  for i in range(len(liste)):
    lowest_value = liste[i]
    lowest_index = i
    for j in range(i, len(liste)):
      if lowest_value > liste[j]:
        lowest_value = liste[j]
        lowest_index = j
    liste[i], liste[lowest_index] = liste[lowest_index], liste[i]

def tri_bulle(liste):
  """
  plus ou moins le tri par selection dans l'autre sens
  """
  n = len(liste)
  has_permuted = True

  while has_permuted:
    has_permuted = False
    for i in range(n-1):
      if liste[i] > liste[i+1]:
        liste[i] , liste[i+1] = liste[i+1] , liste[i]
        has_permuted = True
    n-=1
