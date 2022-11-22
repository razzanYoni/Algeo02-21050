"""Fungsi-fungsi Eigen"""
from PIL import Image
import numpy as np
import os
from loader import *
import sys
from pandas import DataFrame
import cv2
import matplotlib.pyplot as plt

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
    
def eval_evec(A, iter = 50):
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

    # Ubah menjadi n^2
    ArrOfVector = np.array([np.array(i).flatten('F') for i in ArrOfMatrix]).T

    # Hitung Mean
    mean = np.mean(ArrOfMatrix, axis = 0)
    meanFlatten = mean.flatten()

    # Hitung Difference
    ArrOfDiff = ArrOfMatrix - mean
    dimension = len(ArrOfVector[0])
    ArrOfDiffVec = np.array([ArrOfVector[:,i] - meanFlatten for i in range (dimension)]).T

    # Hitung Covariance
    MatrixCovariance = np.matmul(ArrOfDiffVec.T, ArrOfDiffVec)

    # Hitung Eigen
    eigenValue, eigenVector = eval_evec(MatrixCovariance)

    # Hitung Eigen Face
    eigenFace = []

    for i in range(len(ArrOfDiffVec[0])) :
        u = np.zeros((len(ArrOfDiff[0]), len(ArrOfDiff[0])))
        for j in range(len(ArrOfDiffVec[0])) :
            u += eigenVector[i][j] * ArrOfDiff[j]
        eigenFace.append(u.flatten('F'))
    eigenFace = np.array(eigenFace)
    eigenFace = eigenFace.T
    

    # eigenFace = np.array([i/(i.sum()) for i in eigenFace])

    # TEST EIGEN FACE
    # for i in range (len(eigenFace)):
    #     plt.imshow(eigenFace[i], cmap="gray")
    #     plt.show()


    # Hitung weight DataSet
    M = len(eigenVector)
    flattenDimension = len(ArrOfDiffVec[0])
    weight = []
    for i in range(len(ArrOfDiffVec[0])) :
        tempDifference = ArrOfDiffVec[:,i]
        comb = []
        for j in range(len(eigenFace[0])) :
            tempEigFace = eigenFace[:,j]
            dot = np.matmul(tempEigFace, tempDifference)
            comb.append(dot)
        weight.append(comb)

    weight = np.array(weight)
    # temp = np.zeros((256,256))
    # for i in range(M):
    #     temp += weight[0][i] * eigenFace[i,:]
    # plt.imshow(temp, cmap="gray")
    # plt.show()


    # Load Test Image
    testImage = Img(pathImage)

    # Difference Matrix dari Test Image dengan Nilai Tengah
    differenceImage = (testImage - mean).flatten('F')
    # differenceImage = np.array(differenceImage).T

    # Eigen Face dari Test Image
    weightTestImage = np.zeros((1, flattenDimension))
    for i in range(M) :
        tempEigFace = eigenFace[:,i]
        weightTestImage[0][j] = np.dot(tempEigFace, differenceImage)

    # Hitung Eigen Distance
    eigenDistanceOfTestImage = np.zeros((M))

    for i in range(M) :
        dummyMatrix = weightTestImage - weight[:,i]

        for j in range(dummyMatrix.shape[0]) :
            for k in range(dummyMatrix.shape[1]) :
                eigenDistanceOfTestImage[i] += dummyMatrix[j,k]**2
    
    minIdx = np.argmin(eigenDistanceOfTestImage)

    imgMatrix = ArrOfMatrix[minIdx]

    # blue,green,red = cv.split(imgMatrix)
    # imgMatrix = cv.merge((red,green,blue))
    # color_img = cv.cvtColor(imgMatrix, cv.COLOR_GRAY2RGB)

    # photoResult = Image.fromarray(color_img)

    fileName = os.listdir(pathDir)[minIdx]

    return  fileName, pathDir + '/' + fileName