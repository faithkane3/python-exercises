# number 1
def isnegative(num):
    """>>> from solutions import isnegative
    >>> type(isnegative(0))
    <class 'bool'>
    >>> isnegative(4)
    False
    >>> isnegative(0)
    False
    >>> isnegative(-6)
    True"""
    return num < 0

# number 2
def count_evens(lst):
    """>>> from solutions import count_evens
    >>> type(count_evens([1, 2, 3]))
    <class 'int'>
    >>> count_evens([1, 2, 3])
    1
    >>> count_evens([4, 6, 8, 10, 12])
    5
    >>> count_evens([1, 3, 5, 7, 9])
    0
    >>> count_evens([])
    0
    >>> count_evens([3, 2])
    1
    """
    return len([num for num in lst if num % 2 == 0])

# number 3
def increment_odds(nums):
    """>>> from solutions import increment_odds
    >>> type(increment_odds([1, 2, 3]))
    <class 'list'>
    >>> increment_odds([1, 2, 3])
    [2, 2, 4]
    >>> increment_odds([2, 2, 1, 4, 5])
    [2, 2, 2, 4, 6]
    >>> increment_odds([])
    []
    >>> increment_odds([0, 1])
    [0, 2]"""
    new_nums = []
    for num in nums:
        if num % 2 != 0:
            num = num + 1
            new_nums.append(num)
        else:
            num = num
            new_nums.append(num)
    return new_nums

# number 4
def average(lst):
    """>>> from solutions import average
    >>> type(average([1, 2, 3]))
    <class 'float'>
    >>> average([1, 2, 3])
    2.0
    >>> average([4, 6, 8, 10, 12])
    8.0
    >>> average([1, 2])
    1.5
    """
    mean = sum(lst) / len(lst)
    return mean


# number 5
def name_to_dict(name):
    """>>> from solutions import name_to_dict
    >>> type(name_to_dict('Ada Lovelace'))
    <class 'dict'>
    >>> name_to_dict('Ada Lovelace')
    {'first_name': 'Ada', 'last_name': 'Lovelace'}
    >>> name_to_dict('Marie Curie')
    {'first_name': 'Marie', 'last_name': 'Curie'}
    """
    name_lst = name.split(" ")
    name_dict = {}
    name_dict["first_name"] = name_lst[0]
    name_dict['last_name'] = name_lst[1]
    return name_dict



# number 6
def capitalize_names(lst):
    """>>> from solutions import capitalize_names
    >>> names = []
    >>> names.append({'first_name': 'ada', 'last_name': 'lovelace'})
    >>> names.append({'first_name': 'marie', 'last_name': 'curie'})
    >>> names
    [{'first_name': 'ada', 'last_name': 'lovelace'}, {'first_name': 'marie', 'last_name': 'curie'}]
    >>> type(names)
    <class 'list'>
    >>> capitalize_names(names)
    [{'first_name': 'Ada', 'last_name': 'Lovelace'}, {'first_name': 'Marie', 'last_name': 'Curie'}]
    >>> type(capitalize_names(names))
    <class 'list'>
    """
    for person in lst:
        person["first_name"] = person["first_name"].capitalize()
        person["last_name"] = person["last_name"].capitalize()
    return lst


# number 7
def count_vowels(word):
    """>>> from solutions import count_vowels
    >>> type(count_vowels('codeup'))
    <class 'int'>
    >>> count_vowels('codeup')
    3
    >>> count_vowels('abcde')
    2
    >>> count_vowels('why')
    0
    """
    return len([let for let in word if let in "aeiou"])


# number 8
def analyze_word(word):
    """>>> from solutions import analyze_word
    >>> type(analyze_word('codeup'))
    <class 'dict'>
    >>> analyze_word('codeup')
    {'word': 'codeup', 'n_letters': 6, 'n_vowels': 3}
    >>> analyze_word('abcde')
    {'word': 'abcde', 'n_letters': 5, 'n_vowels': 2}
    >>> analyze_word('why')
    {'word': 'why', 'n_letters': 3, 'n_vowels': 0}
    """
    my_dict = {}
    my_dict["word"] = word
    my_dict["n_letters"] = len(word)
    my_dict["n_vowels"] = len([let for let in word if let in "aeiou"])
    return my_dict


if __name__ == "__main__":
    import doctest
    doctest.testmod()
