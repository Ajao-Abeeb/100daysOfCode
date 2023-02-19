import random
import sys
import time
score  = 0

def play_guess():
    global score
    print("\n\033[33m Rock Paper Scissor 🎮🎮🎮🎮")
    options = ["rock","paper","scissor"]
    computer_choice = random.choice(options)
    user_choice = input("\n\033[34m Pick rock,paper,scissor: ").lower()
    while user_choice not in options:
        print("invalid choice")
        break
    
    print("\n computer chose ",computer_choice)
    if user_choice == computer_choice:
        print("\033[34m It is a tie")
        score+=0
    elif user_choice == 'rock' and computer_choice == 'scissor':
        print("\033[34m You won ❤❤")
        score +=1
    elif user_choice == 'paper' and computer_choice == 'rock':
            print("\033[34m You won ❤❤")
            score +=1   
    elif user_choice == 'scissor' and computer_choice == 'paper':
            print("\033[34m You won ❤❤")
            score+=1   
    else:
        print("\033[34m You lose 😪😪")
        score-=1
                  
    still_guessing = 'yes'
    print("Did you want to continue yes or no")
    user_option = input()
    while still_guessing == user_option:
           time.sleep(0.6)
           play_guess()
           break    
    else:
        print("Thanks for playing our Game 🎮🎮🎮")
        sys.exit
   
play_guess()

print("Your score is ",score ,"💯💯💯")


