user_input = input("Ange multiplikationstabell: ")
multiplication = int(user_input)
times = 1
tries = 0

while True:
    result = multiplication * times
    print(result)
    times += 1
    tries += 1
    
    if tries == 3:
       choice = input("Vill du fortsätta? y/n")
       tries = 0
       
       if choice == "y":
           continue
       else:
           break
