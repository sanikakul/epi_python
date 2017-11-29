"""
The parity of a binary word is one if the number of 1s in the word is odd; otherwise it is 0. For example the parity of
1011 is 1 and the parity of 10001000 is 0. Determine parity parity of large 64-bit word.
"""
import unittest


def compute_word_parity_one(n):
    """
    Brute force solution iteratively tests the value of each bit while keeping track of the number of 1s seen so far.
    """
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
    parity = 0
    while n:
        parity ^= 1
        n &= n - 1
    return parity


def compute_word_parity_three(n):
    """
    Caching 16 bit parities in dictionary. Complexity is O(n/L) where n is size of word and L is size of cache
    """
    PRECOMPILED_PARITY = {}
    i = 0
    while i < pow(2, 16):
        PRECOMPILED_PARITY[i] = compute_word_parity_two(i)
        i += 1
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    parity = PRECOMPILED_PARITY[n >> (3 * MASK_SIZE)] ^ PRECOMPILED_PARITY[(n >> (2 * MASK_SIZE)) & BIT_MASK] ^ \
             PRECOMPILED_PARITY[(n >> MASK_SIZE) & BIT_MASK] ^ PRECOMPILED_PARITY[n & BIT_MASK]
    return parity


def compute_word_parity_four(n):
    """
    This method XORs the last half of the word with the first half and returns the final bit.
    """
    n ^= n >> 32
    n ^= n >> 16
    n ^= n >> 8
    n ^= n >> 4
    n ^= n >> 2
    n ^= n >> 1
    return n & 0x1


class ParityOfWordTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(compute_word_parity_one(1234), 1)
        self.assertEqual(compute_word_parity_two(1234), 1)
        self.assertEqual(compute_word_parity_three(1234), 1)
        self.assertEqual(compute_word_parity_four(1234), 1)

    def test_two(self):
        self.assertEqual(compute_word_parity_one(123), 0)
        self.assertEqual(compute_word_parity_two(123), 0)
        self.assertEqual(compute_word_parity_three(123), 0)
        self.assertEqual(compute_word_parity_four(123), 0)

    def test_three(self):
        self.assertEqual(compute_word_parity_one(0), 0)
        self.assertEqual(compute_word_parity_two(0), 0)
        self.assertEqual(compute_word_parity_three(0), 0)
        self.assertEqual(compute_word_parity_four(0), 0)

    def test_four(self):
        self.assertEqual(compute_word_parity_one(9223372036854775807), 1)
        self.assertEqual(compute_word_parity_two(9223372036854775807), 1)
        self.assertEqual(compute_word_parity_three(9223372036854775807), 1)
        self.assertEqual(compute_word_parity_four(9223372036854775807), 1)


if __name__ == "__main__":
    unittest.main()
