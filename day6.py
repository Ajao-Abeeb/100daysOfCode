#pass Generator
import random
import string
import sys
print("\n\033[34m Password Generator 🔒🔒🔒")
a =input("\n\033[33m Did you want to generate password: Automatic or Manually\n")

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
       print('choose between')
    still_guessing = 'yes'
    print("Did you want to generate another password: yes or no")
    b = input()
    while still_guessing == b:
           generator()
           break    
    else:
        print("Thanks fors generating")
        sys.exit
generator()      
file = open("Password Save.txt" , 'w') 
file.write(str(pwd))