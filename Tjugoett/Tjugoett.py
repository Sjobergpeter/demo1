import random

ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ["hearts", "Diamonds", "Clubs", "Spades"]
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print (len(suits))

deck = {}
for rank in ranks:
    for suit in suits:
        card = {"rank": rank, "suit": suit}
        deck[rank] = card

print (deck)