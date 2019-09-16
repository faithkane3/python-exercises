print("\n--- Welcome to your terminal checkbook. ---\n\n")
while True:
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
        print(f"Your current balance is {balance}.\n")
        continue
    elif choice == "2":
        try:
            debit = float(input("How much would you like to withdrawal? \n"))
            continue
        except:
            print("That is not a valid option.\n")
            continue
    elif choice == "3":
        try:
            deposit = float(input("How much would you like to deposit? \n"))
            continue
        except:
            print("That is not a valid option.\n")
            continue
    elif choice == "4":
        print("\nThanks! Have a great day.")
        break