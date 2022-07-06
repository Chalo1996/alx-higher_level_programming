#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def sq(num):
        return num * num
    if matrix:
        return [list(map(sq, i)) for i in matrix]
