import random

#klass som beskriver rektangel
class Rectangle():
    length = 0
    width = 0

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

        #Getters and Setters
    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_width(self):
        return self.__width
    
    def set_width(self, width):
        self.__width = width

#metoder
    def area(self):
        return self.__length * self.__width
    
    def circumference(self):
        return (self.__length + self.__width) * 2

#Skapa objekt av klassen Rectangle
r1 = Rectangle(1, 2)
# print (r1.width)
# print (r1.length)

# Ändra attribut
r1.width = 5
r1.length = 10


print ("Bredd: ", r1.width)
print ("Längd: ", r1.length)
print ("Omkrets: ", r1.circumference())
print ("Area: ", r1.area())

r2 = Rectangle(2, 3)
r2.width = 10
r2.length = 10

print ("Bredd: ", r2.width)
print ("Längd: ", r2.length)
print ("Omkrets: ", r2.circumference())
print ("Area: ", r2.area())

# Lista av objekt
r_lista = [
    Rectangle(1, 2),
    Rectangle (3, 4),
    Rectangle (5, 6)
]

def get_sum(r_lista):
    summa = 0
    for r in r_lista():
        summa += r.area()
    return summa

# print ("Summa av alla areor:", get_sum(r_lista))


slump_lista = []

for i in range(1000):
   slump_lista.append(Rectangle(random.randint(1,100), random.randint(1,100)))

print ((get_sum(slump_lista)))