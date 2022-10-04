def mention(note):
    if note >= 18:
        return "Très Bien avec félicitation du jury"
    elif note >= 16:
        return "Très Bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return 'Assez bien'
    else:
        return ""

note = int(input("Quelle est votre moyenne ? : "))
print(f"Vous avez la mention {mention(note)}")