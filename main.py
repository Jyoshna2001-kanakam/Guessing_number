#Guessing the number
import random

print("GUESS THE NUMBER GAME")
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5

def set_difficulty(level_choosen):
     if level_choosen=='easy':
          return EASY_LEVEL_ATTEMPTS
     elif level_choosen=='hard':
          return HARD_LEVEL_ATTEMPTS
     else:
          print("You have entered wrong level")

def check_answer(guessed_number,answer,attempts):
     if guessed_number<answer:
          print("Your guess is too low...!")
          return attempts-1
     elif guessed_number>answer:
          print("Your guess is too high..!")
          return attempts-1
     elif guessed_number==answer:
          print(f"Your guess is right...The answer was {answer}")
          print("You Won..!!")

def game():
     print("Let me think of a number between 1-50")
     answer=random.randint(1,20)
     print(answer)

     level=input("choose level of difficulty...Type easy or hard:")
     attempts=set_difficulty(level)

     if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
          print("You have entered a wrong level ...play again!!") 
          exit()

     guessed_number=0
     while guessed_number!=answer:
          print(f"You have {attempts} attempts remaining to guess the number.")
          guessed_number=int(input("Guess a number:"))
          attempts=check_answer(guessed_number,answer,attempts)

          if attempts==0:
               print("You are out of attempts...You lose!")
               return
          elif guessed_number!=answer:
               print("Guess again")
game()