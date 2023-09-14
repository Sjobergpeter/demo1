import json
import os

#en variabel för att ta emot och ersätta json filen till python text
notes = ""
#Skapar en anteckningar för grund fil till Json om det inte finns en i grundmappen
anteckningar = {
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Kom ihåg!": "Ta bilen till verkstad",
    "Inför tentamen": "Gör alla instuderingsuppgifter"
}

while True:
    #Rensar terminalen
    os.system("cls" if os.name == "nt" else "clear")
    #hämtar json filen för att lägga in i variabeln notes
    try:
        with open ("anteckningar.json", "r") as myfile:
            anteckningar = myfile.read()
            notes = json.loads(anteckningar)
    
    #Här skapar jag json filen om den inte finns
    except FileNotFoundError:
        print ("finns inte, skapar filen")
        with open ("anteckningar.json", "x+") as myfile:
            print ("nu borde filen finnas")
            myfile.write(json.dumps(anteckningar))

    print (".:  ALWAYSNOTE  :.")
    print ("-- gold edition --")
    print ("******************")
    for f in notes:
        print ("-", f)
    print ("------------------")
    print("view  | view note")
    print("add   | add note")
    print("rm    | remove note")
    print("exit  | exit program")
    print ("------------------")
    user_input = input("menu > ")

    if user_input == "view":
        user_input = input("Vilken anteckning vill du läsa? > ")
        if not user_input in notes:
            print(f"'{(user_input)}' finns inte i anteckningar!")
            input("Tryck 'ENTER' för att fortsätta")
            continue
        
        notes[(user_input)]
        print (notes[(user_input)])
        input("Tryck enter för att fortsätta")
        continue
    
    

    elif user_input.lower() == "add".lower():
        print ("Lägg till artikel:")
        titel = input(" titel > ")
        if titel in notes:
            print(f"'{(titel)}' Finns redan i anteckningar")
            input("Tryck 'ENTER' för att fortsätta")
            continue
        text = input(" text > ")
        notes[titel] = text 

        with open ("anteckningar.json", "w") as myfile:
            myfile.write(json.dumps(notes))
            input("Anteckning tillagd.")
            input("Tryck 'ENTER' för att fortsätta")

    elif user_input.lower() == "rm".lower():
        user_input = input("Vilken anteckning vill du ta bort? > ")
        if user_input in notes:
            del notes[(user_input)]

            with open ("anteckningar.json", "w") as myfile:
                myfile.write(json.dumps(notes))
            
            print (f"'{(user_input)}' är borttagen från anteckningarna")
            input("Tryck 'ENTER' för att fortsätta")
            continue
        
        else:
            print(f"'{(user_input)}' finns inte bland anteckningarna")
            input("Tryck 'ENTER' för att fortsätta")
            continue
    

    elif user_input.lower() == "exit".lower():
        break

    
    else:
        input("Felakting inmatning, tryck 'ENTER' för att fortsätta")