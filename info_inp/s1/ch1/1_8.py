secondes = int(input("Nombre de secondes : "))
heures = secondes//3600
secondes-= heures*3600
minutes = secondes//60
secondes-=minutes*60
print(f"{heures}h {minutes}min {secondes}s")