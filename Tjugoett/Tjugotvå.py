import random
import os
import time


def setDeck():
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ["hearts", "Diamonds", "Clubs", "Spades"]
    i = 0
    deck = []
    for rank in ranks:
        i += 1
        for suit in suits:
            card = {"rank": rank, "suit": suit, "value": i}
            deck.append(card)
    random.shuffle(deck)
    return deck


def winnerIs():
    os.system("cls" if os.name == "nt" else "clear")
    print((".And the winner is.").center(50))
    time.sleep(0.8)
    os.system("cls" if os.name == "nt" else "clear")
    print(("..And the winner is..").center(50))
    time.sleep(0.8)
    os.system("cls" if os.name == "nt" else "clear")
    print((f"...And the winner is...").center(50))
    time.sleep(0.8)
    print(" ")

    if computer.value >= player.value:
        print ("Computer!".center(50))
        print(f"With a final score of {computer.value} against Player's {player.value}".center(50))
    else:
        print("Player!".center(50))
        print(f"With a final score of {player.value} against Computer's {computer.value}".center(50))
    
    print("*"*50)
    loop = len(player.hand)
    print("Player's hand".center(50))
    print("-"*50)
    for i in range(loop):
        time.sleep(0.5)
        print(f"{player.hand[i]['rank']} of {player.hand[i]['suit']}".center(50))
    time.sleep(0.5)
    print("*"*50)
    print("Computer's hand".center(50))
    print("-"*50)
    loop = len(computer.hand)
    for i in range(loop):
        time.sleep(0.5)
        print(f"{computer.hand[i]['rank']} of {computer.hand[i]['suit']}".center(50))
    time.sleep(0.5)
    print("-"*50)
    input("Press Enter for main menu")


class hand():
    def __init__(self, name):
        self.hand = []
        self.value = 0
        self.aceValue = 0
        self.name = name

    
    def PickACard(self, card):
        self.hand.append(card)
        self.value += card['value']
        if card['rank'] == "Ace":
            self.aceValue = self.value + 13
        del deck[0]
    
    def printHand(self):
        if self.value > 21:
            print(f"{self.name} picked up {self.hand[-1]['rank']} of {self.hand[-1]['suit']} and lost with {self.value}")
            print(f"{self.name} lost")
            print("-"*40)

            print(f"{self.name}'s hand was")
            for cards in self.hand:
                print(f"{cards['rank']} of {cards['suit']}")
            print("-"*40)

            input("Press Enter to continue")

        else:
            if self.aceValue > 0 and self.aceValue <=21:
                self.aceValue = self.value + 13
                print(f"{self.name} have {self.value} or {self.aceValue}")

            else:
                print(f"{self.name} have {self.value}")
            print("-"*40)
            print(f"{self.name} is holding:")

            for cards in self.hand:
                print(f"{cards['rank']} of {cards['suit']}")
            print("-"*40)


LostWith = []
i = 0    
computer = hand("Computer")
deck = setDeck()
fullvalue = 0
while True:

    topCard= deck[0]
    computer.PickACard(topCard)
    if computer.value > 21:
        computer.value -= (computer.hand[-1]['value'])
        del(computer.hand[-1])
        LostWith.append(computer.hand)
        deck = setDeck()
        fullvalue += computer.value
        i+=1
        computer = hand("Computer")
        continue
    if i >100000:
        break

average = fullvalue / len(LostWith)
print (average)