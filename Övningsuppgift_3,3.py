import random

dice = random.randint(1, 6)
if dice == 1:
    print ("Du slog en 1a!")
    dice(1)
elif dice == 2:
    print ("Du slog en 2a!")
    print ("---------")
    print ("| X     |")
    print ("|       |")
    print ("|     X |")
    print ("---------")
elif dice == 3:
    print ("Du slog en 3a!")
    print ("---------")
    print ("| X     |")
    print ("|   X   |")
    print ("|     X |")
    print ("---------")
elif dice == 4:
    print ("Du slog en 4a!")
    print ("---------")
    print ("| X   X |")
    print ("|       |")
    print ("| X   X |")
    print ("---------")
elif dice == 5:
    print ("Du slog en 5a!")
    print ("---------")
    print ("| X   X |")
    print ("|   X   |")
    print ("| X   X |")
    print ("---------")
elif dice == 6:
    print ("Du slog en 6a!")
    print ("---------")
    print ("| X   X |")
    print ("| X   X |")
    print ("| X   X |")
    print ("---------")