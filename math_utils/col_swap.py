import utils.prints as p

def col_sawp(matrix, matrix_size, a, b):
    #p.printinfo("Вот текущая матрица, какие столбцы поменять местами?")
    #p.printsucces(matrix)
    for i in range (0, matrix_size):
        matrix[i][int(a)-1], matrix[i][int(b)-1] = matrix[i][int(b)-1], matrix[i][int(a)-1]
    #p.printinfo("Вот итоговая матрица")
    #p.printsucces(matrix)
    return matrix