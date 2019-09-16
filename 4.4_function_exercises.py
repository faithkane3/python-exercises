#!/usr/bin/env python
# coding: utf-8

# ## Exercises
# 
# Create a file named 4.4_function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function.

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[51]:


def is_two(x):
    """ Returns a True if x == number or string 2, otherwise False
    """
    return x in [2, "2"]

assert is_two(2) == True
assert is_two("2") == True
assert is_two(3) == False
assert is_two("two") == False


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
# 

# In[52]:


def is_vowel(let):
    """ is_vowel returns True if letter string is a vowel, False if not
    """
    return len(let) == 1 and let.lower() in "aeiou"

assert is_vowel("A") == True
assert is_vowel("a") == True
assert is_vowel("E") == True
assert is_vowel("ba") == False


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[53]:


def is_consonant(let):
    """use is_vowel to return True if consonant, False if vowel
    """
    #return len(let) == 1 and let not in "aeiou"
    return not is_vowel(let)
assert is_consonant("c") == True
assert is_consonant("r") == True
assert is_consonant("y") == True
assert is_consonant("a") == False


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[54]:


def caps_for_cons(word):
    return word.capitalize() if is_consonant(word[0]) else word
# #     if word[0] in ["a", "e", "i", "o", "u"]:
# #         return word
# #     else:
# #         return word.capitalize()
#     if is_consonant(word):
    

assert caps_for_cons("tony") == "Tony"
assert caps_for_cons("8") == "8"


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[55]:


def calculate_tip(tip, total):
    return f"You should tip ${tip * total} for a total of ${tip * total + total}."

calculate_tip(.2, 20)


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[56]:


def apply_discount(price, discount):
    return f"The price is ${price}, your discount is {discount}, and your new total is ${price - price * discount}."

assert apply_discount(20, .2) == 'The price is $20, your discount is 0.2, and your new total is $16.0.'


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
# 

# In[57]:


def handle_commas(word):
    return float(word.replace(",", ""))

assert handle_commas("2,000") == 2000.0


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
# 

# In[58]:


def get_letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"

assert get_letter_grade(72) == 'C'


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[59]:


def remove_vowels(word):
    """ remove_vowels() returns a word without vowels
    """
    for let in word:
        if let in "aeiou":
            return word.replace(let,"")

assert remove_vowels("happy") == 'hppy'


# In[60]:


# list comprehension version of remove_vowels
def remove_vowels(word):
    """ remove_vowels() returns a word without vowels
    """
    return ''.join([word.replace(let,"") for let in word if let in "aeiou"])

assert remove_vowels("happy") == 'hppy'


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# 
# 
#     -anything that is not a valid python identifier should be removed
# 
#     -leading and trailing whitespace should be removed
# 
#     -everything should be lowercase
# 
#     -spaces should be replaced with underscores
# 
#         for example:
#         
#         Name will become name
# 
#         First Name will become first_name
#         
#         % Completed will become completed

# In[61]:


def normalize_name(word):
    """normalize_name takes a string and returns a valid python identifier
    """
    return word.strip("0123456789!@#$%^&*_() +=\/?<>,.`~;:").lower().replace(" ","_")

normalize_name("% Completed")


# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# 
#     -cumsum([1, 1, 1]) returns [1, 2, 3]
#     
#     -cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[62]:


def cumsum(lst):
    for i in range(1,len(lst)):
        lst[i] = lst[i- 1 ] + lst[i]
    return lst

assert cumsum([1, 1, 1]) == [1, 2, 3]


# ## Bonus
# 
# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. 
# 
# #### Bonus write a function that does the opposite.

# In[63]:


def twelveto24(item):
    """twelveto24() takes in a string time and
    returns the time in a 24-hour format
    """
    #checks that first two chars 12 and last two am
    if item[:2] == "12" and item[-2:] == "am":
        #returns 00:00
        return "00" + item[2:-2] 
    #checks that last two chars are am
    elif item[-2:] == "am" :
        #returns without am
        return item[:-2]
    #checks that last chars are am
    elif item[:-2] == "am":
        #returns the item with a zero added in front
        return "0" + item[:-2] 
    #checks that last two chars are pm and first two 12
    elif item[-2:] == "pm" and item[:2] == "12":
        #returns item
        return item[:-2]
    else:
        return str(int(item[:1]) + 12) + item[1:-2]

assert twelveto24("12:45pm") == '12:45'
assert twelveto24("10:45am") == '10:45'


# #### Bonus Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# 
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27

# In[ ]:




