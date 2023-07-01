import psycopg2 
import random
from datetime import datetime , timedelta , date
mydb = psycopg2.connect(
  host="localhost",
  user="postgres",
  password="abeeb2004",
  database="example"
  
)
print("\033[32m     WELCOME TO BOB BANK       ")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM signup")
myresult =mycursor.fetchall()
for x in myresult:
    print(x)

# sql = "DELETE FROM account "
# mycursor = mydb.cursor()
# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")
 
def signup():
  global username
  global name
  name = input("what is your name \n")
  username = input("what is your username \n")
  password =  input("what is your password \n")
  mycursor = mydb.cursor()
  check = ("SELECT username FROM signup WHERE username = %s ")
  checkval = (username,)
  mycursor.execute(check , checkval)
  checkuser = mycursor.fetchone()
  if  checkuser == None :
     sql = "INSERT INTO signup (name,username,password ) VALUES (%s, %s , %s)"
     val = (name,username,password)
     mycursor.execute(sql, val)
     mydb.commit()
     print(mycursor.rowcount, "You have register with our Bank ") 
     login() 
  else:
    print("Username already exist \n Please register again ")
    signup()
 

def login():
  global username
  print("\n\033[33mOK let login to your account\n")
  username = input("\033[37mwhat is your username \n")
  password =  input("what is your password \n")
  mycursor = mydb.cursor()
  sql = ("SELECT * FROM signup WHERE   username =%s and password = %s ")
  val = ( username , password)
  mycursor.execute(sql , val )
  myresult = mycursor.fetchall()
  # print(myresult)
  for x  in myresult:
    print(x[0]+", Welcome to your account\n")
  if myresult == []:
    print("ohh! Sorry wrong information")
    signup()
   

def account():
     global account_number
     current_amount = 0
     saving_amount = 0
     account_number = random.randint(100000 , 999999)
     otp= random.randint(1000, 9999)
     today_date = datetime.today()
     ahead=today_date+timedelta(days=0)
     mycursor = mydb.cursor()
     sql = "INSERT INTO account (username,account_number,current_amount,saving_amount,otp,date ,ahead_date) VALUES(%s,%s,%s,%s,%s,%s,%s) "
     val = (username,account_number,current_amount ,saving_amount,otp,today_date,ahead)
     mycursor.execute(sql ,val )
     mydb.commit() 
     account_mode() 
 

def account_check():
  mycursor = mydb.cursor()
  check = ("SELECT username , account_number FROM account WHERE username = %s ")
  checkval = (username,)
  mycursor.execute(check , checkval)
  checkuser = mycursor.fetchone()
  if  checkuser == None:
   account()
  else:
    account_mode()
    

def account_mode():
    mycursor = mydb.cursor()
    check = ("SELECT username , account_number , current_amount , saving_amount ,otp FROM account WHERE username = %s ")
    checkval = (username,)
    mycursor.execute(check , checkval)
    checkuser = mycursor.fetchone()
    result= checkuser[2] + checkuser[3]
    print("This is your account number \033[34m",  checkuser[1])
    print("\033[37mYour account balance is  \033[34m$" , result)
    print("\033[37mThis is your account pin number \033[34m",  checkuser[4])
    
    print("\n\033[35mCHOOSE YOU ACCOUNT MODE")
    account_num = input("\033[37m1. Saving Account\n2. Current Account\n")
    if account_num == '1':
       print("\n\033[36mCHOOSE YOUR ACCOUNT INQUIRY")
       num =input('\033[37m1. Deposit\n2. Withdraw\n3. Transfer\n')
       if num == '1' :
         deposit()
       elif  num == '2':
         withdraw()
       elif num == '3':
         transfer()
       else:
         account_mode()
    elif account_num == '2':
       print("\n\033[36mCHOOSE YOUR ACCOUNT INQUIRY")
       num =input('\033[37m1. Deposit\n2. Withdraw\n3. Loan\n')
       if num == '1':
         current_deposit()
       elif num == '2':
         current_withdraw()
      #  --------------------------------------------------------------------------------------------------------
 
       
def deposit():
  mycursor = mydb.cursor()
  check = ("SELECT saving_amount FROM account WHERE username = %s")
  checkval = (username,)
  mycursor.execute(check, checkval)
  myres = mycursor.fetchone()
  saving_amount = int(myres[0]) 
  amount = int(input("how much did you want to deposit\n"))
  current = saving_amount + amount
  saving_amount = current
  if amount <= 1000: 
      sql = "UPDATE account SET saving_amount =  %s WHERE username = %s"
      val = ( saving_amount , username)
      mycursor.execute(sql , val)
      mydb.commit()
      print("Your account balance is $",saving_amount)
  else:
    print("Please deposit it to your current account ")
    account_mode()
  
