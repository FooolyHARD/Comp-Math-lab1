import utils.prints as p


def row_swap(matrix, matrix_size, a, b):
    #p.printinfo("Вот текущая матрица, какие строки поменять местами?")
    #p.printsucces(matrix)
    for i in range(0, matrix_size):
        matrix[int(a) - 1][i], matrix[int(b) - 1][i] = matrix[int(b) - 1][i], matrix[int(a) - 1][i]
    #p.printinfo("Вот итоговая матрица")
    #p.printsucces(matrix)
    return matrix
