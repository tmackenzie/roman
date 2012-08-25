import math

def int_to_roman(input):
    ''' 
       given and integer, input, that is greater than 0 and less than, 4000
       return its modern roman numeral represenation

    '''

    if not 0 < input < 4000:
       raise ValueError, "input must be between 1 and 3999"   

    ints_to_romans = [[ (9,'IX'), (5,'V'), (4, 'IV'), (1,'I')],
                      [ (90, 'XC'), (50, 'L'), (40,'XL'), (10,'X')],
                      [ (900, 'CM'), (500,'D'),(400,'CD'),( 100,'C')],
                      [ (1000, 'M')]]

    result = []

    index_lookup = int(math.log10(input))
    while input != 0:
        for digit, roman in ints_to_romans[index_lookup]:
            int_index = input / digit
            result.append(roman * int_index)
            input -= digit * int_index

        index_lookup-=1

    return ''.join(result)

    
