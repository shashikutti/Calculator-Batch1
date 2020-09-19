import math


def add(num1, num2):
    num1, num2 = convert_to_floats(num1, num2)
    return num1 + num2


def subtract(num1, num2):
    num1, num2 = convert_to_floats(num1, num2)
    return num1 - num2


def multiply(num1, num2):
    num1, num2 = convert_to_floats(num1, num2)
    return num1 * num2


def divide(num1, num2):
    num1, num2 = convert_to_floats(num1, num2)
    return num1/num2


def power(num1, num2):
    num1, num2 = convert_to_floats(num1, num2)
    return num1**num2


def fac(num1):
    num1 = convert_to_float_one_param(num1)
    return math.factorial(num1)


def sqroot(num1):
    num1 = convert_to_float_one_param(num1)
    return math.sqrt(num1)



def log(num1):
    num1, num2 = convert_to_float(num1)
    return math.log(num1)


def log10(num1):
    num1 = convert_to_float(num1)
    return math.log10(num1)


def convert_to_floats(num1, num2):
    num1 = convert_to_float(num1)
    num2 = convert_to_float(num2)
    return num1, num2


def convert_to_float_one_param(num1):
    num1 = convert_to_float(num1)
    return num1


def convert_to_float(param):
    if param is None:
        raise ValueError

    return float(param)

# map(check_type, [[type1, 'First'], [type2, 'Second']])
#
#
# # iterable
# for x in [[type1, 'First'], [type2, 'Second']]:
#     # x -> [type1, 'First']
#     # *x > type1, 'First'
#     # Dereferencing
#     check_type(*x)
