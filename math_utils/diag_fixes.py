import numpy as np

import math_utils.row_swap as rs
import math_utils.col_swap as cs

def isPredomonanceOfDiagonalElements(matrix_size, matrix):
    true_num = 0
    for i in range(0, matrix_size):
        sum = 0
        for j in range(0, matrix_size):
            if j == i:
                continue
            sum += matrix[i][j]
        if (np.absolute(matrix[i][i]) >= sum):
            true_num += 1
    return true_num == matrix_size

def getPredomenanceOfDiagonalElements(matrix_size, matrix):
    for i in range (0, matrix_size):
        largestElem = matrix[i][i]
        largestRowNum = i
        for j in range (0, matrix_size):
            if (matrix[j][i] >  largestElem):
                largestElem = matrix[j][i]
                largestRowNum = j
        if largestRowNum != i :
            rs.row_swap(matrix,matrix_size,i+1, largestRowNum)
            if not isPredomonanceOfDiagonalElements(matrix_size, matrix):
                cs.col_sawp(matrix,matrix_size,largestRowNum, j+1)
    return matrix