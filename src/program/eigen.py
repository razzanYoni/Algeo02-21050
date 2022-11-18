"""Fungsi-fungsi Eigen"""

import numpy as np

"""Fungsi-fungsi Eigen"""
# Jumlah dari 2 Matrix
def sumMatrix(M1, M2) : 
    # I.S : Matrix terdefinisi dnegan ukuran sama
    # F.S : Mengembalikan jumlah dari matrix
    
    # KAMUS LOKAL
    # i : integer
    # j : integer
    # nCol : integer
    # nRow : integer

    # ALGORITMA
    nRow = M2.shape[0]
    nCol = M1.shape[1]
    for i in range(nRow) :
        for j in range(nCol) :
            M1[i,j] = M1[i,j] + M2[i,j]
    return M1

# Penguranan antara 2 matrix
def subtractEigenMatrixInString(M1, M2) :
    # I.S : Matrix M1 dan M2 terdefinisi dengan ukuran sama, M1 dan M2 adalah matrix yang berisi nilai string
    # F.S : Mengembalikan pengurangan dari matrix

    # KAMUS LOKAL
    # i : integer
    # j : integer
    # nCol : integer
    # nRow : integer

    # ALGORITMA
    nRow = M1.shape[0]
    nCol = M1.shape[1]
    for i in range(nRow) :
        for j in range(nCol) :
            if (isString(M1[i,j]) and i == j) :
                M1[i,j] = M1[i,j] + ' - ' + M2[i,j]
            else :
                M1[i,j] = float(M1[i,j]) - float(M2[i,j])

    return M1

# Konversi elemen matrix menjadi string
def convertMatrixToString(Matrix) :
    # I.S : Matrix terdefinisi
    # F.S : Mengembalikan Matrix berelemen string

    # KAMUS LOKAL
    # MatResult : Matrix
    # i,j : integer
    # nCol : integer
    # nRow : integer

    # ALGORITMA
    MatResult = np.zeros((Matrix.shape[0], Matrix.shape[1]), dtype=str)

    nRow = Matrix.shape[0]
    nCol = Matrix.shape[1]

    for i in range(nRow) :
        for j in range(nCol) :
            MatResult[i,j] = str(Matrix[i,j])

    return MatResult

# Concatenate 2 matrix
def concatenateMatrix(M1, M2) :
    # I.S : Matrix M1 dan M2 terdefinisi dengan ukuran sama
    # F.S : Mengembalikan konkatenansi secara horizontal dari matrix

    # KAMUS LOKAL

    # ALGORITMA
    return np.concatenate((M1, M2), axis=1)


# Menentukan apakah nilai tersebut string atau bukan
def isString(val) :
    # I.S val terdefinisi, val adalah sebuah value
    # F.S mengembalikan nilai True jika val adalah string, False jika bukan

    # KAMUS LOKAL

    # ALGORITMA
    try :
        float(val)
        return False
    except ValueError :
        return True

# 4.3.2
"""Menghitung nilai tengah dari data"""
# Mengembalikan nilai tengah dari matrix
def getMedian(M, nData) :
    # I.S : Matrix dan nData terdefinisi
    # F.S : Mengembalikan nilai tengah dari matrix

    # KAMUS LOKAL
    # i : integer
    # j : integer
    # nCol : integer
    # nRow : integer

    # ALGORITMA
    nRow = M.shape[0]
    nCol = M.shape[1]
    for i in range(nRow) :
        for j in range(nCol) :
            M[i,j] = M[i,j] / nData
    return M

# 4.3.3
"""Menghitung Selisih antara Training Image dengan Nilai Tengah"""
# Pasti positif kah?
def DifferenceMatrix(MTrainingImage,MNilaiTengah) :
    # I.S : Matrix MTrainingImage dan MNilaiTengah terdefinisi dengan ukuran sama
    # F.S : Mengembalikan selisih dari matrix

    # KAMUS LOKAL
    # i : integer
    # j : integer
    # nCol : integer
    # nRow : integer

    # ALGORITMA
    nRow = MTrainingImage.shape[0]
    nCol = MTrainingImage.shape[1]
    for i in range(nRow) :
        for j in range(nCol) :
            MTrainingImage[i,j] = abs(MTrainingImage[i,j] - MNilaiTengah[i,j])

    return MTrainingImage

# 4.3.4
"""Hitung Kovarian"""
# Menghitung kovarian dari matrix
def getCovariance(ArrayOfMatrix) :
    # I.S : ArrayOfMatrix terdefinisi, ArrayOfMatrix sudah berisikan Matrix Selisih dari Training Image dengan Nilai Tengah (dari 4.3.3)
    # F.S : Mengembalikan kovarian dari matrix

    # KAMUS LOKAL
    # i : integer
    # length : integer

    # ALGORITMA
    length = len(ArrayOfMatrix)
    for i in range(length) :
        ArrayOfMatrix[i] = np.matmul(ArrayOfMatrix[i].transpose(),ArrayOfMatrix[i])

    MatrixResult = ArrayOfMatrix[0]
    for i in range(1,length) :
        MatrixResult = sumMatrix(MatrixResult,ArrayOfMatrix[i])

    return MatrixResult

