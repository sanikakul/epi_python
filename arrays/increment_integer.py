"""
Increment a number - stored as digits in an array - by one

Eg: input: [1, 2, 9]
    output = [1, 3, 0]
"""
import unittest


def increment_integer_one(input_array):
    """
    This function adds one directly to the last element of the array and keeps a track of
    """
    output = []
    carry = 1
    i = len(input_array) - 1
    while i >= 0 and carry > 0:
        num = input_array[i] + carry
        if num > 9:
            input_array[i] = num % 10
            carry = num / 10
        else:
            input_array[i] = num
            carry = 0
        i -= 1
    if carry > 0:
        output.append(carry)
        output.extend(input_array)
        return output
    else:
        return input_array


class IncrementInteger(unittest.TestCase):
    def test_one(self):
        self.assertEqual(increment_integer_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 1])

    def test_two(self):
        self.assertEqual(increment_integer_one([0]), [1])

    def test_three(self):
        self.assertEqual(increment_integer_one([9, 9, 9, 9]), [1, 0, 0, 0, 0])

    def test_four(self):
        self.assertEqual(increment_integer_one([2, 4, 6, 8]), [2, 4, 6, 9])


if __name__ == "__main__":
    unittest.main()
