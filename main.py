def Main(words):
    print("================= PASSWORD ANALYZER ==================")
    print()
    print("Mot de passe : ", words)
    print()
    print("Longueur :", str(Length(words)) + " caractères")
    print("Majuscule :", UpperCase(words))
    print("Minuscule :", LowerCase(words))
    print("Nombre  :", DigitCase(words))
    print("Caractère spéciaux :", Poctuaction(words))
    print()
    total = j + i + h + l + k
    print("Score :", total, "/5")
    print("Conseil :", Conseil(words))

def Conseil(words):
    if UpperCase(words) == "non":
        return "Il faut mettre des majuscules"
    elif LowerCase(words) == "non":
        return "Il faut mettre des minuscules"
    elif DigitCase(words) == "non":
        return "Il faut mettre des nombres"
    elif Poctuaction(words) == "non":
        return "Il faut mettre des caratères spéciaux"
    elif Length(words) < 8:
        return "Il faut mettre plus de 8 caratères"
    else:
        return "Votre mot de passe est bien robuste"

def Length(words):
    global j
    j = 0
    if len(words) > 8:
        j = 1
    return len(words)

def UpperCase(words):
    global i
    i = 0
    for letter in words:
        if letter.isupper():
            i = 1
    if i != 0:
        return "oui"
    else:
        return "non"

def LowerCase(words):
    global h
    h = 0
    for letter in words:
        if letter.islower():
            h = 1
    if h != 0:
        return "oui"
    else:
        return "non"

def DigitCase(words):
    global k
    k = 0
    for letter in words:
        if letter.isdigit():
            k = 1
    if k != 0:
        return "oui"
    else:
        return "non"
    
def Poctuaction(words):
    global l
    l = 0
    for letter in words:
        if not letter.isalnum() and not letter.isspace():
            l = 1
    if l != 0:
        return "oui"
    else:
        return "non"

print(Main("bonjo#u1"))