print("\n--- Welcome to your terminal checkbook. ---\n\n")
while True:
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
        r =  open("checkbook_info.txt", "r")
        print(f"Your balance is ${r.readline()}")
        r.close()
        wait(1)
        # print(f"Your current balance is ${balance}.\n")
        # wait(1)
        continue

    # choice 2 will subtract a debit from the balance
    elif choice == "2":
        try:
            wait(1)
            debit = float(input("How much would you like to withdrawal? \n"))
            if debit > 0:
                with open("checkbook_info.txt", "r") as r:
                    balance = r.readline()
                    fbalance = float(balance)
                    fbalance -= debit
                with open("checkbook_info.txt", "w") as w:
                    w.write(str(fbalance))
        except(ValueError):
            wait(1)
            print("That is not a valid option.\n")
            continue
    # choice 3 will add a deposit to the balance
    # choice 2 will subtract a debit from the balance
    elif choice == "3":
        try:
            wait(1)
            deposit = float(input("How much would you like to deposit? \n"))
            if deposit > 0:
                with open("checkbook_info.txt", "r") as r:
                    balance = r.readline()
                    fbalance = float(balance)
                    fbalance += deposit
                with open("checkbook_info.txt", "w") as w:
                    w.write(str(fbalance))
        except(ValueError):
            wait(1)
            print("That is not a valid option.\n")
            continue
    # choice 4 will thank the user and exit while True
    elif choice == "4":
        print("\nThanks! Have a great day.")
        break
            

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    