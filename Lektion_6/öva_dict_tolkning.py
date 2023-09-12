person = {
    "firstname": "Johan",
    "lastname": "Svensson",
    "age": 25,
    "pets": [
        {"name": "Morris","age": 3,"typ": "hund"},
        {"name": "Lisa","age": 2,"typ": "katt"}
]
}

namn = person["firstname"] + " " + person["lastname"]
age = person["age"]
pets = person["pets"]
count_pets = len(pets)

print (namn, "är", age, "år gammal och har", count_pets, "husdjur")
for pet in pets:
    print (f"En {(pet['age'])} år gammal {(pet['typ'])} som heter {(pet['name'])}")
