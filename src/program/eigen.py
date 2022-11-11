"""Fungsi-fungsi Eigen"""

# Kalau ada library tambahan yang dibutuhkan, import disini
import numpy as np

# 4.3.2
"""Menghitung nilai tengah dari data"""
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
def SubtractMatrix(M1,M2) :
    # I.S : Matrix M1 dan M2 terdefinisi dengan ukuran sama
    # F.S : Mengembalikan selisih dari matrix

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
            M1[i,j] = M1[i,j] - M2[i,j]

    return M1

# 4.3.4
"""Hitung Kovarian"""