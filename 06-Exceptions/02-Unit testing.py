# UNIT TESTING
print('''UNIT TESTING''')

print('''unittest lets us write your own test programs''')

import unittest
import string


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = string.capwords(text.capitalize())
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = string.capwords(text.capitalize())
        self.assertEqual(result, 'Monty Python')

    def test_with_apostrophes(self):
        text = "monty python's flying circus"
        result = string.capwords(text.capitalize())
        self.assertEqual(result, "Monty Python's Flying Circus")


if __name__ == '__main__':
    unittest.main()
