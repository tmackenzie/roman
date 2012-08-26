import unittest
from roman.convert import roman_to_int


class TestRomanToInt(unittest.TestCase):
    '''
        tests for converting a Roman numeral to an Integer
    '''

    def test_raise_negative_input(self):
        ''' expected to raise a ValueError if the input is <= 0 '''
        self.assertRaises(ValueError, roman_to_int, "nulla")

    def test_raise_large_input(self):
        ''' expected to raise a Value Error if the input is > 3999 '''
        self.assertRaises(ValueError, roman_to_int, "MMMM")

    def test_raise_jiberish(self):
        ''' expected to raise a ValueError when invalid input '''
        self.assertRaises(ValueError, roman_to_int, "blah balha 98988")

    def test_convert_I(self):
        number = roman_to_int("I")
        self.assertEqual(number, 1)

    def test_convert_IV(self):
        number = roman_to_int("IV")
        self.assertEqual(number, 4)

    def test_convert_V(self):
        number = roman_to_int("V")
        self.assertEqual(number, 5)

    def test_convert_IX(self):
        number = roman_to_int("IX")
        self.assertEqual(number, 9)

    def test_convert_X(self):
        number = roman_to_int("X")
        self.assertEqual(number, 10)

    def test_convert_XL(self):
        number = roman_to_int("XL")
        self.assertEqual(number, 40)

    def test_convert_L(self):
        number = roman_to_int("L")
        self.assertEqual(number, 50)

    def test_convert_XC(self):
        number = roman_to_int("XC")
        self.assertEqual(number, 90)

    def test_convert_C(self):
        number = roman_to_int("C")
        self.assertEqual(number, 100)

    def test_convert_CD(self):
        number = roman_to_int("CD")
        self.assertEqual(number, 400)

    def test_convert_D(self):
        number = roman_to_int("D")
        self.assertEqual(number, 500)

    def test_convert_CM(self):
        number = roman_to_int("CM")
        self.assertEqual(number, 900)

    def test_convert_M(self):
        number = roman_to_int("M")
        self.assertEqual(number, 1000)

    def test_convert_MI(self):
        number = roman_to_int("MI")
        self.assertEqual(number, 1001)

    def test_convert_MMMCMXCIX(self):
        number = roman_to_int("MMMCMXCIX")
        self.assertEqual(number, 3999)

    def test_convert_MCMXLIV(self):
        # got this one from wiki. should be able subtract larger ones..
        number = roman_to_int("MCMXLIV")
        self.assertEqual(number, 1944)

if __name__ == "__main__":
    unittest.main()
