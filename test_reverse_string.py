import unittest

from reverse_string import reverse_string


class ReverseStringTest(unittest.TestCase):
    def test_word(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_sentence(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_empty(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_char(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome(self):
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_unicode(self):
        self.assertEqual(reverse_string("héllo"), "olléh")


if __name__ == "__main__":
    unittest.main()
