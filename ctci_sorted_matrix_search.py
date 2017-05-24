"""Cracking the Coding Interview

    10.9 Sorted Matrix Search
    Given an M x N matrix in which each row and each column is sorted in
    ascending order, write a method to find an element."""

def find_element(matrix, element):
    """Given an M x N matrix in which each row and each column is sorted in
    ascending order, write a method to find an element.
    """

    row_i = 0
    col_i = len(matrix[0]) - 1

    while row_i < len(matrix) and col_i >= 0:
        to_check = matrix[row_i][col_i]
        if to_check == element:
            return True
        elif to_check > element:
            col_i -= 1
        else:
            row_i += 1

    return False


sample_matrix = [[15, 20, 40, 69],
                 [20, 35, 80, 95],
                 [30, 55, 90, 105],
                 [40, 85, 120, 120]
                ]

sample_matrix_2 = [[15, 20, 40, 69],
                   [20, 35, 80, 95],
                   [30, 55, 90, 105]
                  ]

print find_element(sample_matrix, 85)
print find_element(sample_matrix, 34)
print find_element(sample_matrix, 15)
print find_element(sample_matrix_2, 85)
print find_element(sample_matrix_2, 34)
print find_element(sample_matrix_2, 15)
