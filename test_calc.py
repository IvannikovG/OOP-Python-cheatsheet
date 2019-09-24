import unittest
import calc
# to run this cmd+b is not enough.
# run in from the directory file is located by:
# python -m unittest test_calc.py
# we inherit here from st.lib


class TestCalc(unittest.TestCase):
    # method names HAVE TO start with test
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_substact(self):
        self.assertEqual(calc.substract(10, 5), 5)
        self.assertEqual(calc.substract(-1, 1), -2)
        self.assertEqual(calc.substract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        # this string tests if the function raises a ValueError
        self.assertRaises(ValueError, calc.divide, 10, 0)
        # assertRaises(<expected type of error>, <function>, *<args>)

        # we can use context manager to do the same
        with self.assertRaises(ValueError):
            calc.divide(10, 0)



# now it is possible to run it directly
# also from the terminal
if __name__ == '__main__':
    unittest.main()
