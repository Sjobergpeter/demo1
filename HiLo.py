import random

print ("""
-----------------------------------
Welcome to The Higher Lower Game.
I will randomize a number between
0 and 99.
Can you guess it?
-----------------------------------
""")
Answer = random.randint (0, 99)
guess = input("Your guess >")
tries = 0

while True:
    tries += 1
    guess = int(guess)
    if guess == Answer:
        break

    elif guess < Answer:
        print ("HIGHER!")
        guess = input("Try again >")
        continue

    elif guess > Answer:
        print ("LOWER!")
        guess = input("Try again >")
        continue

print ((guess), "is correct!")
print ("It took you",(tries),"guesses.")
print ("Good job!")