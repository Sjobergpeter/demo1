user_input = input("Skriv en text här: ")
input_spacefree = ""
clean_string = ""
mellanslag = " "

for bokstav in user_input:
    if bokstav.lower() not in mellanslag:
        clean_string += bokstav
        input_spacefree += bokstav

print (clean_string)

if clean_string == input_spacefree[::-1]:
    print ("Palindrom")
else:
    print("icke palindrom")