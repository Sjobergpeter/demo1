#Skapa dictionary

person = {
    "name": "Peter Sjöberg",
    "age": 29
}

#Hämta element 
print("Hej " + person["name"])
print("Du är " + str(person["age"]) + " år gammal")
#formaterad sträng för att slippa konvertera int till string
print(f"Du är  { person['age'] }  år gammal")

"""
# Referera till en nyckel dynamiskt
attr = input("Ange attribut (nyckel) > ")

try:
    print (person[attr])
except KeyError:
    print("Fel! Attributet existerar inte")
"""

# Ändra värdet på en nyckel i din dictionary
person["age"] = 30

print (person)

# Lägg till ny data (key-value-pair) / element
person["address"] = "Signe Tillischgatan 13"
print (person)

#Kopiera dict
# temp = person  FEL
person_copy = person.copy()
person_copy ["temp2"] = "temp2"
print(person_copy)

# Ta bort element
del person_copy

#Iteration av dict
for key in person:
    print("key", key)
    print("Value", person[key])

    #Nästlande dict
    person["address"] = {
        "gatuadress": "Signe Tillischgatan 13",
        "ort": "Solna",
        "postnummer": "17635"
    }

    # Skriv ut addressen enligt svensk standard

print(person["address"]["gatuadress"])
print(person["address"]["postnummer"], person["address"]["ort"])
