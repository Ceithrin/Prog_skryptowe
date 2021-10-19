import books
import unittest
import argparse
import sys


class Test_TestSum(unittest.TestCase):
    def test_warning(self):
        with unittest.mock.patch(sys.argv, ["books.py", "Ksiazka:3", "Ksiazka2:4"]):
            for arg in books:
                print(arg, books[arg])
            self.assertWarns(UserWarning)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='Ksiazka:2')
    parser.add_argument('unittest_args', nargs='*')

    args = parser.parse_args()

    sys.argv[1:] = args.unittest_args
    unittest.main()