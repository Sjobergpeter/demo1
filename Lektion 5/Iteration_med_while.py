deltagare = ["Peter", "jakob", "Torbjörn", "Henrik"] 
i = 0 
while i < len(deltagare):
    print ("Välkommen " + deltagare[i])
    deltagare.remove(deltagare[i])
    i += 1

    for namn in deltagare:
        print (f"Välkommen {namn}")
        del deltagare