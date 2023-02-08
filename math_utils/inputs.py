import numpy

import utils.prints as pr

def getval():
    pr.printinfo("Введите точность")
    epsilon = float(input())
    pr.printinfo("Введите размерность")
    matrix_size = int(input())
    if (matrix_size > 20):
        pr.printerr("Неподходящий размер")
        return
    matrix_iter = 0
    matrix = [None] * matrix_size
    pr.printinfo("Введите саму матрицу")
    while matrix_iter != matrix_size:
        matrix[matrix_iter] = list(map(int, input().split()))
        matrix_iter += 1
    pr.printsucces(numpy.array(matrix))
    return epsilon, int(matrix_size), numpy.array(matrix)