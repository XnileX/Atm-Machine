import os
from random import choices
from string import digits

users = {"user1": {"pin": "101010", "accountNo":"5721181718090262", "balance":10000},"user2": {"pin": "121212", "accountNo":"6968190590553343","balance":50000}}
def clear():
    os.system('cls'),os.system('clear')

def RandomCC():
    cc_digits = choices(digits, k=16)
    return "".join(cc_digits)
  
def menu(myuser):
    if (myuser):
        display = f"\tWelcome User {myuser}"
        displayMenu = "Eject Card"
    else:
        display = "\tPlease login first to enable transactions..."
        displayMenu = "Login/Create Account"
    return input((f"""\n\n{display}\t\n
            TRANSACTION 
        *******************
            Menu: 
            0. {displayMenu}
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *******************
        \n\tselect > """))

myuser = ""
while True:
    clear()
    try:
        enter = int(menu(myuser))
    except:
        input("\n\tInvalid options... (press any key)")
        continue
    if myuser == "":
        if enter == 0:
            clear()
            select = int(input((f"""\n\tAccount\n\t********************\n\t1. Login\n\t2. Create Account\n\t3. Back\n\t*********************\n\n\tselect > """)))
            if (select == 1):
                accountNo = input("\n\tInput your Account no : ")
                enter = ""
            elif (select == 2):
                accountNo = str(RandomCC())
                userName = input("\n\tInput your account name : ")
                print(f"\tAccount no : {accountNo}")
                pinNo = input("\tPin no : ")
                if (userName == "" or pinNo==""):
                    input(f"\t{userName} error empty data! (press any key)")
                    continue
                users[userName] = {"pin":pinNo,"accountNo": accountNo,"balance":0}
                input(f"\t{userName} succesfully added! (press any key)")
                continue
            else:
                continue
        elif enter == 5:
            exit()
        else:
            input("\tPlease login first to enable transactions...(press any key)")
            continue
    if enter == 0:
        input(f"\n\tEjecting {myuser} card... (press any key to continue)")
        myuser = ""
        continue
    elif enter == 1:
        clear()
        print("\n\t----------ACCOUNT DETAIL----------")
        print(f"\tAccount Holder: {myuser}")
        print(f"\tAccount Number: {users[myuser]['accountNo']}")
        print(f"\tAvailable balance: PHP. {users[myuser]['balance']}\n")
        input("\n\n\t(press any key to continue)")
        continue
    elif enter == 2:
        clear()
        print("\n\t----------Balance----------")
        print(f"\n\tCurrent account balance: PHP. {users[myuser]['balance']}\n")
        input("\n\n\t(press any key to continue)")
        continue

    elif enter == 3:
        clear()
        try:
            print("\n\t----------Deposit----------")
            val = int(input("\n\tEnter amount to deposit : "))
            users[myuser]['balance'] = (users[myuser]['balance']+val)
            print(f"\n\tCurrent account balance: PHP. {users[myuser]['balance']}\n")
            input("\n\n\t(press any key to continue)")
        except:
            input("\n\n\t--Enter a valid number(press any key to continue)")
        continue
    elif enter == 4:
        clear()
        print("\n----------Withdraw----------")
        try:
            val = int(input("\n\tEnter amount to withdraw : "))
            if (users[myuser]['balance'] < val):
                print(f"\tInsufficient fund!\n\tYour balance is PHP.{users[myuser]['balance']} only.\n\tTry with lesser amount than balance.\n")
                input("\n\n\t(press any key to continue)")
                continue
            else:
                users[myuser]['balance'] = (users[myuser]['balance'] - val)
                print(f"\tPHP.{val} withdrawal successful! \n \tCurrent account balance: PHP.{users[myuser]['balance']}]\n")
                input("\n\n\t(press any key to continue)")
                continue
        except:
            input("\n\n\t--Enter a valid number(press any key to continue)")
            continue
    elif enter == 5:
        exit()
    
    userFound = False
    attempt = 0
    for user in users:
        if (users[user]["accountNo"] == accountNo) :
            while(attempt != 3):
                pincode = (input("\tInput your pin no : "))
                if (users[user]["pin"] == pincode):
                    input(f"\n\tWELCOME : {user}\n\n\t (press any key..)")
                    myuser = user
                    userFound = True
                    break
                else:
                    attempt = attempt + 1
                    print(f"\t--Pin code not match retry({attempt}/3)")
                    if (attempt == 3):
                        input(f"\t---Card Ejecting...(press any key)")
