def demi(ch):
    return ch[:len(ch)//2]

def censure(ch):
    return ch[0] + (len(ch)-2)*"#" + ch[-1]

def bidon(ch):
    return ch[0], ch[-1], len(ch)

ch = "salut-à-tous :)"

print(demi(ch))
print(censure(ch))
print(bidon(ch))
