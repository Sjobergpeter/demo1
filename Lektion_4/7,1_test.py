
# Variabler för att lagra de tre posterna
POST_1 = ''
POST_2 = ''
POST_3 = ''

while True:
    # [ ] 1. Rensa terminalfönstret
    import os
    os.system('clear')  # Om du använder Linux/Mac, använd 'clear', om du använder Windows, använd 'cls'

    # [X] 2. Skriv ut instruktioner och anslagstavla
    print('.: basicBILLBOARD :.')
    print('********************')
    print('P1:', POST_1)
    print('P2:', POST_2)
    print('P3:', POST_3)
    print('--------------------')
    print('c | Ändra post')
    print('e | Stäng program')
    print('--------------------')

    # [ ] 3. Hämta kommando från användaren
    kommando = input('meny > ')

    # [ ] 4. Utför operationer för inmatat kommando
    if kommando == 'c':
        post_nummer = input('Vilken post vill du ändra (P1, P2, eller P3)? ')
        ny_text = input('Skriv den nya texten för posten: ')
        if post_nummer == 'P1':
            POST_1 = ny_text
        elif post_nummer == 'P2':
            POST_2 = ny_text
        elif post_nummer == 'P3':
            POST_3 = ny_text
        else:
            print('Ogiltigt postnummer. Inget ändrades.')

    elif kommando == 'e':
        print('Programmet stängs.')
        break  # Avslutar programmet om användaren väljer att stänga det

    # [X] 5. Pausa exekvering
    input('Tryck enter för att fortsätta ...')

# [X] 6. Gå till 1 (programmet kommer att loopa igen från början)