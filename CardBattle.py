#Card Battle / War
#Basically in this the deck of card is equally distributed among two players
#Players pick out the card on by one from their share of deck and are not allowed to see which card they are picking
#The player who have a card with greater value takes another players card and keeps it in his deck.
#There might occur a situation that both players have same card value (ex. 3 of hearts - 3 of spade)
#This is the condition of war
#Players have to keep certain number of cards (8 in our code) on stake, and then take out another card player who will have greater value of card wins this time and takes opponent's cards.
#The player who will be having less than 9 cards remaining will lose.

# NOTE: In our code player doesn't have to play because the only play is to pick a card that players are not allowed to see. However by adding input function it can be done. 





class Cards:

  def __init__(self,card_name,card_type="str"):
    self.card_value=values[card_name]
    self.card_type=card_type
    self.card_name=card_name
  
  def __str__(self):
    return self.card_name +" of "+ self.card_type


from random import shuffle
class Deck():

  def __init__(self):
    self.all_card=[]
   
    for t in types:
     for n in name:
      card_obj=Cards(n,t)
      self.all_card.append(card_obj)

    shuffle(self.all_card)
    
deck=Deck()


#game logic

player1_deck = deck.all_card[:int(len(deck.all_card)/2)]
player2_deck = deck.all_card[int(len(deck.all_card)/2):]


def card_display(player1_deck, player2_deck):
  
  print("|"+str(player1_deck[0]) +"|"  ,  "|"+str(player2_deck[0])+"|")
 


def war_win_check():
  if len(player1_deck) == len(deck.all_card):
    print("congratulations player1 has won the game!! ")
    return True
  elif len(player1_deck) == len(deck.all_card):
    print("congratulations player2 has won the game!! ")
    return True
  else:
    return False


def check_enough_cards(player1_deck,player2_deck,k):
  if len(player1_deck)<k:
    print(f"len of dec1 is {len(player1_deck)}")
    print("player1 does not have enough cards ")
    print("congratulations player2 has won the game!! ")
    return True
  elif len(player2_deck)<k:
    print(f"len of dec2 is {len(player2_deck)}")
    print("player2 does not have enough cards ")
    print("congratulations player1 has won the game!! ")
    return True
  else:
    return False



def condition_war( player1_deck,player2_deck,k,count ):
  j=0 
  # print(len(player1_deck))
  # print(len(player2_deck))
  #if check_enough_cards(player1_deck,player2_deck,k)==True:
    #return 0
  if player1_deck[0+k].card_value > player2_deck[0+k].card_value:
    card_display(player1_deck, player2_deck) 
    print(f"player1 {player1_deck[0+k]} has taken the war over player2 {player2_deck[0+k]}")
    try:
      while j<k:
        player1_deck.append(player2_deck.pop(0+j))
        j+=1
      count+=1
    except IndexError:
      print("player1 does not have enough card!")
      return 0
    finally:
      count+=1
   
            
  elif player1_deck[0+k].card_value < player2_deck[0+k].card_value:     
    print(f"player2 {player2_deck[0+k]} has taken the war over player1 {player1_deck[0+k]}")
    try:
      while j<k:
          player2_deck.append(player1_deck.pop(0+j))
          j+=1
      count+=1
    except IndexError:
      print("plaer2 does not have enough card!")
      return 0
    finally:
      count+=1
  else:
    print("recurssion war")
    k+=9
    condition_war(player1_deck,player2_deck,k,count)

  
k=9  # This variable will help us compare the latest value in player deck and pop that latest value if lose and also is the minimum limit of cards a player can have
import random
while war_win_check()!=True :


  if count!=26 and check_enough_cards(player1_deck,player2_deck,k)!=True :
       
    if player1_deck[0].card_value > player2_deck[0].card_value:     #Comparing if player1 is greater than player2
      card_display(player1_deck, player2_deck)
      print(f" p1 won ",end="\n\n")
      player1_deck.append(player2_deck.pop(0))
      player1_deck.append(player1_deck.pop(0))
      count+=1
            

    elif player1_deck[0].card_value < player2_deck[0].card_value:     #Comparing if player2 is greater than player2
      card_display(player1_deck, player2_deck)
      print(f" p2 won ",end="\n\n")      
      player2_deck.append(player1_deck.pop(0))
      player2_deck.append(player2_deck.pop(0))
      count+=1


    else:
      print("war")
      #print(player1_deck[0])
      #print(player2_deck[0])
      print(f"war condition has occured. Each players has 8 cards on stake!! ",end="\n\n")
      condition_war( player1_deck, player2_deck,k,count )
      k=9
      print(len(player1_deck))
      print(len(player2_deck))
  
  elif count==26 and check_enough_cards(player1_deck,player2_deck,k)!=True :
    count=0
    print("new round")
    random.shuffle(player1_deck)
    random.shuffle(player2_deck)

  else:
    break  
