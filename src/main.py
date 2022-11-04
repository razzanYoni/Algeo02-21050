import numpy as np
from sympy import *


def numpy_to_sympy(x):
    return Matrix(x.tolist())

def sympy_to_numpy(x):
    return np.array(x).astype(np.float64)

def printMatrix(x):
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            print(x[i,j], end=' ')
        print()

M = np.matrix([[1,2,5], [3,4,6]])
printMatrix(M)
print()

M = numpy_to_sympy(M)
printMatrix(M)
print()

M_rref = M.rref()

printMatrix(M_rref[0]) # matrix in reduced row echelon form
print()

print(M_rref[1]) # pivot columns
print()

# coba print elemen
print(M_rref[0][1,2]) # udah langsung float bisa dioperasikan secara matematis
print()