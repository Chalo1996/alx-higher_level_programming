#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides the elements of a matrix

    Args:
        matrix: The matrix to divide
        div: The divident

    Return:
        The return. The newly divided matrix

    """

    newMatrix = []

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) \
    of integers/floats")

    rowlen = None

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) \
        of integers/floats")

        if rowlen is None:
            rowlen = len(row)
        elif rowlen != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        for val in row:
            if type(val) is not int and \
               type(val) is not float:
                raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        newMatrix.append([round(val / div, 2) for val in row])

    return (newMatrix)
