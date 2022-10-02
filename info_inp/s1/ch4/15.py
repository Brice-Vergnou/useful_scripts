CONTINUE = True
valeurs = []

while CONTINUE:
    x= input("Donnez une valeur numérique ou dites fin : ")
    if x.lower() == "fin":
        CONTINUE = False
    else:
        valeurs.append(int(x))
    
double = False
for valeur in valeurs:
    compte = valeurs.count(valeur)
    if compte != 1 :
        print(f"La valeur {valeur} apparaît {compte} fois")
        double = True

if not double:
    print("Toutes les valeurs sont uniques")