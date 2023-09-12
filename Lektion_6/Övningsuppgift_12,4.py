anteckningar = {
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Kom ihåg!": "Ta bilen till verkstad",
    "Inför tentamen": "Gör alla instuderingsuppgifter"
}

print ("Lägg till artikel:")
titel = input(" titel > ")
text = input(" text > ")
anteckningar[titel] = text

for a in anteckningar:
    print ("-----")
    print (a)
    print (anteckningar[a])