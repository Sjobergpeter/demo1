import os
import math

while True:
    # Skapar och/eller öppnar en variabel av textfilen för att läsas
    sign = open('sign.txt', 'r')
    # nedan så skapar vi en string som består av texten i textfilen
    read = sign.read()
    
    with open("sign.txt", "r")as forcenterx:
        #F orcenterx är hälften av alla mellanslag som får plats i skylten (18) minus hälften av antal bokstäver i meddelandet. omringar man meddelandet med varsin av denna variabel så centrerar det positionen utan att förstöra gränssnittet
        forcenterx = (18 - (len(forcenterx.read()))/2)
        # För säkerhetsskull så gör jag 2 variablar av forcenterx som nedan. skulle då forcenterx vara ett udda tal så blir forcenterspace1 ett mellanslag mindre än forcenterspace2. är talet uddan så hamnar meddelandet NÄSTAN i mitten men gränssnittets omgivning bibehålls
        forcenterspace1 = (" " * (math.floor(forcenterx)))
        forcenterspace2 = (" " * (math.ceil(forcenterx)))

    os.system ("cls" if os.name == "nt" else "clear")
# Här börjar gränssnittet, allt tidigare i terminalen "clearas" i samtlige OS
    print ("|------------------------------------------------------------|")
    print ("|  #  --------------------------------------            #    |")
    print (f"| ### |{forcenterspace1}{read}{forcenterspace2}|       #   ###   |")
    print ("| ### --------------------------------------      ###  ###   |")
    print ("|  |         |                     |               |    |    |")
    print ("|------------------------------------------------------------|")
    print ("| C | Change sign message")
    print ("| E | Exit program")
    print ("|-------------------------")
# Här skriver användaren in sin input för att välja att ändra meddelande eller att avbryta programmet
    indata = input("| > ")

    if indata.lower() == "c":
        new_message = input("Ändra skyltmeddelande (max 36 tecken):  ")

        if len(new_message) >36:
            # Meddelanderutan är 36 mellanslag lång. Skulle användaren skriva mer än 36 tecken så hade resterande symboler i gränssnittet följt med så därför tvingas användaren hålla sig inom ramen
            new_message = input("Error: skyltmeddelandet bestod av fler än 36 tecken. skriv ett nytt skyltmeddelande: ")
        
        # När det nya meddelandet har registrerats som under 36 tecken så fortsätter programmet att återigen öppna den separata filen för att skriva över den.
        with open("sign.txt", "w") as sign_file:
            sign_file.write(new_message)
            read = new_message.strip()

    elif indata.lower() == "e":
        break