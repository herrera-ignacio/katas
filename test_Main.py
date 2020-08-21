from unittest import TestCase
from Main import FizzBuzz


class TestFizzBuzz(TestCase):
    def calculate_when_input_return_expected(self, input, expected):

        fizzbuzz = FizzBuzz()
        output = fizzbuzz.calculate(input)

        self.assertEqual(output, expected, 'When given {}, returns {}'.format(input, expected))
        self.assertTrue(type(output), 'string')

    def test_calculate_when_1_return_1(self):
        self.calculate_when_input_return_expected(1, '1')

    def test_calculate_when_2_return_2(self):
        self.calculate_when_input_return_expected(2, '2')

    def test_calculate_when_3_return_fizz(self):
        self.calculate_when_input_return_expected(3, 'Fizz')

    def test_calculate_when_9_return_fizz(self):
        self.calculate_when_input_return_expected(9, 'Fizz')

    def test_calculate_when_5_return_buzz(self):
        self.calculate_when_input_return_expected(5, 'Buzz')

    def test_calculate_when_10_return_buzz(self):
        self.calculate_when_input_return_expected(10, 'Buzz')

    def test_calculate_when_15_return_fizzbuzz(self):
        self.calculate_when_input_return_expected(15, 'FizzBuzz')

    def test_calculate_multiples_of_three_returns_fizz_or_fizzbuzz(self):
        values = range(3, 16, 3)
        for digit in values:
            if digit % 5 == 0:
                self.calculate_when_input_return_expected(digit, 'FizzBuzz')
            else:
                self.calculate_when_input_return_expected(digit, 'Fizz')

    def test_calculate_multiples_of_five_returns_buzz(self):
        values = range(5, 16, 5)
        for digit in values:
            if digit % 3 == 0:
                self.calculate_when_input_return_expected(digit, 'FizzBuzz')
            else:
                self.calculate_when_input_return_expected(digit, 'Buzz')

    def test_calculate_non_multiples_of_three_or_five_returns_number_as_string(self):
        values = range(0, 16)
        for digit in values:
            if digit % 3 == 0 or digit % 5 == 0:
                continue

            self.calculate_when_input_return_expected(digit, str(digit))
