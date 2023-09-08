import json
    # Ange den JSON-formaterade strängen
my_chars = '["abc" , "\u00e5\u00e4\u00f6 " , "123"]'

# Omvandla JSON-strängen till en Python-lista
char_list = json.loads(my_chars)

# Skriv ut varje objekt på en ny rad genom att iterera listan
for item in char_list:
    print(item)  # Använd strip() för att ta bort onödig mellanslag