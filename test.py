#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from ts import is_even

class TestEven(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to check if given input is even
        """
        data = 23
        result = is_even(data)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()