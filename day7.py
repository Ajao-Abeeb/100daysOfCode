# The code takes a string as an input and checks if it is a palindrome.
#A palindrome is a word that reads the same backwards as forwards.
#The code checks if the string is the same as its reverse.
#If it is, then it prints True, otherwise it prints False.
#"""
string = input('write a word\n')
def check(string):
    if string.lower() == string[::-1].lower():
        print('True')
    else:
        print('False')
check(string)