def extract_time_components(stime):
    """
    >>> extract_time_components('21:30:00')
    {'hours': 21, 'minutes': 30, 'seconds': 0}
    >>> extract_time_components('09:01:53')
    {'hours': 9, 'minutes': 1, 'seconds': 53}
    """
    time_dict = {}
    # for s in stime:
    time_dict.update(
                    {"hours" : int(stime[0:2]),
                    "minutes" : int(stime[3:5]),
                    "seconds" : int(stime[6:])})
    return time_dict

print(extract_time_components('21:30:00'))