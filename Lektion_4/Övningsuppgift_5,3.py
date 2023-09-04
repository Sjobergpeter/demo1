print (".:MATHLETE V2.0:.")
print ("-----------------")
sum = 0
antal = 0
while True:
    try:
        user_input = int(input(">"))

        break
    except ValueError:
        print("NEJ")
        continue