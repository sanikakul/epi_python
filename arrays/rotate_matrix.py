def rotate_matrix(input_matrix):
    n = len(input_matrix)
    i = n - 1
    while i > 0:
        j = len(input_matrix) - 1 - i
        current = i
        orig_j = j
        orig_current = current
        while j < i:
            input_matrix[orig_j][j], input_matrix[j][current] = input_matrix[j][current], input_matrix[orig_j][j]
            input_matrix[orig_j][j], input_matrix[current][orig_current] = input_matrix[current][orig_current], input_matrix[orig_j][j]
            input_matrix[orig_j][j], input_matrix[orig_current][orig_j] = input_matrix[orig_current][orig_j], input_matrix[orig_j][j]
            j += 1
            orig_current -= 1
        i -= 1
    return input_matrix