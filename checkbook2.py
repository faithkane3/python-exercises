from checkbook_funcs import debit as deb
from checkbook_funcs import deposit as dep
from time import sleep as wait

balance = 500
print("\n--- Welcome to your terminal checkbook. ---\n\n")
with open("checkbook_info.txt", "a+") as reader:
    while True:
        #account = input("Please enter your four-digit account number:\n")
        wait(.5)
        print(
        "What would you like to do today?\n\n"
        "1. view current balance\n"
        "2. record a debit (withdrawal)\n"
        "3. record a credit (deposit)\n"
        "4. exit\n"
        )
        choice = input("Your choice: \n")
        while choice not in "1234":
            print("That is not a valid option.\n")
            choice = input("Your choice: \n")
            continue
        if choice == "1":
            wait(1)
            print(f"Your current balance is ${balance}.\n")
            wait(1)
            continue
        elif choice == "2":
            try:
                wait(1)
                debit = int(input("How much would you like to withdrawal? \n"))
                if debit > 0:
                    balance = deb(balance)
                    print(balance)
                continue
            except:
                wait(1)
                print("That is not a valid option.\n")
                continue
        elif choice == "3":
            try:
                wait(1)
                deposit = int(input("How much would you like to deposit? \n"))
                if deposit > 0:
                    balance = dep(deposit)
                    print(balance)
                    wait(1)
                continue
            except:
                print("That is not a valid option.\n")
                continue
        elif choice == "4":
            print("\nThanks! Have a great day.")
            break