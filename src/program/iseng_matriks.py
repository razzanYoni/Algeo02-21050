import numpy as np
from sympy import *
import cv2 as cv

def numpy_to_sympy(x):
    return Matrix(x.tolist())

def sympy_to_numpy(x):
    return np.array(x).astype(np.float64)

def printMatrix(x):
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            print(x[i,j], end=' ')
        print()

M = np.matrix([[1,2,5], [30,21,8]])
printMatrix(M)
print("ini adalah transpose")
printMatrix(M.transpose())
print()

M2 = M.transpose()
# print("perkalian matrix")
# printMatrix(np.matmul(M, M2))
# print()

m1 = np.matmul(M2, M)
print("hasil transpose")
printMatrix((m1))
print()

m2 = np.matmul(M, M2)
print("hasil transpose cara 2")
printMatrix(m2.transpose())
print()

M = numpy_to_sympy(M)
printMatrix(M)
print()

M_rref = M.rref()

printMatrix(M_rref[0])
print()

print(M_rref[1]) # pivot columns
print()

# coba print elemen
print(M_rref[0][1,2]) # udah langsung float bisa dioperasikan secara matematis
print()