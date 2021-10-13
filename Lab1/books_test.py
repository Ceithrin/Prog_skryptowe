import books
import unittest


class Test_TestSum(unittest.TestCase):
    def test_list_int_int(self):
        self.assertEqual(books.list({1: 2}), "1 2")

    # def test_sum_integer_float(self):
    #     self.assertEqual(main.sum(2, 1.5), 3.5)

    # def test_sum_integer_string(self):
    #    self.assertEqual(main.sum(2, '2'), 4)

    # def test_sum_string_string(self):
    #     self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    # def test_sum_integer_wrong_number_in_string(self):
    #     self.assertRaises(TypeError,main.sum(2, 'Ala ma kota123'))

    # def test_sum_integer_list(self):
    #     self.assertRaises(TypeError,main. sum(1, [2, 3]))


if __name__ == '__main__':
    unittest.main()