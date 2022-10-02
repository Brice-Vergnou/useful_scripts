def moyenne(notes):
    return sum(notes)/len(notes)

def ecart(notes):
    return max(notes) - min(notes)

def moyenne_gauche(notes):
    if len(notes) < 0:
        return 0
    return moyenne(notes[:3])

def moyenne_droite(notes, k):
    if len(notes) < k:
        return 0
    return moyenne(notes[-k:])

bulletin = (15,12,8,11,13)
print(moyenne(bulletin))
print(ecart(bulletin))
print(moyenne_gauche(bulletin))
print(moyenne_droite(bulletin,5))