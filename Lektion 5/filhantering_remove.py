#Tar bort filen textfil.txt
import os
if os.path.exists("textfil.txt"):
    os.remove("textfil.txt")
else:
    print("The file does not exist")