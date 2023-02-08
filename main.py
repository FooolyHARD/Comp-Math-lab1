import numpy

import math_utils.inputs as i
import math_utils.diag_fixes as df
import math_utils.col_swap as cs
import math_utils.row_swap as rs
import utils.prints as p

def main():
    values = i.getval()
    epsilon = values[0]
    matrix_size = values[1]
    matrix = numpy.array(values[2])
    iterations = 0
    p.printerr(
        "Диагональное преобладание в исходной матрице отсутствует, нужно поменять столбцы или строки\n Меняю..."
    )
    while (df.isPredomonanceOfDiagonalElements(matrix_size, matrix) == False):
        df.getPredomenanceOfDiagonalElements(matrix_size, matrix)
        iterations +=1
        if iterations == matrix_size*matrix_size:
            p.printcriterr(p.printbold("За "+str(iterations)+" итераций не получилось вычислить диагональное преобладание"))
            break
        p.printinfo(matrix)
        p.printsucces("В матрице присутствует диагональное преобладание")
main()