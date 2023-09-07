#öppna en fil med with. f är en variabel som kan döpas till vadsom
with open('textfil.txt') as f:
    text = f.read()
print(text)