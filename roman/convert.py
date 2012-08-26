import math
import re
"""
    @author: tmackenzie

"""


def int_to_roman(input):
    """
       given an integer, input, that is greater than 0 and less than, 4000
       return its modern roman numeral represenation

    """

    if not 0 < input < 4000:  # 2 comparators
        raise ValueError("input must be between 1 and 3999")

    # these could of just been lists, for speed purposes they are dicts.
    int_to_roman = {
        1: {1: (1, 'I'),
            2: (2, 'II'),
            3: (3, 'III'),
            4: (4, 'IV'),
            5: (5, 'V'),
            6: (6, 'VI'),
            7: (7, 'VII'),
            8: (8, 'VIII'),
            9: (9, 'IX')},
        2: {1: (10, 'X'),
            2: (20, 'XX'),
            3: (30, 'XXX'),
            4: (40, 'XL'),
            5: (50, 'L'),
            6: (60, 'LX'),
            7: (70, 'LXX'),
            8: (80, 'LXXX'),
            9: (90, 'XC')},
        3: {1: (100, 'C'),
            2: (200, 'CC'),
            3: (300, 'CCC'),
            4: (400, 'CD'),
            5: (500, 'D'),
            6: (600, 'DC'),
            7: (700, 'DCC'),
            8: (800, 'DCCC'),
            9: (900, 'CM')},
        4: {1: (1000, 'M'),
            2: (2000, 'MM'),
            3: (3000, 'MMM')}}

    result = []

    """
        significant, is the significant digit of input..
        used to lookup dict.
            1 = ones.
            2 = tens.
            3 = hundreds
            4 = thousands.

        factor, is the whole number for the current significant digit.
        used to calculate, count.
            example, input = 101
            - factor = 100.

        count, the number of times input is divisible by factor.
        used to lookup the arabic, romans tuple.
            example, input = 101, factor = 100
            - count = 1

    """

    while input != 0:

        significant = int(math.log10(input)) + 1
        factor = 10 ** (significant - 1)
        count = (input / factor)

        # acquire the arabic and roman values
        number, roman = int_to_roman[significant][count]
        result.append(roman)

        # this could just be, count * factor, its not b/c of speed.
        input -= number

    return ''.join(result)


def roman_to_int(input):
    '''
        Given a string that represents a roman numeral, then,
        return its integer value

        O(N) - iterates through all characters in the array.
    '''

    input = input.upper()

    # regular expression to parse and validate the input string.
    roman_group_re = re.compile('^([M]{0,3})([DCM]*)([XLC]*)([IVX]*)')

    # parse input..
    thousands, hundreds, tens, ones = roman_group_re.match(input).groups()

    # should be pretty simple, all I need is a dict to match the vars to their ints.

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
