attendants = ['Lisa', 'Kalle', 'Olivia', 'Johan']
with open('textfil.txt', 'w') as file:
    for attendant in attendants:
        file.write('Hello ' + attendant + '!\n')