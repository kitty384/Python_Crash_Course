import unittest
from employee import Employee


class EmployTest(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('li', 'si', 10000)
        self.original_salary = self.employee.salary

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.original_salary+5000, self.employee.salary)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.original_salary+10000, self.employee.salary)


unittest.main()
