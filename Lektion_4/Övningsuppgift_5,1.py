user_input = input("Tal>")

try:
    user_input = int(user_input)
    Times = user_input * 2
    print("tal", user_input)
    print(" Resultat", Times)
    print (Times)
    
except ValueError:
    print (user_input, "kan inte översättas till ett heltal")