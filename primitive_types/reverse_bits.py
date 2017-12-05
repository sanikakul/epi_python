"""
Reversing bits in a number


"""


def main():
    x = 71
    print "{0}: {0:b}".format(x)

    output = reverse_bits_one(x)

    print "{0}: {0:b}".format(output)


def swap_bits(x, i, j):
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


def reverse_bits_one(x):
    int_length = len("{0:b}".format(x))
    for i in range(0, int_length/2):
        x = swap_bits(x, i, int_length-1-i)
    return x


if __name__ == "__main__":
    main()