import books
import unittest
import argparse
import sys


class Test_TestSum(unittest.TestCase):
    def test_dictionary(self):
        self.assertEqual(books.dictionary(["Ksiazka:3", "Ksiazka2:4"]), {"Ksiazka": 3, "Ksiazka2": 4})
    
    def test_rent_warning(self):
        self.assertEqual(books.Wypozyczenie(["Adam", "Ksiazka", "W"], {"Adam": ["Ksiazka", "Ksiazka2"]}, {"Ksiazka": 0, "Ksiazka2": 3}), None)

    def test_dictionary_error(self):
        with self.assertRaises(Exception):
            books.dictionary(["Ksiazka:XD", "Ksiazka2:4"])
    
    def test_book_return(self):
        self.assertEqual(books.Zwrot(["Adam", "Ksiazka", "Z"], {"Adam": ["Ksiazka2"]}, {"Ksiazka": 0, "Ksiazka2": 3}), None)

if __name__ == '__main__':
    unittest.main()