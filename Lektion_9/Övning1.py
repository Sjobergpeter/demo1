# Djur
#   Sort
#   Namn
#   Antal ben
#   Kan flyga

class Djur():
    #Konstruktor
    #Används vid instansiering
    def __init__(self):
        self.sort = "ingen sort"
        self.namn = "Inget namn"
        self.ben = 0
        self.kan_flyga = False

    #Metoder
    def print_djur(self):
        print ("Information om objektet (Djur)")
        print ("\tSort:", self.sort)
        print ("\tNamn:", self.namn)
        print ("\tAntal ben:", self.ben)
        if self.kan_flyga == True:
            print("\tKan flyga")
        else:
            print("\tKan inte flyga")
    
class Zoo():
    def __init__(self):
        self.djur_lista = []
        self.namn = "inget namn"

        #Lägger till ett djur
    def lägg_till_djur(self, nytt_djur):
        self.djur_lista.append(nytt_djur)
    
    def antal_djur(self):
        return len(self.djur_lista)
    
    def print_zoo(self):
        print("Zoonamn:", self.namn)
        for djur in self.djur_lista:
            djur.print_djur()


# Instansiera ett objekt
apa = Djur()
apa.sort ="Apa"
apa.namn ="Nicke Nyfiken"
apa.ben = 2
# print(apa.sort)
# print(apa.namn)
# print(apa.kan_flyga)

# print ("---------------")
# print ("Hundobjekt")
hund = Djur()
hund.sort = "Hund"
hund.namn = "Pluto"
hund.ben = 4

# print(hund.sort)
# print(hund.namn)
# print(hund.ben)

# apa.print_djur()

skata = Djur()
skata.sort = "Skata"
skata.namn = "Krax"
skata.ben = 2
skata.kan_flyga = True  # Skator kan flyga

# Skriv ut information om skatan
# skata.print_djur()

nytt_zoo = Zoo()
nytt_zoo.namn = "Nya Zooet"
print(nytt_zoo.namn)
nytt_zoo.lägg_till_djur(skata)
nytt_zoo.djur_lista[0].print_djur()
nytt_zoo.lägg_till_djur(hund)

print (nytt_zoo.antal_djur())

nytt_zoo.print_zoo()