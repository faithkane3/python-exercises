import functions_exercises
from functions_exercises import is_two
from functions_exercises import is_consonant as iscon

question = functions_exercises.is_vowel("t")
print(question)

num_check = is_two(3)
print(num_check)

check = iscon("t")
print(check)

# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
from itertools import product
prod = list(product("abc", "123"))
num = len(prod)
print(prod)
print(f"There are {num} possible combinations.")

# 2. How many different ways can you combine two of the letters from "abcd"?

from itertools import combinations_with_replacement as cwr
combo = list(cwr("abcd", 2))
length = len(combo)
print(combo)
print(f"There are {length} possible combinations.")

# 2. Number 2 using permutations instead of combinations_with_replacement

from itertools import permutations as per
combo = list(per("abcd", 2))
length = len(combo)
print(combo)
print(f"There are {length} possible combinations.")
