from tris import *
from random import shuffle
from solve import *
import numpy as np

systeme = [[3, 95, 8],
           [-2, 8, 7],
           [1, 2, 0]]
valeurs = [5,6, 0] 

def f(x):
  """
  f doit être continue est s'annuler sur au moins un point
  """
  return x**2 + 3*x - 4



if __name__=="__main__":
  systeme, valeurs = pivot(systeme, valeurs)
  print(systeme)
  print(valeurs)

  # x = dichotomie(f, 0, 50)
  # print(f"Par dichotomie : {x}")
  # print(f"f({x}) =  {f(x)}")
  # x, result = methode_newtown(f, 50)
  # print(f"Par newtown : {x}")
  # print(f"f({x}) =  {f(x)}")


  # liste = list(range(10))
  # shuffle(liste)
  # print(liste)
  # tri_insertion(liste)
  # tri_selection(liste)
  # tri_bulle(liste)
  # print(liste)
