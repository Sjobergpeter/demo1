
# 2 olika def för att returnera det minsta talet i en lista

def minimum(lista):
    minsta_talet = lista[0]
    for i in lista:
        if (minsta_talet > i):
            minsta_talet = i
    return (minsta_talet)

my_list = [5, 2, 7, 4, 9]
print (minimum(my_list))




def mini(listas):
    sorted_list = sorted(listas)
    return sorted_list[0]

numbers = [5, 2, 7, 9, 4]
print (mini(numbers))

def greet(firstname, lastname):
    print ("Hello", firstname, lastname)

greet("Lisa", "Svensson")
