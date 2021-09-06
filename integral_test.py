import unittest
from integral import integrate  # the function to test

class IntegralTest(unittest.TestCase):
    """Tests of the integrate function."""

    #TODO Write 2 more tests.
    # 1. test using a quadratic function a*x^2 + b*x + c
    # 2. test using sin function, integrate from 0 to pi

    def test_constant(self):
        """integral of a constant function"""
        c = 2.5
        def fun(x):
            return c
        # integral from 1 to 5 returns exact result
        self.assertEqual(4*c, integrate(fun, 1, 5))
        # using multiple subintervals
        self.assertEqual(4*c, integrate(fun, 1, 5), 10)
        # test using a negative value and non-integer endpoints
        c = -4
        self.assertEqual(2*c, integrate(fun, -0.5, 1.5))
        # integral over an empty interval is always 0
        self.assertEqual(0, integrate(fun, 2, 2))