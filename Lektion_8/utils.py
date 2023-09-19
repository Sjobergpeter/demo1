MAX_NUM = 1000

def minimum(lista):
    minsta_talet = lista[0]
    for i in lista:
        if (minsta_talet > i):
            minsta_talet = i
    return (minsta_talet)

def addera(tal1, tal2):
    summa = tal1 + tal2
    return summa

def greet(firstname, lastname):
    return(print ("Hello", firstname, lastname))