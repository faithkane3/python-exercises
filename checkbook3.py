from checkbook_funcs import debit as deb
from checkbook_funcs import deposit as dep
from time import sleep as wait

print("\n--- Welcome to your terminal checkbook. ---\n\n")
# Open read/write text file as f
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
    # if user doesn't choose 1, 2, 3, or 4 they will be prompted again for valid input
    while choice not in "1234":
        print("That is not a valid option.\n")
        choice = input("Your choice: \n")
        continue
    # choice 1 will print out current balance and return to prompt for 1, 2, 3, or 4
    if choice == "1":
        wait(1)
        with open("checkbook_info.txt", "r") as reader:
            print(reader.readline())
            reader.close()
            wait(1)
            # print(f"Your current balance is ${balance}.\n")
            # wait(1)
            continue
    # choice 2 will prompt for withdrawal amount and run deb() to subtract amount from balance
    elif choice == "2":
        #try:
        wait(1)
        debit = int(input("How much would you like to withdrawal? \n"))
        if debit > 0:
            balance = deb(balance)
            print(balance)
            continue
        # except:
        #     wait(1)
        #     print("That is not a valid option.\n")
        #     continue
    # choice 3 will prompt user for deposit amount and run dep() to add amount to balance
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
    # choice 4 will thank the user and exit while True
    elif choice == "4":
        print("\nThanks! Have a great day.")
        break