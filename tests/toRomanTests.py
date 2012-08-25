import unittest
from roman.calculator import int_to_roman

class IntToRomanTests(unittest.TestCase):
    '''
        tests for converting a integer to a roman numeral
    '''

    def test_negative_input(self):
        ''' expected to raise a ValueError if the input is <= 0 '''
        self.assertRaises(ValueError, int_to_roman, 0)

    def test_large_input(self):
        ''' expected to raise a Value Error if the input is > 3999 '''
        self.assertRaises(ValueError, int_to_roman, 4000)

if __name__ == "__main__":
    unittest.main()
