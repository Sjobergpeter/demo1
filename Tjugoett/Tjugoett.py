import random
import os

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
            input("Press Enter to continue")
            return
        if self.aceValue > 0:
            self.aceValue = self.value + 13
            print(f"You have {self.value} or {self.aceValue}")
        else:
            print(f"You have {self.value}")
        print("You're holding:")
        for cards in self.hand:
            print(f"{cards['rank']} of {cards['suit']}")
        
# random.shuffle(deck)

while True:
    player = hand("Player")
    computer = hand("Computer")
    deck = setDeck()
    topCard = deck[0]   
    os.system("cls" if os.name == "nt" else "clear")
    print(".:              Twentyone             :.")
    print("-"*40)
    print("Welcome to a game of Twentyone")
    print("-"*40)
    print("Rules / Start / Exit")
    user_input = input("> ")
    if user_input.lower() == "rules":
        os.system("cls" if os.name == "nt" else "clear")
        print("""The game works as follows: the user receives one card at a time and after each card, they decide whether they want another card or not.

The goal for the user is to try to get the sum of the card values as close to 21 as possible without exceeding this number.

Aces can be counted as either 1 or 14.

If the user goes over 21, they lose, and the computer wins.

If the user decides to stop under 21, the computer also draws one card at a time and after each card decides whether to continue or not.

If the computer gets more than 21 points or fewer points than the user, the user wins; otherwise, the computer wins.
""")
        input("Press Enter to continue")
        continue
    
    elif user_input.lower() == ("start"):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            player.PickACard(topCard)
            topCard = deck[0]
            player.printHand()
            if player.value > 21:
                break
            user_input = input("Do you want to pick another card? y/n")
            if user_input == "y":
                continue
            else:
                break

    elif user_input.lower() == "exit":
        break
    continue
    break