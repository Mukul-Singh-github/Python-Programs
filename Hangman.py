from random import choice

words_list=["tobirama","naruto","football","ronaldinho","lionelmessi","castle",
            "hyroscope","battery","python","mercurial","gameloft","guitar","sasuke"]


def hangstage(life):
  if life == 4:
    print("               ")
    print("               ")
    print("               ")
    print("               ")
    print("         ______")
  
  elif life == 3:
    print("           |   ")
    print("           |   ")
    print("           |   ")
    print("           |   ")
    print("        ___|___")

  elif life == 2:
    print("     ------|   ")
    print("           |   ")
    print("           |   ")
    print("           |   ")
    print("        ___|___")
  
  elif life == 1:
    print("     ------|   ")
    print("     |     |   ")
    print("           |   ")
    print("           |   ")
    print("        ___|___")

def getword():
  return choice(words_list)


def word_per(word):
  return round(len(word)*0.4)


def us_word_gen(word):    #under-score word generator
  """
  creates the under score word of provided word
  """
  i=0
  us_word=list(word)
  while i <= word_per(word):
   letter = choice(range(0,len(word)))
   if us_word[letter] != "_":
     us_word[letter] = "_"
     i+=1
  return us_word,u_list

def comparing_list_gen(word):
  """
  creates the comparing list 
  """
  comparing_list=[]
  for i in range(0,len(word)):
    il=[]
    il.append(word[i])
    il.append(i)
    comparing_list.append(il)
  return comparing_list

def win_check():
  """
  checks if player won
  """
  print(us_word)
  if list(word) == us_word: 
    print("       O         \     ")
    print("    |__|___      /     ")
    print("       |        /      ")
    print("      / \   ___/___    ")  
    print("Hey congratulations you guessed the right word")
    return True
  else: 
    return False

#GAME LOGIC
word = getword()
life = 3
#creating respective under-score word
us_word,u_list = us_word_gen(word)

#creating comapring list
comparing_list = comparing_list_gen(word)

lost_count=0
life = 4

while win_check() == False:
  if life > 0:
    guess = input("enter the letter: ")
    print()

    for [element,element_index] in comparing_list:
      # print("in for")
      if element == guess and us_word[element_index] != guess:
          # print("in if")
          us_word[element_index] = guess
          lost_count+=1
          break
      else:
        lost_count = 0
        
    if lost_count == 0:
      print(f"Oops! Wrong Guess, You have {life-1} lives left")
      print()
      hangstage(life)
      life-=1

  else:
    print("You Lost")
    print("     ------|   ")
    print("     |     |   ")
    print("     O     |   ")
    print("    /|\    |   ")
    print("    / \ ___|___")
    print(f"the word was {word}")
    break
