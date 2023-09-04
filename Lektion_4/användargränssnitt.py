ui_width = 30
print(ui_width * '*')
print('FÄRG-GISSAREN 2.0'.center(ui_width))
print(ui_width * '-')
print(':: REGLER ::'.center(ui_width))
print('Gissa en färg!'.center(ui_width))
print('Gissar du rätt färg'.center(ui_width))
print('vinner du spelet!'.center(ui_width))
print('-' * ui_width)
times = 1
color = input('Gissa färg > ').lower()
while color != 'gul':
    print('Fel gissning , försök igen... ')
    times += 1
    color = input('Gissa färg > ').lower()
print('-' * (ui_width))
print('Korrekt gissat efter', times, 'försök!')
print (input("Tryck på retur för att starta igen"))

import os
if os.name == "nt":
    os.system("cls")
    