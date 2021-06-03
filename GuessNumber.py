from random import choice
num=choice(range(1,100))
# print(num)
lives = 5
print("Number is between 1 and 100 you have to guess it")
print("NOTE: you have 5 lives")
no_guess = 0

while no_guess != num:
  no_guess = int(input("Guess the number: "))
  if no_guess in range(1,101):
    if lives >= 1 :
      if abs(no_guess-num) >= 20 and no_guess > num:
        print("Too High")
        lives-=1
        print(f"{lives} left")

      elif abs(no_guess-num) >= 20 and no_guess < num:
        print("Too Low")
        lives-=1
        print(f"{lives} left")

      elif abs(no_guess-num) <= 10 and no_guess > num:
        print("High")
        lives-=1
        print(f"{lives} left")

      elif abs(no_guess-num) <= 10 and no_guess < num:
        print("Low")
        lives-=1
        print(f"{lives} left")

    else: 
      print("You ran out lives: ")
      print(f"the number was {num}")
      break
  else:
    print("give no between 1 and 100")
else:
  print("Hey! You guessed the number ")
