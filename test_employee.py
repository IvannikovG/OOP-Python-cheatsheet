import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    # these methods will help to stop repeating the code
    @classmethod
    def setUp(self):
        print('setUp')
        # runs its code before every single test
        self.emp_1 = Employee('Georgii', 'Ivannikov', 50000)
        self.emp_2 = Employee('Sange', 'Andyasha', 60000)

    @classmethod
    def tearDown(self):
        # runs its code after every single test
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Georgii.Ivannikov@gmail.com')
        self.assertEqual(self.emp_2.email, 'Sange.Andyasha@gmail.com')

        self.emp_1.first = 'John'
        self.emp_1.last = 'Snow'
        self.emp_2.first = 'Sansa'
        self.emp_2.last = 'Stark'

        self.assertEqual(self.emp_1.email, 'John.Snow@gmail.com')
        self.assertEqual(self.emp_2.email, 'Sansa.Stark@gmail.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Georgii Ivannikov')
        self.assertEqual(self.emp_2.fullname, 'Sange Andyasha')

        self.emp_1.first = 'Leo'
        self.emp_2.last = 'Pan'

        self.assertEqual(self.emp_1.fullname, 'Leo Ivannikov')
        self.assertEqual(self.emp_2.fullname, 'Sange Pan')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
