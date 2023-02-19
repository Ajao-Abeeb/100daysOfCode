score = 0
a = input("what is your name \n")
print("Guess the animal")
guess1 = input("which animal lives in the North pole \n")
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
         if guess.lower() == answer.lower():
          # print("correct answer")
              score = score + 1
              still_guessing = False
         else:
             if attempt < 2:
               guess = input("sorry wrong answer. Try again. \n")
         attempt = attempt + 1
    if attempt == 3:
        print("the correct answer is " + answer)

check_guess(guess1,'polar bear')
guess2 = input("what is the name of fastest animal \n")
check_guess(guess2 , 'cheetah')
guess3 = input("who is the animal king \n")
check_guess(guess3 , 'lion')
guess4 = input("which one is a fish \n \
A) Dolphin\n B)Whale\n C)Shark\n D)squid\n TYPE A,B,C or D\n" )
check_guess(guess4 , 'C')
print("your score is "+ str(score))
# print(ans)
