
#This is Black Jack Game

#HOW TO PLAY THE GAME
#There is a dealer and a player they will both have two random cards from the deck of 52
#the player's always plays first.
#the goal is to have total value of our cards close to 21 aur 21.
#if player's total of two card is suppose 15 player can say hit and he/she will be given a random card form the deck by the dealer
#player can get as many cards as he wants from dealer to make his total colse to 21 or 21
#but if players value reaches above 21 the th player is bust and loses the bet amount
#when player is close to 21 and can get bust player can choose to stay that means no more cards will be served to him
#then plays the dealer.
#a rule for dealer is that he has to hit till his cards value greater than or equals to 17.
#once card value exceeds the limit he has to stay.
#then the value is compared.
#value close to 21 aur 21 wins and is value is 21 the person is called the blackjack and wins the 3 times the bet amount

#NOTE: Ace can have two values 1 or 11 player will have to choose according to his situation which value can take closer to 21 or 21.

values={"ace":[1,11],"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"joker":10,"king":10,"queen":10}
name=["ace","two","three","four","five","six","seven","eight","nine","ten","joker","king","queen"]
types=["clubs","hearts","diamond","spade"]
global player_state
player_state=1

class Card:
    
    def __init__(self,card_name,card_type):
      self.card_name=card_name
      self.card_type=card_type 
      self.card_value=values[card_name]

    def __str__(self):
      return f"{self.card_name} of {self.card_type}"


class Deck:
  def __init__(self):
    self.allcards=[]

    for n in name:
      for t in types:
        card_obj=Card(n,t)    #here of card object will be created
        self.allcards.append(card_obj)

    #shuffle(self.allcards)


class Bank_account:

  def __init__(self,name,balance):
    self.name=name
    self.balance=balance
  
  
  def check_balance(self):
    return f"Your current balance is {self.balance}"

  def deposit(self,deposit_amt):
    self.balance += deposit_amt
    return self.balance
  
  def withdraw(self,withdrawing_amt):
    if withdrawing_amt > self.balance:
      print(f"Not enough balance! withdrawing amount is {withdrawing_amt} while balance is {self.balance}")
    else:
      self.balance -= withdrawing_amt
      return self.balance

  #shuffles the deck
def shuffle_deck(deck):
  from random import shuffle
  shuffle(deck.allcards)


   # hit method
def hit(Who,player_deck,dealer_deck,player_state):
  if Who == "p" and player_state != 0:
    player_deck = player_deck.append(deck.allcards.pop(0))

  elif Who == "d":
    dealer_deck = dealer_deck.append(deck.allcards.pop(0))

  else:
    print("player_state is 0 cannot hit")


  # stay method
def stay():
  global player_state
  player_state=0

def game_reset(player_deck,dealer_deck):
  for i in range(0,len(player_deck)):  #returning cards to deck from players deck
    deck.allcards.append(player_deck.pop(0))

  for i in range(0,len(dealer_deck)):  #returning cards to deck from dealers deck
    deck.allcards.append(dealer_deck.pop(0))
      
  shuffle_deck(deck)
  global player_state
  player_state = 1

  for i in range(0,2):   #two cards for player
    player_deck.append(deck.allcards.pop(0))
  for i in range(0,2):   #two cards for dealer
    dealer_deck.append(deck.allcards.pop(0))
  
  print(f"Your bank balance is {player_acc.balance}")
  bet=int(input("how much you wanna bet! "))
  while bet not in range(100, (player_acc.balance+1)):
    bet=int(input("bet range error!"))
  player_move()



  # Main game logic

def player_situation(player_sum):
  if player_sum > 21:
    print("Player Bust!!, the bet amt is lost ")
    player_acc.balance -= bet
    return True
  elif player_sum == 21:
    print("Player is a BlackJack")
    player_acc.balance+=int(bet+bet*1.5)
    return True
  else:
    return False


def dealer_situation(dealer_sum):
  if dealer_sum > 21:
    player_acc.balance+=(bet+bet)
    print("Deaer Bust!!, Player gets doubled bet amt")
    return True
  if dealer_sum == 21:
    print("Dealer is a BlackJack")
    player_acc.balance -= bet
    return True
  else:
    return False



def win_check(player_sum,dealer_sum,):
  if player_sum > dealer_sum: 
    print("Players total is greater than dealers total, Player Wins!! ","\n",)
    player_acc.balance += (bet+bet)
    return True
  
  elif dealer_sum > player_sum:
    print("Dealers total is greater than Players total, Dealer Wins!! ","\n")
    player_acc.balance -= bet
    return True

  elif dealer_sum == player_sum:
    print("dealers and Players sum is equal, It's a tie!!","\n")
    return True

  else:
    return False
