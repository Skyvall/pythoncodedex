import unittest

from string_utils import reverse_string, capitalize_string, is_capitalized


class MyTestCase(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")
        self.assertEqual(capitalize_string("python"), "Python")

    def test_is_capitalized(self):
        self.assertTrue(is_capitalized("Hello"))
        self.assertFalse(is_capitalized("hello"))
        
if __name__ == "__main__":
    unittest.main()