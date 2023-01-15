from random import randint

def value_digit(digit):
    return "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(str(digit).upper())

def letter_from_int(r):
    return "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[r]

def base2int(mot_bin,b):
    s = 0
    for i, digit in enumerate(mot_bin[::-1]):
        s+= value_digit(digit) * b**i
    return s

def int2base(entier,b):
    mot_bin = ""
    continuer = True
    while entier != 0:
        entier,r = entier//b, entier%b
        mot_bin = letter_from_int(r) + mot_bin
    return mot_bin
        


print(int2base(255,16) == "FF")
print(base2int("FF",16)==255)

for _ in range(50):

    n = randint(0,1e5)
    
    print(int2base(n,16) == hex(n)[2:].upper())
    print(base2int(str(n),16) == int(str(n),16))