import math
Vanligkorv2 = int(input("Hur många elever vill ha 2 vanliga korvar? :"))
Vanligkorv3 = int(input("Hur många elever vill ha 3 vanliga korvar? :"))
Vegankorv2 = int(input("Hur många elever vill ha 2 veganska korvar? :"))
Vegankorv3 = int(input("Hur många elever vill ha 3 veganska korvar? :"))
Dryck = int(input("Hur många elever vill ha dryck?: "))

Antalvanligkorv = math.ceil(((Vanligkorv2 * 2) + (Vanligkorv3 * 3)) / 8)
Antalvegankorv = math.ceil((Vegankorv2 * 2 ) + (Vegankorv3 *3) / 4)
print (Antalvanligkorv)