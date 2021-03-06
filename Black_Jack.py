# Chandler Supple, 2/18/18
# To initialize program, type 'Play()' in a seperate kernel


# libraries
import random   
from time import sleep

# setup

print("Let's begin!\n")
Jack = 'Jack'
Queen = 'Queen'
King = 'King'
Ace = 'Ace'
player_money = 300
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace]
x = 0

class Play():                 # initializes class
    Jack = 'Jack'
    Queen = 'Queen'
    King = 'King'
    Ace = 'Ace'
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace]
    player_money = 300
    def __init__(self):       # main function
        while(1):
            global x
            x = 0
            print('$50 was deducted from your account')
            global player_money
            player_money = player_money - 50
            print("Current Balance: $ %s" % player_money)
            sleep(1)
            print("Dealing Cards...")
            sleep(2)
            x1 = random.randint(0,13)
            x2 = random.randint(0,13)
            x3 = random.randint(0,13)
            x4 = random.randint(0,13)
            card1 = cards[x1]
            card2 = cards[x2]
            card_s = str(card1) + ', and ' + str(card2)
            card_d1 = cards[x3]
            card_d2 = cards[x4]
            global Ace
            Jack = 10
            Queen = 10
            King = 10
            Ace = 11
            if (card_d1 == 'Jack'):
                card_d1 = 10
            if (card_d1 == 'Queen'):
                card_d1 = 10
            if (card_d1 == 'King'):
                card_d1 = 10
            if (card_d1 == 'Ace'):
                card_d1 = 11
            if (card_d2 == 'Jack'):
                card_d2 = 10
            if (card_d2 == 'Queen'):
                card_d2 = 10
            if (card_d2 == 'King'):
                card_d2 = 10
            if (card_d2 == 'Ace'):
                card_d2 = 11
            dealer_card = int(card_d1) + int(card_d2)
            if (dealer_card <= 9):
                x5 = random.randint(0,13)
                card_d3 = cards[x5]
                if (card_d3 == 'Jack'):
                    card_d3 = 10
                if (card_d3 == 'Queen'):
                    card_d3 = 10
                if (card_d3 == 'King'):
                    card_d3 = 10
                if (card_d3 == 'Ace'):
                    card_d3 = 11
                dealer_card = int(card_d1) + int(card_d2) + int(card_d3)
                
            print("Your cards are the following: %s" % card_s)
            sleep(1)
            if (str(card1) == 'Ace'):
                ace_value = int(input('Please choose the value of your ace (1 or 11): '))
                Ace = ace_value
            if (str(card2) == 'Ace'):
                ace_value = int(input('Please choose the value of your ace (1 or 11): '))
                Ace = ace_value
            if (card1 == 'Jack'):
                card1 = 10
            if (card1 == 'Queen'):
                card1 = 10
            if (card1 == 'King'):
                card1 = 10
            if (card1 == 'Ace'):
                card1 = ace_value
            if (card2 == 'Jack'):
                card2 = 10
            if (card2 == 'Queen'):
                card2 = 10
            if (card2 == 'King'):
                card2 = 10
            if (card2 == 'Ace'):
                card2 = ace_value
            card_v = card1 + card2
            move = str(input('Would you like to fold/hit/stand: '))
            if (move == 'hit'):
                while (move == 'hit'):
                    x5 = random.randint(0,12)
                    card3 = cards[x5]
                    print("You got a %s" % card3)
                    if (card3 == 'Jack'):
                        card3 = 10
                    if (card3 == 'Queen'):
                        card3 = 10
                    if (card3 == 'King'):
                        card3 = 10
                    card_v = card1 + card2 + card3
                    if (card_v > 21):
                        print("Bust!")
                        x = 1
                        break
                    move = str(input('Would you like to fold/hit/stand: '))
                    if (move == 'hit'):
                        x5 = random.randint(0,12)
                        card4 = cards[x5]
                        if (card4 == 'Jack'):
                            card4 = 10
                        if (card4 == 'Queen'):
                            card4 = 10
                        if (card4 == 'King'):
                            card4 = 10
                        card_v = card1 + card2 + card3 + card4
                        print("You got a %s" % card4)
                        if (card_v > 21):
                            print("Bust!")
                            x = 1
                            break
                        move = str(input('Would you like to fold/hit/stand: '))
                        if (move == 'hit'):
                            x5 = random.randint(0,12)
                            card5 = cards[x5]
                            if (card5 == 'Jack'):
                                card5 = 10
                            if (card5 == 'Queen'):
                                card5 = 10
                            if (card5 == 'King'):
                                card5 = 10
                            card_v = card1 + card2 + card3 + card4 + card5
                            print("You got a %s" % card5)
                            if (card_v > 21):
                                print("Bust!")
                                x = 1
                                break
                            move = str(input('Would you like to fold/hit/stand: '))
                if (x == 1):
                    break
            if (move == 'fold'):
                print("Folded...")
                break
            if (move == 'stand'):
                pass
            sleep(1)
            while(1):
                bet = int(input('Please place your bet: $'))
                if (bet > player_money):
                    print("You do not have enough money to place that bet!")
                if (bet <= player_money):
                    break
            sleep(1)
            print('Flip your cards!')
            sleep(2)
            player = 21 - card_v
            dealer = 21 - dealer_card
            if (dealer > player):
                print("You won!")
                player_money = player_money + bet
                print("Current balance: %s" % player_money)
            if (dealer < player):
                print("You lost...")
                player_money = player_money - bet
                print("Current balance: %s" % player_money)
            if (dealer == player):
                print("It's a tie.")
            break
