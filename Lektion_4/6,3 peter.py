user_input = input("Skriv en text här: ")
clean_string = ""
mellanslag = " "

for bokstav in user_input:
    if bokstav.lower() in mellanslag:
        clean_string += bokstav

print (clean_string)
