def normalize_name(word):
    """normalize_name takes a string and returns a valid python identifier
    """
    return word.strip("0123456789!@#$%^&*_() +=\/?<>,.`~;:").lower().replace(" ","_")

def cumsum(lst):
    for i in range(1,len(lst)):
        lst[i] = lst[i- 1 ] + lst[i]
    return lst