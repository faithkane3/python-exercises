#!/usr/bin/env python
# coding: utf-8

# ## 1. Conditional Basics

# a. prompt the user for a day of the week, print out whether the day is Monday or not
# 
# 

# In[1]:


answer = input("What day of the week is today?: ")
answer == "Monday"


# In[3]:


day = input("What day of the week is today?: ")
def its_monday(day):
    if day == "Monday":
        return True
    else:
        return False
its_monday(day)


# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# 
# 

# In[19]:


def weekend_or_not(day):
    day = input("What day of the week is today?: ")
    if day in ["Saturday", "Sunday"]:
        return "Weekend"
    else: 
        return "Weekday"    
weekend_or_not(day)


# c. create variables and make up values for:
# 
#     -the number of hours worked in one week
#     
#     -the hourly rate
# 
#     -how much the week's paycheck will be
#     
# (write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours)
# 
# 

# In[4]:


hours_worked = 40
hourly_rate = 15.00
paycheck = hours_worked * hourly_rate
paycheck


# ## 2. Loop Basics
# 
# 

# a. While

#     -Create an integer variable i with a value of 5.
#     
#     -Create a while loop that runs so long as i is less than or equal to 15
#     
#     -Each loop iteration, output the current value of i, then increment i by one.

# In[5]:


i = 5
while i <= 15:
    print(i)
    i += 1


#     -Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

# In[6]:


i = 0
while i <= 100:
    print(i,"\n")
    i +=2


# -Alter your loop to count backwards by 5's from 100 to -10.
#     

# In[7]:


i = 100
while i >= -10:
    print(i)
    i -= 5


# -Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

# In[2]:


i = 2
while i <= 1000000:
    print(i ** 2)
    i += 1


#     -Write a loop that uses print to create the output shown below.

# In[3]:


i = 100
while i >= 5:
    print(i)
    i -= 5


# b. For Loops

#     i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

# In[4]:


number = input("Type a number: ")
for i in range(1,11):
    print(f"{number} x {i} = ", int(number) * i) 


#     ii. Create a for loop that uses print to create the output shown below.
# 
# 

# In[5]:


for i in range(1,10):
    print(str(i) * i)


# c. break and continue
# 
# 

# i. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# 
# (Hint: use the isdigit method on strings to determine this). 
# 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
# 
# 

# In[ ]:


#newest attempt
number = input("Type an odd number between 1 and 50: ")
while number.isdigit() == False or int(number) % 2 == 0:
    number = input("Type an odd number between 1 and 50: ")
    continue
for i in range(1,51):
    if i == int(number):
        continue
    print(i)


# d. Input Function 
# 
#     -The input function can be used to prompt for input and use that input in your python code. 
#     
#         -Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
#         
# (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)
# 
# 

# In[ ]:


number = input("Type a positive number between 1 and 50: ")
while number.isdigit() == False or int(number) % 2 != 0:
    number = input("Type a positive number between 1 and 50: ")
    continue
for i in range(1,51):
    if i == int(number):
        continue
    print(i)


# e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.
# 
# 

# In[ ]:


number = input("Type a positive number between 1 and 50: ")
while number.isdigit() == False or int(number) % 2 != 0:
    number = input("Type a positive number between 1 and 50: ")
    continue
number = int(number)
for i in range(number,0,-1):
    print(i)


# ## 3. Fizzbuzz

# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# 
#     -Write a program that prints the numbers from 1 to 100.
#     
#     -For multiples of three print "Fizz" instead of the number
#     
#     -For the multiples of five print "Buzz".
#     
#     -For numbers which are multiples of both three and five print "FizzBuzz".
# 

# In[ ]:


for i in range(1,101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# ## 4. Display a table of powers.
# 
#     -Prompt the user to enter an integer.
#     
#     -Display a table of squares and cubes from 1 to the value entered.
#     
#     -Ask if the user wants to continue.
#     
#     -Assume that the user will enter valid data.
#     
#     -Only continue if the user agrees to.
# 

# In[ ]:


while True:
    integer = int(input("Enter an integer: "))
    for i in range(1, integer):
        square = i ** 2
        cube = i ** 3
        print(square, cube)
    stuff = input("Do you want to continue? Enter Y or N: ")
    if stuff == "Y" or stuff == "y":
        print("Let's keep going.")
        continue
    else:
        print("We're done here.")
        break


# ## Bonus: Research python's format string specifiers to align the table
# 
# 5. Convert given number grades into letter grades.
# 
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
# 
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

# ## Bonus
# 
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
# 
# 6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
# 
# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[ ]:




