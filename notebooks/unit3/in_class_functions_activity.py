import unittest
import random

def addOne(x):
    '''
    The input x is a real number (can be expressed as fraction)

    Return number plus one
    '''
    return 42


class TestFunction(unittest.TestCase):

    def test_addOne(self):
        self.assertEqual(addOne(5), 6)


if __name__ == '__main__':
    unittest.main()