#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from ts import is_even

class TestEven(unittest.TestCase):
    def test_1(self):
        """
        Test case to check if given input is even
        """
        data = 23
        result = is_even(data)
        self.assertEqual(result, True)
    def test_2(self):
        """
        Test case to check if given input is even
        """
        data = 76
        result = is_even(data)
        self.assertEqual(result, True)
    def test_3(self):
        """
        Test case to check if given input is even
        """
        data = 1257
        result = is_even(data)
        self.assertEqual(result, False)
    def test_4(self):
        """
        Test case to check if given input is even
        """
        data = 43
        result = is_even(data)
        self.assertEqual(result, False)
    def test_5(self):
        """
        Test case to check if given input is even
        """
        data = 392
        result = is_even(data)
        self.assertEqual(result, True)



if __name__ == '__main__':
    unittest.main()
