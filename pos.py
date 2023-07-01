import psycopg2

mydb = psycopg2.connect(
    host = 'localhost',
    password = 'abeeb2004',
    user = 'postgres',
    database = 'example'
)
def run():
   global num
   global mycursor
   print("WELCOME TO BOB POS AGENT\n")
   print("Choose 1 or 2 in the option\n")
   num = int(input("1. Create Admin section\n2. Login to Admin section\n"))
   mycursor = mydb.cursor()
   if num == 1:
    signup()
   elif num == 2:
    login()
   else:
    print("Sorry please signup or login")
    run()
def signup():
    name = 'BOB POS AGENT'
    username = input("Input your username\n")
    password = input("Input your Password\n")
    select = ("SELECT  username FROM admin")
    sel = (username,)
    mycursor.execute(select,sel)
    if int(mycursor.rowcount) < 2 :
        sql = "INSERT INTO admin (name,username,password) VALUES (%s,%s,%s)"
        val = (name,username,password)
        mycursor.execute(sql,val)
        mydb.commit()
        login()
    else:
        print("It only allow two Admin")
def login():
    global username
    print("\nOk, let login your account\n")
    username = input("Input your username\n")
    password = input("Input your Password\n")
    select = ("SELECT * FROM admin WHERE username=%s and password=%s")
    val = (username,password)
    mycursor.execute(select,val)
    myresult = mycursor.fetchall()
  # print(myresult)
    for x  in myresult:
      print(x[0]+", Welcome to your account\n")
      choose_mode()
    if myresult == []:
      print("ohh! Sorry wrong information")
      print("please create account")
      run()
def choose_mode():
    print("\n\033[35mCHOOSE YOU ACCOUNT MODE")
    account_num = input("\033[37m1. Saving Account\n2. Current Account\n")
    if account_num == '1':
       print("\n\033[36mCHOOSE YOUR ACCOUNT INQUIRY")
       num =input('\033[37m1. Deposit\n2. Withdraw\n3. Transfer\n')
       if num == '1':
           deposit()
       elif num == '2':
           withdraw()
       elif num == '3':
           transfer()
    elif account_num == '2':
       print("\n\033[36mCHOOSE YOUR ACCOUNT INQUIRY")
       num =input('\033[37m1. Deposit\n2. Withdraw\n3. Transfer\n')
       if num == '1':
           deposit_current()
       elif num == '2':
           withdraw_current()
       elif num == '3':
           transfer_current()
           
    else:
        print("sorry provide neccessary information")
def deposit():
    mycursor=mydb.cursor()
    otp = int(input("What is your pin number\n"))
    select = ("SELECT otp,saving_amount,username FROM account WHERE otp =%s")
    val = (otp,)
    mycursor.execute(select,val)
    check = mycursor.fetchone()
    # print(check)
    if check == None:
        print("Wrong pin number")
        deposit()
    else:
        amount= int(input(f"{check[2]},How much did you want to deposit\n"))
        if amount <= 50000:
            saving_amount = amount + check[1]
            # print(saving_amount)
            saving_amount = saving_amount - 5 
            update = "UPDATE account SET saving_amount =%s  WHERE otp=%s"
            val = (saving_amount ,otp)
            mycursor.execute(update,val)
            mydb.commit()
            print("Deposited successfully")
        else:
            print("The money is much, pls transfer it to your current")

def deposit_current():
    mycursor=mydb.cursor()
    otp = int(input("What is your pin number\n"))
    select = ("SELECT otp,current_amount,username FROM account WHERE otp =%s")
    val = (otp,)
    mycursor.execute(select,val)
    check = mycursor.fetchone()
    # print(check)
    if check == None:
        print("Wrong pin number")
        deposit()
    else:
        amount= int(input(f"{check[2]},How much did you want to deposit\n"))
        if amount >= 50000 and amount <=100000:
            current_amount = amount + check[1]
            # print(saving_amount)
            current_amount = current_amount - 5 
            update = "UPDATE account SET current_amount =%s  WHERE otp=%s"
            val = (current_amount ,otp)
            mycursor.execute(update,val)
            mydb.commit()
            print("Deposited successfully")
        else:
            print("The money is much, pls carry it to bank")
def withdraw():
    mycursor=mydb.cursor()
    otp = int(input("What is your pin number\n"))
    select = ("SELECT otp,saving_amount,username FROM account WHERE otp =%s")
    val = (otp,)
    mycursor.execute(select,val)
    check = mycursor.fetchone()
    # print(check)
    if check == None:
        print("Wrong pin number")
        withdraw()
    else:
        amount= int(input(f"{check[2]},How much did you want to Withdraw \n"))
        if amount <= check[1] -5:
            saving_amount = check[1] - amount 
            saving_amount = saving_amount - 5
            update = "UPDATE account SET saving_amount =%s  WHERE otp=%s"
            val = (saving_amount ,otp)
            mycursor.execute(update,val)
            mydb.commit()
            print(f"Your account balance is {saving_amount}")
            print("Withdraw successfully")
        else:
            print("Hmm,Insufficient funds")
def transfer():
    mycursor=mydb.cursor()
    otp = int(input("What is your pin number\n"))
    select = ("SELECT otp,saving_amount,username FROM account WHERE otp =%s")
    val = (otp,)
    mycursor.execute(select,val)
    check = mycursor.fetchone()
    # print(check)
    if check == None:
        print("Wrong pin number")
        transfer()
    else:
       mycursor = mydb.cursor()
       check = ("SELECT saving_amount FROM account WHERE otp = %s")
       checkval = (otp,)
       mycursor.execute(check, checkval)
       myres = mycursor.fetchone()
       saving_amount = int(myres[0]) 
       print(saving_amount)
       amount = int(input("how much did you want to transfer\n"))
       if  saving_amount - 5 > amount  :
                current = saving_amount - amount 
                saving_amount = current - 5
                receiver_account_number =int(input("Input the receiver account number\n"))
                check_receiver = ("SELECT account_number , username  FROM account WHERE account_number =%s")
                check_receiver_val = (receiver_account_number,)
                mycursor.execute(check_receiver , check_receiver_val)
                myreceiver = mycursor.fetchall()
                if myreceiver == []:
                 print("Wrong account number")
                 transfer()
                else:
                  print("Are you sure you want to proceed the transfer to " , myreceiver[0][1] ,"\n")
                  sure = input("1.Proceed\n2.Abort\n")
                  if sure == '1':
                      update = "UPDATE account SET saving_amount =%s WHERE otp =%s "
                      val = (saving_amount, otp)
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
        print("Insufficient fund")
    
        
             
run()