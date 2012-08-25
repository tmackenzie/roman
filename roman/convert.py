import math
'''
    The following is taken from the Python Cookbook,
    by Alex Martelli, David Ascher

    http://books.google.com/books?id=yhfdQgq8JF4C
'''


def int_to_roman(input):
    '''
       given an integer, input, that is greater than 0 and less than, 4000
       return its modern roman numeral represenation
    '''

    if not 0 < input < 4000:
        raise ValueError("input must be between 1 and 3999")

    # two dimensions allow for faster lookups in starting conversion.
    ints_to_romans = [[(9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')],
                      [(90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X')],
                      [(900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C')],
                      [(1000, 'M')]]

    result = []

    # determines where to start.
    index_lookup = int(math.log10(input))

    while input != 0:
        for digit, roman in ints_to_romans[index_lookup]:
            count = input / digit
            result.append(roman * count)
            input -= digit * count
        index_lookup -= 1

    return ''.join(result)


def roman_to_int(input):
    '''
        Given a string that represents a roman numeral, then,
        return its integer value
    '''

    input = input.upper()
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sum = 0
    for i in range(len(input)):
        try:
            value = nums[input[i]]

            # If the next place holds a larger number, this value is negative.
            if i + 1 < len(input) and nums[input[i + 1]] > value:
                sum -= value
            else:
                sum += value
        except KeyError:
            raise ValueError('input is not a valid Roman numeral: %s' % input)

    return sum
