############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import random
from os import system
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerCards = {}
houseCards = {}

def deal():
    playerCards["card1"] = random.choice(cards)
    playerCards["card2"] = random.choice(cards)

    houseCards["card1"]= random.choice(cards)

def hitCard(cardStack):
    cardName = "card"+str(len(cardStack)+1)
    cardStack[cardName] = random.choice(cards)

def countValue(cardStack):
    total = 0
    for card in cardStack:
        total+= cardStack[card]
    return total

def printStatus():
    print(f"Your cards are: {playerCards} with a total of {countValue(playerCards)}")
    print(f"House cards are: {houseCards} with a total of {countValue(houseCards)}")

def checkForAnAce(cardStack):
    for card in cardStack:
        if (cardStack [card] == 11):
            cardStack[card] = 1
            return True
    return False

playing = True

while (playing):
    playerCards = {}
    houseCards = {}
    system("cls")
    resp = input ("Do you want to play a game of blackjack $$$ (y/n): ").lower()

    if (resp == "n"):
        playing = False
    elif (resp != "y"):
        playing = False
        print("Wrong answer closing game")
    elif (resp == "y"):
        deal()
        printStatus()

        hit = True
        while (hit):
            if (countValue(playerCards)== 21 and len(playerCards)==2):
                print("You have BlackJack got a win of 1.5X")
                hit= False
            else:
                resp = input("Do you want another card (y/n): ")

                if (resp != "y"):
                    hit = False
                else:
                    hitCard(playerCards)
                    printStatus()

                if (countValue(playerCards)>21 and not checkForAnAce(playerCards)):
                    printStatus()
                    print("You Lose!!!!!!")
                    hit = False
                else:
                    printStatus()
            system("cls")

            sense = True
            while (sense and countValue(playerCards)<=21):
                if (countValue(houseCards)>= countValue(playerCards)):
                    print("The house always win")
                    printStatus()
                    sense = False
                else:
                    hitCard(houseCards)
                    print("The House Draws a card...")
                    if(countValue(houseCards)>21 and not checkForAnAce(houseCards)):
                        print("The houses losses")
                        sense = False
                    printStatus()