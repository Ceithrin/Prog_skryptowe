import main
import unittest
from fractions import Fraction


class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
       self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_fraction_fraction(self):
        self.assertEqual(main.sum(Fraction(1, 3), Fraction(1, 9)), Fraction(4, 9))

    def test_sum_complex_complex(self):
        self.assertEqual(main.sum(complex(8, 3), complex(1, 4)), complex(9, 7))

    # def test_sum_integer_wrong_number_in_string(self):
    #     self.assertEqual(main.sum(2, 'Ala ma kota123'), 2)

    def test_sum_text_integer(self):
        with self.assertRaises(ValueError):
            main.sum(2, 'Ala ma kota123')

    def test_sum_integer_bad_type(self):
        with self.assertRaises(TypeError):
            main.sum(1, [2, 3])
            


if __name__ == '__main__':
    unittest.main()