def withdraw():
  mycursor = mydb.cursor()
  check = ("SELECT saving_amount FROM account WHERE username = %s")
  checkval = (username,)
  mycursor.execute(check, checkval)
  myres = mycursor.fetchone()
  saving_amount = int(myres[0]) 
  amount = int(input("how much did you want to withdraw\n"))
  if saving_amount < amount:
    print('Oops,fund your account \nYour account balance is ',saving_amount)
  else :
    current = saving_amount - amount
    saving_amount = current 
    sql = "UPDATE account SET saving_amount =  %s WHERE username = %s"
    val = ( saving_amount , username)
    mycursor.execute(sql , val)
    mydb.commit()
    print("Your account balance is $",saving_amount)
  
def transfer():
  global receiver_account_number
  mycursor = mydb.cursor()
  account_number = input("Input your account number\n")
  check = ("SELECT account_number FROM account WHERE username = %s and account_number = %s")
  checkval = (username, account_number)
  mycursor.execute(check, checkval)
  myres = mycursor.fetchone()
  # print(myres)
  if myres == None :
    print("your account number is not correct")
    account_mode
  else :
       mycursor = mydb.cursor()
       check = ("SELECT saving_amount FROM account WHERE username = %s")
       checkval = (username,)
       mycursor.execute(check, checkval)
       myres = mycursor.fetchone()
       saving_amount = int(myres[0]) 
       amount = int(input("how much did you want to transfer\n"))
       if saving_amount > amount :
                current = saving_amount - amount
                saving_amount = current 
                receiver_account_number =int(input("Input the receiver account number\n"))
                check_receiver = ("SELECT account_number , username  FROM account WHERE account_number =%s")
                check_receiver_val = (receiver_account_number,)
                mycursor.execute(check_receiver , check_receiver_val)
                myreceiver = mycursor.fetchall()
                if myreceiver == []:
                 print("Wrong account number")
                 account_mode()
                else:
                  print("Are you sure you want to proceed the transfer to " , myreceiver[0][1] ,"\n")
                  sure = input("1.Proceed\n2.Abort\n")
                  if sure == '1':
                      update = "UPDATE account SET saving_amount =%s WHERE username=%s "
                      val = (saving_amount, username)
                      mycursor.execute(update ,val)
                      mydb.commit()
                      print("Your account balance is $",saving_amount)
                      if myreceiver[0][0] == receiver_account_number:
                        receiver_2 = ("SELECT saving_amount FROM account WHERE account_number =%s")
                        check_receiver_val_2 = (receiver_account_number,)
                        mycursor.execute(receiver_2 , check_receiver_val_2)
                        myreceiver_2 = mycursor.fetchone()
                        receiver_amount = amount + int(myreceiver_2[0])

                        update2 = "UPDATE account SET saving_amount = %s WHERE account_number = %s"
                        val2 = (receiver_amount , receiver_account_number)
                        mycursor.execute(update2 , val2)
                        mydb.commit()
                        print("Transaction is done successfully")
                  else:
                    account_mode()
       else:
         print("Fund your account")
         account_mode()
           
def current_deposit():
  mycursor = mydb.cursor()
  check = ("SELECT current_amount FROM account WHERE username = %s")
  checkval = (username,)
  mycursor.execute(check, checkval)
  myres = mycursor.fetchone()
  current_amount = int(myres[0]) 
  amount = int(input("how much did you want to deposit\n"))
  current = current_amount + amount
  current_amount = current
  if amount > 1000: 
      sql = "UPDATE account SET current_amount =  %s WHERE username = %s"
      val = ( current_amount , username)
      mycursor.execute(sql , val)
      mydb.commit()
      print("Your account balance is $",current_amount)
  else:
    print("Please deposit it to your saving account ")
    account_mode()

def current_withdraw():
  mycursor = mydb.cursor()
  check = ("SELECT current_amount,ahead_date, username FROM account WHERE username = %s")
  checkval = (username,)
  mycursor.execute(check, checkval)
  myres = mycursor.fetchone()
  current_amount = int(myres[0]) 
  today_date = date.today()
  print(today_date)
  update = "UPDATE account SET date = %s WHERE username=%s"
  update_val = (today_date , username)
  mycursor.execute(update , update_val)
  mydb.commit()
  ahead= myres[1]
  print(ahead)
  amount = int(input("how much did you want to withdraw\n"))
  current = current_amount - amount
   
  if today_date >= ahead :
    if current_amount >= amount: 
      sql = "UPDATE account SET current_amount =  %s WHERE username = %s"
      val = ( current , username)
      mycursor.execute(sql , val)
      mydb.commit()
      print("Your account balance is $",current)
    else:
      print("Funds your account")
      account_mode()
  else:
    print('Sorry you are just a fresher')
        
   
  
num1 = input("\033[37m1. Did you want to create account \n2. Did you want to login to your account\n")
print('PRESS 1 0r 2 for options')



if num1 == '1' :
  print("Ok let start to create account")
  signup()
  account_check()
  # account()

  
elif  num1 == '2': 
  login()
  account_check()

else:
  print("Welcome to our bank")
  signup()
 

