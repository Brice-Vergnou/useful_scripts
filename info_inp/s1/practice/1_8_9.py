secondes = 18769
heures = secondes // 3600
minutes = secondes % 3600 //60
secondes = secondes % 3600 % 60
print(f"{heures}h {minutes}min {secondes}s")
