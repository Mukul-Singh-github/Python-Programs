  
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
count=1
 #PRINTS BOARDS
 
def Board(board):
 # board[position_choice]=variable
  print(board[1]+'|'+board[2]+'|'+board[3])
  print("-----")
  print(board[4]+'|'+board[5]+'|'+board[6])
  print("-----")
  print(board[7]+'|'+board[8]+'|'+board[9])

# user chooses his character and start playing
def choice():
  lst=['X','O']
  character_choice= input("what you wanna choose X or O: ")

  while character_choice not in lst:
        character_choice=input("invalid input for character please pick X or O:  ")
  if character_choice in lst:
    lst.remove(character_choice)
    player2_char=lst.pop()
    print("player two is: ",player2_char)
    return character_choice,player2_char

player1_char,player2_char=choice()

#check if won
def win_check(board):
  print(board)

  if board[1]==board[2]==board[3]== ' ':
    return False
  if board[1]==board[2]==board[3]== 'X' or board[1]==board[2]==board[3]== 'O':
    return True
  elif board[4]==board[5]==board[6]=='X' or board[4]==board[5]==board[6]=='O':
    return True
  elif board[7]==board[8]==board[9]=='X' or board[7]==board[8]==board[9]=='O':
    return True
  elif board[1]==board[4]==board[7]=='X' or board[1]==board[4]==board[7]=='O':
    return True
  elif board[2]==board[5]==board[8]=='X' or board[2]==board[5]==board[8]=='O':
    return True
  elif board[3]==board[6]==board[9]=='X' or board[3]==board[6]==board[9]=='O':
    return True
  elif board[1]==board[5]==board[9]=='X' or board[1]==board[5]==board[9]=='O':
    return True
  elif board[3]==board[5]==board[7]=='X' or board[3]==board[5]==board[7]=='O':
    return True
  else:
    return False

def empty_check(board,position_choice):
  if board[position_choice]== ' ':
   #board[position_choice]==character
   return True
  else:
   print("position is not available please pick another one ")    
   print(board[position_choice])
   return False


#game begins and player 1 makes move 
def game_start(*args):
  count=1

  game_win,win_player = win_check(board)

  while win_check(board)==False:        
    position_choice=int(input("enter a postion (1 to 9):   "))
    while position_choice not in range(1,10):
      position_choice=int(input("invalid:   ")) 
    if count%2!=0:
        #position_choice=int(input("choose your position player1 (0 to 8):   "))
        if empty_check(board,position_choice)==True:
          board[position_choice]=player1_char #no need to pass board as board is global 
          Board(board)
          count+=1
        else:
           print("position taken choose another")
           continue
    else:
       #position_choice=int(input("choose your position player2 (0 to 8):   "))
       while position_choice not in range(1,10):
          position_choice=int(input("invalid:   "))       
       if empty_check(board,position_choice)==True:
         board[position_choice]=player2_char
         Board(board)
         count+=1
       else:
         print("position taken choose another")
         continue
  else:
    print("player won the game")

game_start(player2_char,player1_char,board)
