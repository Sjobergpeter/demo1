anteckningar = {
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Kom ihåg!": "Ta bilen till verkstad",
    "Inför tentamen": "Gör alla instuderingsuppgifter"
}

remove = input("Ta bort artikel: ")
del anteckningar[remove]

for a in anteckningar:
    print ("-----")
    print (a)
    print (anteckningar[a])