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
def subtractMatrix(M1, M2) :
    # I.S : Matrix M1 dan M2 terdefinisi dengan ukuran sama
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
            M1[i,j] = M1[i,j] - M2[i,j]
    return M1

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
    # eigenValue : array of float
    # eigenVector : array of array of float

    # ALGORITMA
    

    return eigenValue, eigenVector