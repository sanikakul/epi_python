"""
The parity of a binary word is one if the number of 1s in the word is odd; otherwise it is 0. For example the parity of
1011 is 1 and the parity of 10001000 is 0. Determine parity parity of large 64-bit word.
"""
import unittest


def compute_word_parity_one(n):
    """
    Brute force solution iteratively tests the value of each bit while keeping track of the number of 1s seen so far.
    """
    n = abs(n)
    parity = 0
    while n:
        parity ^= n & 1
        n >>= 1
    return parity


def compute_word_parity_two(n):
    """
    Erases the lowest bit set in a word in a single operation thereby improving performance in the best and average
    cases
    """
    n = abs(n)
    parity = 0
    while n:
        parity ^= 1
        n &= n - 1
    return parity


class ParityOfWordTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(compute_word_parity_one(1234), 1)
        self.assertEqual(compute_word_parity_two(1234), 1)

    def test_two(self):
        self.assertEqual(compute_word_parity_one(123), 0)
        self.assertEqual(compute_word_parity_two(123), 0)

    def test_three(self):
        self.assertEqual(compute_word_parity_one(0), 0)
        self.assertEqual(compute_word_parity_two(0), 0)

    def test_four(self):
        self.assertEqual(compute_word_parity_one(9223372036854775807), 1)
        self.assertEqual(compute_word_parity_two(9223372036854775807), 1)

    def test_five(self):
        self.assertEqual(compute_word_parity_one(-123), 0)
        self.assertEqual(compute_word_parity_two(-123), 0)

    def test_six(self):
        self.assertEqual(compute_word_parity_one(-4), 1)
        self.assertEqual(compute_word_parity_two(-4), 1)

if __name__ == "__main__":
    unittest.main()
