print (".:MATHLETE V2.0:.")
print ("-----------------")
total = 0
count = 0

while True:
    try:
        user_input = (input(">"))
        if user_input.lower() == "exit":
            break
        number = int(user_input)
        total += number
        count += 1

    except ValueError:
        print("FEL: Ogiltigt nummer!")
        print("Skriv \"exit\" för att avsluta!")
        continue    

print ("-----------------")
print ("Kardinalitet:", count)
print ("Summa:       ", total)
print ("Medelvärde   ", (total / count))