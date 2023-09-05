konsonanter = "bcdfghjklmnpqrstvwxyz"
resultat = ""

text = input("Ange texten du vill översätta till rövarspråket")

for bokstav in text:																																	
    if bokstav.lower() in konsonanter:
        resultat += bokstav + "o" + bokstav
    else:
        resultat += bokstav

print("Översättning till rövarspråket: ", resultat )