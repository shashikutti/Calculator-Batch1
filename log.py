import numpy as np


def log(a):
    if a is None:
        return None
    acceptable_types = [int, float]

    type1 = type(a)

    if type1 not in acceptable_types:
        raise TypeError('Input parameter must be an int. Instead it is ' + str(type1))

    if type1 is None:
        raise TypeError('Input parameter must be an int. Instead it is Null')

    return np.log(a)
