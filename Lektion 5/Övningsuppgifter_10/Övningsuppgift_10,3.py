import os
while True:
    #Öppnar och läser databasen. "encoding="utf-8" får bokstäverna å, ä och ö att läsas korrekt (bergström == BergstrÃ¶m utan encoding)
    database = open ("database.csv", "r", encoding="utf-8")
    os.system("cls" if os.name == "nt" else "clear")
    print (".: PEOPLES DATABASE :.")
    print ("----------------------")
    print ("get_id | Get person by ID")
    print ("scan_f | List people by FORENAME")
    print ("scan_s | List people by SURNAME")
    print ("exit   | Exit program")
    print ("----------------------")
    user_input = input("| >")
    print ("----------------------")

    if user_input == "get_id":
        id = input("ID: ")
        print ("----------------------")
        for line in database:
            #splittar
            fields = line.strip().split(',')
            if id == fields[0]:
                print(fields[0])
                print(fields[1])
                print(fields[2])
                print(fields[3])
                print(fields[4])

    if user_input == ("scan_f"):
        forename = input("| FORENAME: ")
        print ("----------------------")
        for line in database:
            #.strip() tar bort mellanrum, och i detta fall så printades en till tom rad ut efter denna if sats utan strip. split (,) gör allting mellan kommatecknen till separata element
            fields = line.strip().split(',')
            if forename.lower() == fields[1].lower():
                print(fields[0], ",", fields[1], ",", fields[2], ",", fields[3], ",", fields[4])

    if user_input == ("scan_s"):
        surname = input("| SURNAME: ")
        print ("----------------------")
        for line in database:
            fields = line.strip().split(',')
            if surname.lower() == fields[2].lower():
                print(fields[0], ",", fields[1], ",", fields[2], ",", fields[3], ",", fields[4])

    elif user_input == "exit":
        break
    print ("----------------------")
    input("Tryck enter för att fortsätta")