"""Fungsi-fungsi Eigen"""
from PIL import Image
import numpy as np
import os
from loader import *
import sys

"""Fungsi-fungsi Eigen"""
def qr_hr(A, dtype = float):
    """
    O(2m^3) for given m*m matrix
    Fungsi  : mendekomposisi A menjadi Q * R dengan Q adalah matrix orthogonal dan R adalah  
        matrix segitiga atas, menggunakan metode Householder Reflection
    reff :https://rpubs.com/aaronsc32/qr-decomposition-householder
    Input A : matrix of float
    Output  : tuple of matrix (Q, R) 
    """

    (num_row, num_col) = np.shape(A)
    Q = np.eye(num_row)
    R = np.copy(A)    
    for n in range (num_col):
        H = np.eye(num_row)
        x = R[n:, n]
        e = np.zeros(len(x))
        e[0] = 1
        v = x + np.sign(x[0]) * np.linalg.norm(x) * e
        H[n:, n:] = np.eye(len(x)) - 2 * (np.outer(v,v))/v.dot(v)
        Q = Q.dot(H)
        R = H.dot(R)
    return Q, R
    
def eval_evec(A, iter = 25):
    """
    Fungsi  : mencari eigen value dari matrix A yang diberikan dengan metode Q R iteration
    reff    : https://www.physicsforums.com/threads/how-do-i-numerically-find-eigenvectors-for-given-eigenvalues.561763/
    Input A : matrix of float (prekondisi: matrix simetris agar approximasi optimal)
    Output  : List of float (list of eigen value dari A)
    """
    Temp = np.copy(A)
    evec = np.eye(len(A))
    for _ in range (iter):
        (Q, R) = qr_hr(Temp)
        evec = evec.dot(Q)
        Temp = R.dot(Q)
    return [Temp[i][i] for i in range (len(Temp))], evec

def getResultEigenFaceFromImageFile(pathDir, pathImage) :
    # I.S : path terdefinisi
    # F.S : Mengembalikan nama file dengan eigen distance terkecil dan hasil foto

    # KAMUS LOKAL
    # ArrayOfMatrix : array of Matrix DataSet
    # matrixSum : Matrix
    # matrixMedian : Matrix
    # matrixCovariance : Matrix
    # eigenValue : array of float
    # eigenVector : array of array of float
    # i : integer

    # ALGORITMA

    # Load DataSet
    ArrOfMatrix = load(pathDir)

    # Ubah Matrix menjadi vektor
    ArrOfVector = np.zeros((len(ArrOfMatrix), ArrOfMatrix[0].shape[0]*ArrOfMatrix[0].shape[1]))
    for i in range(len(ArrOfMatrix)) :
        ArrOfVector[i] = ArrOfMatrix[i].flatten('F')
    
    ArrOfVector = ArrOfVector.T

    # Calculate the mean of the data
    mean = np.mean(ArrOfVector, axis=1)

    # Subtract the mean from the data
    ArrOfDiffVector = ArrOfVector - mean[:,None]

    # Calculate the covariance matrix
    tempMatrix = ArrOfDiffVector[:]
    MatrixCovariance = np.matmul(tempMatrix, tempMatrix.transpose())
    MatrixCovariance = MatrixCovariance / (ArrOfDiffVector.shape[1])

    # Hitung EigenValue dan EigenVector
    eigenValue, eigenVector = eval_evec(MatrixCovariance)

    eigenVector = eigenVector[:,0:11]

    # Hitung weight ingat sususan terurut ke kanan bukan ke bawah
    weight = np.zeros((ArrOfDiffVector.shape[0], eigenVector.shape[1]))

    for i in range(ArrOfDiffVector.shape[1]) :
        tempDifference = ArrOfDiffVector[:,i]
        for j in range(eigenVector.shape[1]) :
            tempVector = eigenVector[:,j]
            weight[i][j] = np.dot(tempDifference, tempVector)


    # # Susunan juga ke kanan bukan ke bawah
    # ReconstructedVector = []

    # for i in range(len(eigenVector)) :
    #     temp = []
    #     for j in range(len(eigenVector[i])) :
    #         temp.append(weight[i,j] * eigenVector[:,j])
        
    #     temp = np.array(temp)
    #     temp = np.real(temp)

    #     for k in range(len(temp)) :
    #         temp[k] = temp[k].sum(axis=0)
    #     temp = temp[:,0]
        
    #     for l in range(len(temp)) :
    #         temp[l] = temp[l] + mean[l]

    #     ReconstructedVector.append(temp) 
    
    # ReconstructedVector = np.array(ReconstructedVector)

    # Load Image yang ingin diuji
    testImage = Img(pathImage)

    # Ubah Matrix menjadi vektor
    testImageVector = testImage.flatten('F')

    # Difference Vector dari Test Image dengan Nilai Tengah
    differenceImageVector = testImageVector - mean

    # Hitung weight ingat sususan terurut ke kanan bukan ke bawah
    weightTestImage = np.zeros((eigenVector.shape[1]))

    # Susunan juga ke kanan bukan ke bawah
    for i in range(eigenVector.shape[1]) :
        weightTestImage[i] = np.dot(differenceImageVector, eigenVector[:,i])

    min = sys.maxsize
    minIdx = -1

    EucledianDistance = np.zeros((weight.shape[0]))

    for i in range(weight.shape[0]) :
        temp = 0
        for j in range(weight.shape[1]) :
            temp += (weightTestImage[j] - weight[i,j])**2
        
        EucledianDistance[i] = temp**0.5

        if temp < min :
            min = temp
            minIdx = i

    fileName = os.listdir(pathDir)[minIdx]

    return fileName, pathDir + '/' + fileName