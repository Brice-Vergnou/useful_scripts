l = int(input("Combien de lignes ? : "))
c = int(input("Combien de colonnes ? : "))
ligne=c*"*"+"\n"
ligne_a_trou="*"+" "*(c-2)+"*\n"
print(ligne+ligne_a_trou*(l-2)+ligne)