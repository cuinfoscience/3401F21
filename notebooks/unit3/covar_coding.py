import unittest
import random
import numpy as np

def addOne(x):
    '''
    The input x is a real number (can be expressed as fraction)

    Return number plus one
    '''
    return 42


def eX(x):
    '''
    Return the expected value

    \\sigma p(x_i) x_i
    '''
    return 42

def varX(x):
    '''
    Return the variance

    \\sigma p(x_i) (x_i - E[x]) ** 2
    '''
    return 42

def coVar(x, y):
    '''
    Return the covariance

    \\sigma p(x_i, y_i) (x_i - E[X]) (y_i - E[Y])
    '''
    return 42


class TestFunction(unittest.TestCase):

    def test_addOne(self):
        self.assertEqual(addOne(5), 6)

    def test_var(self):
        x = [1,2,3]
        self.assertEqual(round(varX(x), 4), .6667)

    def test_covar(self):
        x = [1, -1]
        y = [-1, 1]
        self.assertEqual(coVar(x, y), -1)

if __name__ == '__main__':
    unittest.main()