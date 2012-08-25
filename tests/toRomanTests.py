import unittest
from roman.convert import int_to_roman

class IntToRomanTests(unittest.TestCase):
    '''
        tests for converting a integer to a roman numeral

        - test scenarios
            - too low <= 0
            - too high > 3999
    '''

    def test_raise_negative_input(self):
        ''' expected to raise a ValueError if the input is <= 0 '''
        self.assertRaises(ValueError, int_to_roman, 0)

    def test_raise_large_input(self):
        ''' expected to raise a Value Error if the input is > 3999 '''
        self.assertRaises(ValueError, int_to_roman, 4000)

    def test_convert_1(self):
        roman = int_to_roman(1)
        self.assertEqual(roman, "I")

    def test_convert_4(self):
        roman = int_to_roman(4)
        self.assertEqual(roman,"IV")

    def test_convert_5(self):
        roman = int_to_roman(5)
        self.assertEqual(roman,"V")

    def test_convert_9(self):
        roman = int_to_roman(9)
        self.assertEqual(roman,"IX")

    def test_convert_10(self):
        roman = int_to_roman(10)
        self.assertEqual(roman,"X")

    def test_convert_40(self):
        roman = int_to_roman(40)
        self.assertEqual(roman,"XL")

    def test_convert_50(self):
        roman = int_to_roman(50)
        self.assertEqual(roman,"L")

    def test_convert_90(self):
        roman = int_to_roman(90)
        self.assertEqual(roman,"XC")

    def test_convert_100(self):
        roman = int_to_roman(100)
        self.assertEqual(roman,"C")

    def test_convert_400(self):
        roman = int_to_roman(400)
        self.assertEqual(roman,"CD")

    def test_convert_500(self):
        roman = int_to_roman(500)
        self.assertEqual(roman,"D")

    def test_convert_900(self):
        roman = int_to_roman(900)
        self.assertEqual(roman,"CM")

    def test_convert_1000(self):
        roman = int_to_roman(1000)
        self.assertEqual(roman,"M")

    def test_convert_3999(self):
        roman = int_to_roman(3999)
        self.assertEqual(roman, "MMMCMXCIX")

if __name__ == "__main__":
    unittest.main()
