from Week_5_Function import add_num
import unittest


class TestFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add_num(3, 2)
        self.assertEqual(result, 5)

    def test_add_positive_and_negative_numbers(self):
        result = add_num(4, -2) 
        self.assertEqual(result, 2)

    def test_add_decimal_numbers(self):
        result = add_num(3.2, 2.2)
        self.assertAlmostEqual(result, 1.4, 0.3)


if __name__ == '__main__':
    unittest.main()
