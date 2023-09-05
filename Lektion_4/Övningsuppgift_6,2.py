konsonanter = "bcdfghjklmnpqrstvwxyz"
resultat = ""

text = input("Ange texten du vill översätta till rövarspråket: ")

for b in text:																																	
    if b.lower() in konsonanter:
        resultat += b + "o" + b
    else:
        resultat += b

print("Översättning till rövarspråket: ", resultat )
