import unittest
from area import area
from Salary import expenses
from Salary import savings


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = 2
        result = area(data)
        self.assertEqual(result, 4)

    def test_mortgage(self):
        salary = 1000000
        percent_mortgage = 30
        percent_life = 50
        result = expenses(salary, percent_mortgage, percent_life)
        self.assertEqual(result, 3600000.0)

    def test_savings(self):
        salary = 1000000
        percent_mortgage = 30
        percent_life = 50
        result = savings(salary, percent_mortgage, percent_life)
        self.assertEqual(result, 2400000.0)

if __name__ == '__main__':
    unittest.main()


