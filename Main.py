class FizzBuzz:
    @staticmethod
    def is_multiple_of(digit, base):
        return digit % base == 0

    def calculate(self, value):
        # 3 if-s
        # if self.is_multiple_of(value, 3) and self.is_multiple_of(value, 5):
        #     return 'FizzBuzz'
        # elif self.is_multiple_of(value, 3):
        #     return 'Fizz'
        # elif self.is_multiple_of(value, 5):
        #     return 'Buzz'

        # 2 consecutive if-s, 1 nested
        if self.is_multiple_of(value, 3):
            if self.is_multiple_of(value, 5):
                return 'FizzBuzz'
            return 'Fizz'
        elif self.is_multiple_of(value, 5):
            return 'Buzz'

        return str(value)
