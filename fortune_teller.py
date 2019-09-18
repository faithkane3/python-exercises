from random import randint
num = randint(0,11)
with open("fortunes.txt") as f:
    fortune = f.readlines()
    print(" \n ")
    print(fortune[num])
    print(" \n ")
