import math
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

    romans = [
        ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],  # ones
        ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],  # tens
        ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],  # hundreds,
        ['M', 'MM', 'MMM']]  # thosands

    ints = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],  # ones
        [10, 20, 30, 40, 50, 60, 70, 80, 90],  # tens
        [100, 200, 300, 400, 500, 600, 700, 800, 900],  # hundreds,
        [1000, 2000, 3000]]  # thousands

    result = []

    """
        significant, is the significant digit of input..
        used to lookup proper inner list in the ints, roman lists.
            0 = ones.
            1 = tens.
            2 = hundreds
            3 = thousands.

        factor, is the whole number for the current significant digit.
            example, input = 101
            - factor will be 100.

        count, is the index mapping to the inner lookup lists.

    """

    while input != 0:
        significant = int(math.log10(input))
        factor = 10 ** (significant)
        count = (input / factor) - 1
        input -= ints[significant][count]
        result.append(romans[significant][count])

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
