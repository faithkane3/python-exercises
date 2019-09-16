def normalize_name(word):
    """normalize_name takes a string and returns a valid python identifier
    """
    return word.strip("0123456789!@#$%^&*_() +=\/?<>,.`~;:").lower().replace(" ","_")

def cumsum(lst):
    """cumsum takes in a list and returns a list integers from the first list
    each added to the number before it
    """
    for i in range(1,len(lst)):
        lst[i] = lst[i- 1 ] + lst[i]
    return lst