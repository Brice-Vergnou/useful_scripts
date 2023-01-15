alphabet = 'abcdefghijklmnopkrstuvwxyz'
lettre_commune = "e"

def valeur(lettre):
    for i, char in enumerate(alphabet):
        if char == lettre:
            return i
        
def lettre(n):
    return alphabet[n]

def normalise(chaine):
    new_chaine = ''
    for char in chaine.lower():
        if char in alphabet:
            new_chaine += char
    return new_chaine


def code(chaine):
    return [valeur(lettre) for lettre in normalise(chaine)]

def decode(liste_codee):
    liste_decodee = [lettre(n) for n in liste_codee]
    return "".join(liste_decodee)

def codage_cesar(chaine, k):
    liste = code(chaine)
    liste = [(n + k)%26 for n in liste] # codage
    return decode(liste)
    
def decodage_cesar(chaine, k):
    liste = code(chaine)
    liste = [(n-k)%26 for n in liste] # decodage
    return decode(liste)

def cle_code(chaine):
    most_used = chaine[0]
    nb_most_used = chaine.count(most_used)
    for char in chaine:
        occur = chaine.count(char)
        if occur > nb_most_used:
            most_used = char
            nb_most_used = occur
    return valeur(most_used) - valeur(lettre_commune)


def casse_cesar(chaine):
    cle = cle_code(chaine)
    return decodage_cesar(chaine, cle)


chaine_moodle = "lujyfwavnyhwoplsljopmmyltluawhykljhshnlhbzzpjvuubjvttlsljopmmylkljlzhyvbsljvklkljlzhylzabultlaovklkljopmmyltluaaylzzptwslbapspzllwhyqbslzjlzhykhuzzlzjvyylzwvukhujlzzljylalzslalealjopmmylzviaplualuyltwshjhuajohxblslaaylkbalealjshpyvypnpuhswhybulslaaylhkpzahujlmpelavbqvbyzkbtltljvalkhuzsvykylklshswohilawvbyslzklyuplylzslaaylzkhuzsljhzkbukljhshnlhkyvpalvuylwylukhbklibawhyleltwslhcljbukljhshnlklayvpzclyzshkyvpalhlzayltwshjlwhykiklcpluallahpuzpqbzxbhdxbpklcpluagwbpzeklcpluahlajpszhnpakbulwlytbahapvujpyjbshpylklshswohilashsvunblbykbkljhshnlayvpzkhuzsleltwsllcvxbljvuzapablshjslkbjopmmyltluaxbpszbmmpaklayhuztlaaylhbklzapuhahpylzpszhpaklqhxbpszhnpakbujopmmyltluakljlzhywvbyxbljlsbpjpwbpzzlkljopmmylysltlzzhnlkhuzsljhzklshswohilashapusljopmmylkljlzhyuhxblcpunazpejslzwvzzpislzfjvtwypzshjslubsslxbpultvkpmplwhzslalealpszhnpakbujhzwhyapjbsplykljopmmyltluawhyzbizapabapvutvuvhswohilapxbljlzzbizapabapvuzylwvzluazbybuwypujpwlhuhsvnblthpzzvuavialublzwhyklzwlytbahapvuzxblsjvuxblzklzslaaylzklshswohilakhuzsljhznlulyhsshjsllzakvuullwhyshwlytbahapvulasluvtiylkljslzwvzzpislzlzahsvyzzhuzjvttbultlzbylhcljjlsbpklzjopmmyltluazkljlzhyjljopmmyltluakljlzhyhwblaylbapspzljvttllsltluakbultlaovklwsbzjvtwsleljvttlsljopmmylklcpnlulylzlbspsuvmmylhbjbulzljbypalkljvttbupjhapvuhjhbzlkbaylzmhpisluvtiylkljslzjlxbpwlytlaklzzhflyzfzalthapxbltluajlsslzjpxbhukshtlaovklkljopmmyltlualzajvuublthpzhbzzpwhyjlxbljvttlavbalujvkhnlwhyzbizapabapvutvuvhswohilapxblpswlbalaylaylzyhwpkltluajhzzlwhyhuhsfzlklmylxblujlzjlyahpulzslaaylzhwwhyhpzzluailhbjvbwwsbzzvbcluaxblslzhbaylzkhuzbulshunbluhabylssl"


print(casse_cesar(chaine_moodle))