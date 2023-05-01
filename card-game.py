##
## Our python card game
##

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

player_1 = {}
player_2 = {}

# list of all our cards
suit_cards = []

for suit in suits:
    for card in cards:
        suit_cards.append(f"{card} of {suit}")

def shuffle_cards(cards):
    # TODO - fill in code
    print("I am shuffling")

def deal_cards(cards):
    # TODO - fill in code
    print("I am dealing")

def print_cards(cards):
    # TODO - fill in code
    print("I am printing")

def how_to_play():
    print("How to play")

def main():
    print("Welcome to 20/50")
    print("Play game: Y/N or H for help")
    selection = input()

    if selection in ["Y","y"]:
        print("Let's play")
        # how_to_play()
    elif selection in ["H","h"]:
        how_to_play()
    else:
        print("Goodbye")
        exit()

    # shuffle the cards
    # shuffle_cards(suit_cards)

    # # deal cards
    # deal_cards(suit_cards)

    # # print the cards
    # print_cards(suit_cards)

main()
# print(suit_cards)