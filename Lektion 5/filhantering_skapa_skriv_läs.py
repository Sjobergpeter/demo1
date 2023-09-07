import os

"""
"r" är read
"x" - är create
"a" är append, öppnar
"w" är write
x+ / a+ / w+ är and read
f.seek(0) hamnar du på början av filen
.readline läser du bara den raden
"""""

#Kollar om filen finns textfil.txt
if os.path.exists("textfil.txt"):
    f = open("textfil.txt", "r")
#Finns filen inte så skapar den filen textfil.txt med append
else:
    f = open("textfil.txt", "x")
f = open("textfil.txt", "a")


#Skriver i filen textfil.txt
f.write("rad 1\n")
f.write("rad 2\n")
f.write("rad 3\n")

# Öppna och läs från en fil med read
f = open('textfil.txt', 'r')
text = f.read()
print(text)

