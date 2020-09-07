import math


def add(a, b):
    check_types(a, b)
    return a + b


def subtract(a, b):
    check_types(a, b)
    return a - b


def multiply(a, b):
    check_types(a, b)
    return a * b


def log(a):
    check_type(a)
    return math.log(a)


def log10(a):
    check_type(a)
    return math.log10(a)


def check_types(a, b):
    check_type(a, 'First')
    check_type(b, 'Second')


def check_type(param, name=''):
    if param is None:
        raise TypeError

    acceptable_types = [int, float]

    param_type = type(param)

    if param_type not in acceptable_types:
        raise TypeError(f'{name} input parameter must be {acceptable_types}. Instead it is {str(param_type)}')

# map(check_type, [[type1, 'First'], [type2, 'Second']])
#
#
# # iterable
# for x in [[type1, 'First'], [type2, 'Second']]:
#     # x -> [type1, 'First']
#     # *x > type1, 'First'
#     # Dereferencing
#     check_type(*x)
