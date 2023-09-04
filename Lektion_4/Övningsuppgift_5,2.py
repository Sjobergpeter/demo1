while True:
    try:
        a = float(input("Skriv in float A> "))
        0 / a
        break
    except ValueError:
        print("FEL: ogiltigt nummer, försök igen")
    except ZeroDivisionError:
        print ("FEL: Går inte att dividera med 0, försök igen")

while True:
    try:
        b = float(input("Skriv in float B> "))
        a / b
        break
    except ValueError:
        print("FEL: ogiltigt nummer, försök igen")
    except ZeroDivisionError:
        print ("FEL: Går inte att dividera med 0, försök igen")

result = a / b
print ("""*****************************
*     The Great Divider     *"
-----------------------------""")
print ("")
print (hej)
print("beräknar c för uttrycket a / b = c")
print("")
print("-----------------------------")
print ("A =", a)
print ("B =", b)
print ("-----------------------------")
print(a, "/", b, "=", result)

