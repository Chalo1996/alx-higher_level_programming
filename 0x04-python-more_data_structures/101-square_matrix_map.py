#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda mul: list(map(lambda x: x * x, mul)), matrix)))
