"""
Delete duplicates from a sorted array

Eg: input: [2, 3, 5, 5, 7, 11, 11, 11, 13]
    output: [2, 3, 5, 7, 11, 13, 0, 0, 0]

"""


def delete_sorted_duplicates_one(input_array):
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


if __name__ == "__main__":
    print delete_sorted_duplicates_two([1, 1, 1, 1, 1, 1])
