import skrypt
import unittest

class Test_RegexMatch(unittest.TestCase):
    def test_word_match(self):
        self.assertEqual(skrypt.word_match("56kotów")[1], "kotów")

    def test_word_index(self):
        self.assertEqual(skrypt.word_match("56kotów")[0], 2)

    def test_word_index2(self):
        self.assertEqual(skrypt.word_match("2391psów")[0], 4)

    def test_word_none(self):
        self.assertEqual(skrypt.word_match("12345"), None)

    def test_word_number(self):
        self.assertEqual(skrypt.word_match("Ala1")[1], 'Ala')

    def test_word_index0(self):
        self.assertEqual(skrypt.word_match("Kot")[0], 0)

    def test_number_match(self):
        self.assertEqual(skrypt.number_match("56kotów")[1], "56")

    def test_number_index(self):
        self.assertEqual(skrypt.number_match("kotów56")[0], 5)

    def test_number_index0(self):
        self.assertEqual(skrypt.number_match("2391psów")[0], 0)

    def test_number_none(self):
        self.assertEqual(skrypt.number_match("Psy"), None)

    def test_number_word(self):
        self.assertEqual(skrypt.number_match("Ala1")[1], '1')


if __name__ == '__main__':
    unittest.main()