# 4.3.5
"""Hitung EigenValue dan EigenVector"""
# Menghitung eigenvalue dan eigenvector dari matrix
def getEigen(MatrixCovariance) :
    # I.S : MatrixCovariance terdefinisi
    # F.S : Mengembalikan eigenvalue dan eigenvector dari matrix

    # KAMUS LOKAL
    # MatrixS : Matrix {matrix hasil penguranan antara matrix covariance dengan matrix identitas}
    # ArrOfEigenValue : Array of float {array of eigenvalue}
    # n : integer {ukuran matrix}
    # i, j : integer
    # eigenValue : array of float
    # eigenVector : array of array of float

    # ALGORITMA

    """Menghitung eigenValue"""
    n = MatrixCovariance.shape[0]

    # Menghitung eigenvalue
    
    # Create a matrix of zeros
    # unico lambda : \u03BB
    MatrixEigenValue = np.zeros((n,n), dtype=str)
    for i in range(n):
        for j in range(n) :
            if (i != j) :
                MatrixEigenValue[i,j] = "0"
            else :
                MatrixEigenValue[i,j] = "\u03BB"

    # Kurangkan MatrixEigenValue dengan MatrixCovariance
    MatrixS = subtractEigenMatrixInString(MatrixEigenValue, convertMatrixToString(MatrixCovariance))

    # Cari setiap eigenvalue
    ArrOfEigenValue = []




    

    return eigenValue, eigenVector


def getEigenFaceFromDataSet(path) :
    # I.S : path terdefinisi
    # F.S : Mengembalikan eigenFace dari dataset

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
    ArrOfMatrix = load(path)

    # Hitung Nilai Tengah
    matrixSum = np.zeros((ArrOfMatrix[0].shape[0], ArrOfMatrix[0].shape[1]))
    for i in range(len(ArrOfMatrix)) :
        matrixSum = sumMatrix(matrixSum, ArrOfMatrix[i])
    matrixMedian = getMedian(matrixSum, len(ArrOfMatrix))

    # Hitung Selisih antara Training Image dengan Nilai Tengah
    MatrixDifference = np.zeros((len(ArrOfMatrix), ArrOfMatrix[0].shape[0], ArrOfMatrix[0].shape[1]))
    for i in range(len(ArrOfMatrix)) :
        MatrixDifference[i] = DifferenceMatrix(ArrOfMatrix[i], matrixMedian)

    # Hitung Kovarian
    MatrixCovariance = getCovariance(MatrixDifference)

    """Jangan Lupa diganti"""
    # Hitung EigenValue dan EigenVector
    eigenValue, eigenVector = getEigen(MatrixCovariance)
    eigenValue = np.real(eigenValue)
    eigenVector = np.real(eigenVector)

    # Hitung Eigen Face
    eigenFace = np.zeros((len(ArrOfMatrix), ArrOfMatrix[0].shape[0], ArrOfMatrix[0].shape[1]))
    for i in range(len(ArrOfMatrix)) :
        eigenFace[i] = np.matmul(MatrixDifference[i], eigenVector)
    
    return eigenFace, matrixMedian

def getResult(eigenFaceOfDataSet, matrixMedianOfDataSet, path) :
    # I.S : eigenFaceOfDataSet dan path terdefinisi
    # F.S : Mengembalikan result kecocokan dari image yang diuji dengan dataset

    # KAMUS LOKAL
    # eigenFaceOfTestImage : Matrix
    # result : float

    # ALGORITMA

    # Load Test Image
    testImage = Img(path)

    # Difference Matrix dari Test Image dengan Nilai Tengah
    differenceImage = DifferenceMatrix(testImage, matrixMedianOfDataSet)

    # Eigen Face dari Test Image
    eigenFaceOfTestImage = np.matmul(differenceImage, eigenFaceOfDataSet.transpose())

    # Hitung Eigen Distance
    max = -9999
    min = 9999

    eigenDistanceOfTestImage = np.zeros((len(eigenFaceOfDataSet)))

    for i in range(len(eigenFaceOfDataSet)) :
        dummyMatrix = eigenFaceOfTestImage - eigenFaceOfDataSet[i]

        for j in range(dummyMatrix.shape[0]) :
            for k in range(dummyMatrix.shape[1]) :
                eigenDistanceOfTestImage[i] += dummyMatrix[j,k]**2

        if eigenDistanceOfTestImage[i] > max :
            max = eigenDistanceOfTestImage[i]
        if eigenDistanceOfTestImage[i] < min :
            min = eigenDistanceOfTestImage[i]

    result = 100 - ((min/max) * 100)

    return result