def add(a, b):
    if a is None:
        return b

    if b is None:
        return a

    type1 = type(a)
    type2 = type(b)

    acceptable_types = [int, float, complex]

    if type1 not in acceptable_types:
        raise TypeError('First input parameter must be an int. Instead it is ' + str(type1))

    if type2 not in acceptable_types:
        raise TypeError('Second input parameter must be an int. Instead it is ' + str(type2))

    return a + b
