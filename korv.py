import math
Vanligkorv2 = int(input("Hur många elever vill ha 2 vanliga korvar? :"))
Vanligkorv3 = int(input("Hur många elever vill ha 3 vanliga korvar? :"))
Vegankorv2 = int(input("Hur många elever vill ha 2 veganska korvar? :"))
Vegankorv3 = int(input("Hur många elever vill ha 3 veganska korvar? :"))
Dryck = int(input("Hur många elever vill ha dryck?: "))

Antalvanligkorv = (((Vanligkorv2 * 2) + (Vanligkorv3 * 3)) / 8)
Antalvegankorv = ((Vegankorv2 * 2 ) + (Vegankorv3 *3) / 4)

if Antalvanligkorv % 1 > 0:
    Antalvanligkorv = int(Antalvanligkorv) + 1
else:
    Antalvanligkorv = int(Antalvanligkorv)
print (Antalvanligkorv)
