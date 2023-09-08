todos = ['Städa', 'Handla', 'Plugga', 'Ge blod']
new_todo = input("Ange todo: ")

if new_todo in todos:
    print (f"'{new_todo}' finns i listan")

else:
    print (f"'{new_todo}' finns inte i listan")
    indata = input("Vill du lägga till denna (J/N)? ")
    if indata.lower() == "j":
        print (f"Todo tillagd!")
        todos.append (new_todo)
        print (todos)
    elif indata.lower() == "n":
        print ("OK, todos är orörd")
        print (todos)
    else:
        print(" inmatning inkorrekt, programmet avslutas")