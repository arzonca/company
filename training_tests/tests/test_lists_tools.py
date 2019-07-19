import unittest
#from unittest import TestCase
from training_tests.lists_tools import filter_even_numbers


class TestListTools(unittest.TestCase):
    def test_filter_even_numbers(self):
        result = filter_even_numbers([1, 2, 3, 4])
        expected_result = [2, 4]
        self.assertEqual(result, expected_result)    #test przechodzi OK

        self.assertEqual([2, 1], filter_even_numbers([1, 2, 3, 4]))  # test nie przechodzi

if __name__ == '__main__':
    unittest.main()