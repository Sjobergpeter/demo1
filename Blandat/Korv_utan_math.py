Vanligkorv2 = int(input("Hur många elever vill ha 2 vanliga korvar? :"))
Vanligkorv3 = int(input("Hur många elever vill ha 3 vanliga korvar? :"))
Vegankorv2 = int(input("Hur många elever vill ha 2 veganska korvar? :"))
Vegankorv3 = int(input("Hur många elever vill ha 3 veganska korvar? :"))
Dryck = int(input("Hur många elever vill ha dryck?: "))

Antalvanligkorv = (((Vanligkorv2 * 2) + (Vanligkorv3 * 3)) / 8)
Antalvegankorv = (((Vegankorv2 * 2 ) + (Vegankorv3 * 3)) / 4)

if Antalvanligkorv % 1 > 0:
    Antalvanligkorv = int(Antalvanligkorv) + 1
else:
    Antalvanligkorv = int(Antalvanligkorv)

if Antalvegankorv % 1 > 0:
    Antalvegankorv = int(Antalvegankorv) + 1
else:
    Antalvegankorv = int(Antalvegankorv)

pris = float((20.95 * (Antalvanligkorv)) + (34.95 *(Antalvegankorv)) + (13.95 * (Dryck)))

print ("Korvkollen 1.0.1:")
print ("-----------------------------------")
print ("Antal vanliga korvar : ", ((Vanligkorv2 * 2) + (Vanligkorv3 * 3)))
print ("Antal veganska korvar : ", ((Vegankorv2 * 2 ) + (Vegankorv3 *3)))
print ("Antal drickor: ", Dryck)
print ("-----------------------------------")
print ("-      INKÖPSLISTA       -")
print ("-----------------------------------")
print ("Vanlig korv:", (Antalvanligkorv), "Förpackningar")
print ("Vegansk korv:", (Antalvegankorv), "Förpackningar")
print ("Dryck:", (Dryck), "drickor")
print ("-----------------------------------")
print (round(pris, 1), "SEK")
print ("-----------------------------------")