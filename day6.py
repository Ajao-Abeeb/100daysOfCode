#pass Generator
import random
import string
import sys
print("\n\033[34m Password Generator 🔒🔒🔒")
a =input("\n\033[32m Did you want to generate password: Automatic or Manually\n")

def generator():
    if a == 'Automatic' :
        global pwd 
        number = string.digits
        letter = string.ascii_letters
        special_char = string.punctuation
        
        password = number + letter + special_char
         
        #generate  password
        pwd_length = 12
        pwd = ''
        for i in range(pwd_length):
            pwd +=''.join(random.choice(password))
        print(pwd)
    elif a == 'Manually':
     
        number = input("\033[34m what year are you born\n")
        name = input('what is your name\n')
        special_char = string.punctuation
        
        password = number+name +special_char
        pwd = ''
        # how word to generate
        pwd_length = 12
        for i in range(pwd_length):
            pwd +=''.join(random.choices(password))
        print(pwd)
    else:
        sys.exit
    still_guessing = 'yes'
    print("Did you want to generate another password: yes or no")
    b = input()
    while still_guessing == b:
           generator()
           break    
    else:
        print("Thanks for generating")
        sys.exit
generator() 
try:     
   file = open("Password Save.txt" , 'w') 
   file.write(str(pwd))
   file.close()
except NameError as v:
    v = "No password is save"
    print('Password is not going to save in Password save.txt')
#The code is a password generator. It generates a password for you. You can choose to generate a password automatically or manually.
#If you choose to generate a password automatically, the program will generate a random password for you.
#If you choose to generate a password manually, the program will ask you to input your name and year of birth and then it will generate a password for you.
#The program will also save the generated password in a file called Password Save.txt.
#"""