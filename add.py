def add(a, b):
    if a is None:
        return b

    if b is None:
        return a

    type1 = type(a)
    type2 = type(b)

    acceptable_types = [int, float, complex]

    check_type(acceptable_types, type1, 'First')
    check_type(acceptable_types, type2, 'Second')

    return a + b


def check_type(acceptable_types, type, foo):
    if type not in acceptable_types:
        raise TypeError(f'{foo} input parameter must be an int. Instead it is {str(type)}')


def divide(a, b):
    type1 = type(a)
    type2 = type(b)

    if a is None:
        return b

    if b is None:
        return a

    if type1 is not int:
        raise TypeError('First input parameter must be an int. Instead it is ' + str(type1))

    if type2 is not int:
        raise TypeError('Second input parameter must be an int. Instead it is ' + str(type2))

    return a / b