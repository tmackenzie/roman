
def int_to_roman(input):
    ''' 
       given and integer, input, that is greater than 0 and less than, 4000
       return its modern roman numeral represenation

    '''

    if not 0 < input < 4000:
       raise ValueError, "input must be between 1 and 3999"   

    romans = [ 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    result = []

    for i in range(len(romans)):
        int_index = input / ints[i]
        result.append(romans[i] * int_index)
        input -= ints[i] * int_index

    return ''.join(result)

    
