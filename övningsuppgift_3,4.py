country = str(input("Skriv in ett land: "))

if country.lower() == "england" or country.lower() == "nordirland" or country.lower() == "skottland" or country.lower() == "wales":
    print ("Landet tillhör Storbritannien")
elif country.lower() == "sverige" or country.lower() == "danmark" or country.lower() == "norge" or country.lower() == "finland" or country.lower() == "island":
    print ("Landet tillhör Norden")
else:

    print("Jag är inte bekant med det landet")