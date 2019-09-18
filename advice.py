import random
import string

## Generate a random string of specific characters 
def rand_string():
    letter = 'abcdefghij'
    return random.choice(letter)

def advice():
    let = rand_string()
    advice_dict = {
                    "a" : "Life really does begin at forty. Up until then, you are just doing research. Carl Gustav Jung",
                    "b" : "Remember life is an adventure!",
                    "c" : "Baggage is the stuff in life you wouldn't leave the house without.",
                    "d" : "Reality is just an illusion, albeit a very persistent one.",
                    "e" : "Life doesn't imitate art; it imitates bad tv.",
                    "f" : "Life is a question and how we live it is our answer. -Gary Keller",
                    "g" : "Persist while others are quitting. -William Arthur Ward",
                    "h" : "The pen is mightier than the sword, if you shoot that pen out of a gun. -Stephen Colbert",
                    "i" : "Those who believe in telekinesis, raise my hand. -Kurt Vonnegut",
                    "j" : "If you try to fail, and succeed, which have you done? -George Carlin"
                    }
    
    for advice in advice_dict:
        return advice_dict[let]

print(" \n ")
print(advice())
print(" \n ")