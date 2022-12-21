"""Fungsi-fungsi Eigen"""
import numpy as np
import os
from loader import *
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
    # return [Temp[i][i] for i in range (len(Temp))], evec  # dengan eigen value
    return evec

def nxnTOn2(ArrayOfMatrix) :
    # I.S : ArrayOfMatrix terdefinisi
    # F.S : Mengembalikan ArrayOfMatrix dalam bentuk n^2

    # KAMUS LOKAL
    # ArrayOfVector : array of array of float
    # i : integer

    # ALGORITMA
    ArrayOfVector = np.array([np.array(i).flatten() for i in ArrayOfMatrix])
    return ArrayOfVector

def meanOfMatrix(ArrOfVector) :
    # I.S : ArrOfMatrix terdefinisi
    # F.S : Mengembalikan mean dari ArrOfMatrix

    # KAMUS LOKAL
    # mean : Matrix

    # ALGORITMA
    mean = np.mean(ArrOfVector, axis = 0)
    return mean

def DifferenceOfMatrix(ArrOfVector, mean) :
    # I.S : ArrOfMatrix terdefinisi
    # F.S : Mengembalikan ArrOfMatrix - mean dan ArrOfVector - mean

    # KAMUS LOKAL
    # ArrOfDiff : array of Matrix

    # ALGORITMA
    ArrOfDiff = np.subtract(ArrOfVector, mean)
    return ArrOfDiff

def CovarianceOfMatrix(ArrOfDiffVec) :
    # I.S : ArrOfDiffVec terdefinisi
    # F.S : Mengembalikan Covariance dari ArrOfDiffVec

    # KAMUS LOKAL
    # MatrixCovariance : Matrix

    # ALGORITMA
    MatrixCovariance = np.matmul(ArrOfDiffVec, ArrOfDiffVec.T)
    return MatrixCovariance

def ArrOfEigenFace(ArrOfDiffVec, eigenVector) :
    # I.S : ArrOfDiffVec dan eigenVector terdefinisi
    # F.S : Mengembalikan hasil eigen face

    # KAMUS LOKAL
    # eigenFace : array of array of float

    # ALGORITMA
    eigenFace = []
    for i,j in zip(eigenVector, ArrOfDiffVec) :
        eigenFaceOfImg = np.zeros(256*256) 
        for k in i :
            eigenFaceOfImg +=  k * j
        eigenFaceOfImg = eigenFaceOfImg / np.linalg.norm(eigenFaceOfImg)
        eigenFace.append(eigenFaceOfImg)
    eigenFace = np.array(eigenFace)
    return eigenFace

def weightOfImg(EigenFace, ArrOfDiffVec) :
    # I.S : EigenFace dan ArrOfDiffVec terdefinisi
    # F.S : Mengembalikan weight dari setiap data

    # KAMUS LOKAL
    # weight : array of array of float

    # ALGORITMA
    weight = [[np.dot(j,i) for j in EigenFace] for i in ArrOfDiffVec]
    weight = np.array(weight)
    return weight

def getResultEigenFaceFromImageFile(pathDir, boolFaceCascade:bool=True, pathImage=None, NoneType = []) :
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
    if boolFaceCascade :
        ArrOfMatrix, NoneType = load(pathDir)
    else :
        ArrOfMatrix = loadWithoutCascade(pathDir)
    
    # Ubah menjadi n^2
    ArrOfVector = nxnTOn2(ArrOfMatrix)

    # Hitung Mean yang Sudah Diflat
    mean = meanOfMatrix(ArrOfVector)

    # Hitung Difference
    ArrOfDiffVec = DifferenceOfMatrix(ArrOfVector, mean)

    # Hitung Covariance
    MatrixCovariance = CovarianceOfMatrix(ArrOfDiffVec)

    # Hitung Eigen
    eigenVector = eval_evec(MatrixCovariance)

    # Hitung Eigen Face
    eigenFace = ArrOfEigenFace(ArrOfDiffVec, eigenVector)    

    # TEST EIGEN FACE
    # for i in (eigenFace):
    #     i = i.reshape(256,256)
    #     plt.imshow(i, cmap="gray")
    #     plt.show()

    # Hitung weight DataSet
    weightOfDataSet = weightOfImg(eigenFace, ArrOfDiffVec)

    # Test Menampilkan weight DataSet
    # for i,j in zip(weight, eigenFace) :
    #     temp = np.zeros((256*256))
    #     for k in i :
    #         temp += k * j
    #     temp = temp.reshape(256,256)
    #     plt.imshow(temp, cmap="gray")
    #     plt.show()

    # Load Test Image
    if type(pathImage) is str :
        if boolFaceCascade :
            testImage = normalized(pathImage)
            if testImage is None :
                testImage = normalizedNone(pathImage).flatten()
            else :
                testImage = testImage.flatten()
        else :
            testImage = normalizedNone(pathImage).flatten()
    else :
        testImage = pathImage.flatten()
        # if boolFaceCascade :
        #     testImage = normalized_obj_img(pathImage)
        #     if testImage is None :
        #         testImage = normalized_obj_img_None(pathImage).flatten()
        #     else :
        #         testImage = testImage.flatten()
        # else :
        #     testImage = normalizedNone(pathImage).flatten()

    # Difference Matrix dari Test Image dengan Nilai Tengah
    diffImage = DifferenceOfMatrix([testImage], mean)

    # Eigen Face dari Test Image
    weightOfTestImage = weightOfImg(eigenFace, diffImage)

    # Hitung Eigen Distance
    lenOfWeight = len(weightOfDataSet)
    eigenDistanceOfTestImage = np.zeros(lenOfWeight)

    for i in range(lenOfWeight) :
        for j in (np.subtract(weightOfTestImage[0], weightOfDataSet[i])) :
                eigenDistanceOfTestImage[i] += j**2
    
    minIdx = np.argmin(eigenDistanceOfTestImage)
    # print(eigenDistanceOfTestImage)

    # if len(NoneType) > 0 :
    for i in NoneType :
        if (i <= minIdx) :
            minIdx +=1
        else :
            break

    fileName = os.listdir(pathDir)[minIdx]

    return  fileName, pathDir + '/' + fileName

if __name__ == "__main__":
    from tkinter import filedialog
    pathDir = filedialog.askdirectory()
    pathImage = filedialog.askopenfilename()
    fileName, path = getResultEigenFaceFromImageFile(pathDir, True, pathImage)
    print("image", pathImage)
    print("closest", fileName)