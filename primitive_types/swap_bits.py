"""
Swap the ith and jth bits of a given number

Eg: x = 10110010
    i = 2
    j = 5

    output = 10010110

"""
import unittest


def swap_bits_one(x, i, j):
    ith_index = (x >> i) & 1
    jth_index = (x >> j) & 1

    if ith_index == 1:
        x |= ith_index << j
    else:
        x &= ~(1 << j)
    if jth_index == 1:
        x |= jth_index << i
    else:
        x &= ~(1 << i)

    return x


def swap_bits_two(x, i, j):
    ith_index = (x >> i) & 1
    jth_index = (x >> j) & 1

    if ith_index != jth_index:
        if ith_index == 1:
            x |= ith_index << j
            x &= ~(1 << i)
        else:
            x |= jth_index << i
            x &= ~(1 << j)
    return x


class SwapBits(unittest.TestCase):
    def test_one(self):
        self.assertEqual(swap_bits_one(1234, 2, 4), 1222)
        self.assertEqual(swap_bits_two(1234, 2, 4), 1222)

    def test_two(self):
        self.assertEqual(swap_bits_one(123, 2, 3), 119)
        self.assertEqual(swap_bits_two(123, 2, 3), 119)

    def test_three(self):
        self.assertEqual(swap_bits_one(0, 0, 0), 0)
        self.assertEqual(swap_bits_two(0, 0, 0), 0)

    def test_four(self):
        self.assertEqual(swap_bits_one(9223372036854775807, 7, 9), 9223372036854775807)
        self.assertEqual(swap_bits_two(9223372036854775807, 7, 9), 9223372036854775807)


if __name__ == "__main__":
    unittest.main()