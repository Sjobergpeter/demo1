cars = ["Mercedes", "Volvo", "Toyota"]
indata = ""
# Layout
ui_width = 30
while True:
    import os
    os.system ("cls" if os.name == "nt" else "clear")
    print("*" * ui_width)
    print(".: STACKMASTER 1.0 :.".center(ui_width))
    print("-" * ui_width)
    for n in cars:
        print ("-"+ n)
    print("-"*(ui_width))
    print ("|  MENU  |".center(ui_width))
    print ("push | Push element to stack")
    print ("pull | Pull element to stack")
    print ("exit | Exit program")
    print ("-"*ui_width)
    indata = input("MENU >")
    
    if indata == "push":
        indata = input("Vilket bilmärke vill du lägga till? ")
        cars.append(indata.capitalize())

    elif indata == "pull":
        if len(cars) == 0:
            fel = input("Finns inga bilar att ta bort. Tryck ENTER för att börja om")
        else:
            indata = input(f"Vill du ta bort {cars[-1]}? y/n: ")
        if indata.lower() == "y" :
            cars.pop()
        elif indata == "n":
            continue
    
    elif indata.lower() == "exit":
        break