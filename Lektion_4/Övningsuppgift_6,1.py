user_text = input("Skriv din text här: ")
Chosen_letter = input("Ange en bokstav: ")

counter = 0
i = 0

while i < len(user_text):
    if user_text[i].lower() == Chosen_letter:
        counter += 1
    i += 1
print("Bokstaven", Chosen_letter, "förekommer", counter, "gånger i texten")