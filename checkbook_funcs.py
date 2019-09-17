# from random import randint
# balance = random.randint(100, 5000)

#balance = 500
# print(balance)

def debit(num):
    balance -= num
    return balance

def deposit(num):
    balance += num
    return balance