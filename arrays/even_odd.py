"""
Given an array of integers, re-arrange the elements in such a way that even numbers should be before odd numbers.

Eg: input: [1, 2, 3, 4, 5, 6, 7, 8]
    output: [2, 4, 6, 8, 1, 3, 5, 7]

"""
import unittest


def even_odd_one(input_array):
    """
    This function uses additional space. input_array is split
    into even_array and odd_array and then those two array
    are combined and returned.

    Time complexity is O(n), space complexity is O(n)

    :param input_array: array of integers

    """
    even_array = []
    odd_array = []
    for el in input_array:
        if el % 2 == 0:
            even_array.append(el)
        else:
            odd_array.append(el)
    even_array.extend(odd_array)
    return even_array


def even_odd_two(input_array):
    """
    This function swaps values in place in an array

    Time complexity is O(n), space complexity is O(1)

    """
    even_index = 0
    odd_index = len(input_array) - 1
    unclassified_index = 0

    while unclassified_index <= odd_index:
        if input_array[unclassified_index] % 2 == 0:
            if even_index < unclassified_index:
                input_array[even_index], input_array[unclassified_index] = \
                    input_array[unclassified_index], input_array[even_index]
            even_index += 1
            unclassified_index += 1
        else:
            while input_array[odd_index] % 2 == 1 and odd_index >= unclassified_index:
                odd_index -= 1
            if unclassified_index < odd_index:
                input_array[unclassified_index], input_array[odd_index] = \
                    input_array[odd_index], input_array[unclassified_index]
            else:
                unclassified_index += unclassified_index
    return input_array


class EvenOdd(unittest.TestCase):
    def test_one(self):
        self.assertEqual(even_odd_one([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), [2, 4, 6, 8, 0, 1, 3, 5, 7, 9])
        self.assertEqual(even_odd_two([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), [0, 2, 8, 4, 6, 5, 7, 3, 9, 1])

    def test_two(self):
        self.assertEqual(even_odd_one([]), [])
        self.assertEqual(even_odd_two([]), [])

    def test_three(self):
        self.assertEqual(even_odd_one([1, 3, 5, 7]), [1, 3, 5, 7])
        self.assertEqual(even_odd_two([1, 3, 5, 7]), [1, 3, 5, 7])

    def test_four(self):
        self.assertEqual(even_odd_one([2, 4, 6, 8]), [2, 4, 6, 8])
        self.assertEqual(even_odd_two([2, 4, 6, 8]), [2, 4, 6, 8])


if __name__ == "__main__":
    unittest.main()
