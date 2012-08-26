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

       worst case:
       O(N), input = value for every significant digit. example, 1111
       
       cost +
       13 * (1 comparator + 2 assignments + 1 read + 3 operations + 1 method call)

       best case O(?), input = 1000

    '''
    if not 0 < input < 4000: # 2 comparators
        raise ValueError("input must be between 1 and 3999")

    romans = [
        ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'], # ones
        ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'], # tens
        ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'], # hundreds,
        ['M', 'MM', 'MMM']] # thosands

    ints = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9], # ones
        [10, 20, 30, 40, 50, 60, 70, 80, 90], # tens
        [100, 200, 300, 400, 500, 600, 700, 800, 900], # hundreds,
        [1000, 2000, 3000] ] # thousands

    result = []


    while input !=  0:
        input_length = int(math.log10(input))
        factor = 10 ** (input_length) 
        count = (input / factor) - 1
        input -= ints[input_length][count]
        result.append(romans[input_length][count])

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
