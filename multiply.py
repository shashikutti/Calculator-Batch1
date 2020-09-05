def multiply(a, b):
    if a is None:
        return b
    if b is None:
        return a

    type1 = type(a)
    type2 = type(b)

    map(check_type, [[type1, 'First'], [type2, 'Second']])

    return a * b


def check_type(acceptable_types, type, foo):
    if type not in acceptable_types:
        raise TypeError(f'{foo} input parameter must be an int. Instead it is {str(type)}')
