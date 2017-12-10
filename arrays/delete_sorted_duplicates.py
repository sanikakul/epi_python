"""
Delete duplicates from a sorted array

Eg: input: [2, 3, 5, 5, 7, 11, 11, 11, 13]
    output: [2, 3, 5, 7, 11, 13, 0, 0, 0]

"""
import unittest


def delete_sorted_duplicates_one(input_array):
    """
    This function removes duplicate elements by creating a new array and appending
    unique values into it.

    time complexity id O(n), space complexity in the worst case is O(n)

    """
    output = []
    current = False
    for el in input_array:
        if not current or el != current:
            current = el
            output.append(el)
    diff = len(input_array) - len(output)
    i = 0
    while i < diff:
        output.append(0)
        i += 1
    return output


def delete_sorted_duplicates_two(input_array):
    """
    This function swaps ints and moves the duplicates to the end of the array instead
    of creating a new array altogether

    Time complexity id O(n), space complexity is O(1)
    """
    i, j = 0, 0
    current = False
    while i < len(input_array):
        if not current:
            current = input_array[i]
            i += 1
            j += 1
        elif input_array[i] == current:
            i += 1
        else:
            current = input_array[i]
            if i > j:
                input_array[i], input_array[j] = input_array[j], input_array[i]
            i += 1
            j += 1
    while j < len(input_array):
        input_array[j] = 0
        j += 1
    return input_array


class DeleteSortedDuplicates(unittest.TestCase):

    def test_one(self):
        self.assertEqual(delete_sorted_duplicates_one([2, 3, 5, 5, 7, 11, 11, 11, 13]), [2, 3, 5, 7, 11, 13, 0, 0, 0])
        self.assertEqual(delete_sorted_duplicates_two([2, 3, 5, 5, 7, 11, 11, 11, 13]), [2, 3, 5, 7, 11, 13, 0, 0, 0])

    def test_two(self):
        self.assertEqual(delete_sorted_duplicates_one([]), [])
        self.assertEqual(delete_sorted_duplicates_two([]), [])

    def test_three(self):
        self.assertEqual(delete_sorted_duplicates_one([9, 9, 9, 9]), [9, 0, 0, 0])
        self.assertEqual(delete_sorted_duplicates_two([9, 9, 9, 9]), [9, 0, 0, 0])

    def test_four(self):
        self.assertEqual(delete_sorted_duplicates_one([2, 4, 6, 8]), [2, 4, 6, 8])
        self.assertEqual(delete_sorted_duplicates_two([2, 4, 6, 8]), [2, 4, 6, 8])


if __name__ == "__main__":
    unittest.main()
