#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_len = len(row)
        for a in range(row_len):
            if a < (row_len - 1):
                print("{:d}".format(row[a]), end=' ')
            else:
                print("{:d}".format(row[a]), end='')
        print()
