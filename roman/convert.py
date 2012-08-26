'''
    The following is taken from the Python Cookbook, by Alex Martelli, David Ascher
    http://books.google.com/books?id=yhfdQgq8JF4C

'''


def int_to_roman(input):
    ''' 
       given and integer, input, that is greater than 0 and less than, 4000
       return its modern roman numeral represenation

       worst/best case.
       O(1) - b/c no matter what the input is, 
        - it will always execute the same methods, comparators and assignments.   

       performs:
        - 2 method calls.
        - 2 comparators.

       performs 13 times..
        - 3 operations.
        - 3 reads
        - 2 writes
    '''

    if not 0 < input < 4000:
       raise ValueError, "input must be between 1 and 3999"   

    romans = ( 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

    result = []

    for i in range(len(romans)):
        count = input / ints[i]
        result.append(romans[i] * count)
        input -= ints[i] * count 

    return ''.join(result)

def roman_to_int(input):
    ''' 
        Given a string that represents a roman numeral, return its integer value
    '''
    
    input = input.upper()
    nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    sum = 0
    for i in range(len(input)):
        try:
            value = nums[input[i]]

            # If the next place holds a larger number, this value is negative.            
            if i+1 < len(input) and nums[input[i+1]] > value:
                sum -= value
            else:
                sum += value
        except KeyError:
            raise ValueError, 'input is not a valid Roman numeral: %s' % input

    return sum 
