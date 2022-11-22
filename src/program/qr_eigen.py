import numpy as np

def qr_hr(A):
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
        # (Q, R) = qr_hr(Temp)            # Dekomposisi Q R dengan metode Household Rotation sebagai benchmark
        (Q, R) = np.linalg.qr(Temp)     # Dekomposisi Q R dengan built-in numpy
        evec = evec.dot(Q)
        Temp = R.dot(Q)
    return [Temp[i][i] for i in range (len(Temp))], evec

def random_sim_matrix(n = 10, min = 0, max = 9): 
    """
    Fungsi      : mengembalikan simetris random dengan ukuran n*n, dengan distribusi nilai elemen [min..max]
    Input n     : <optional> float (size dari matrix) 
    Input min   : <optional> float (batas bawah distribusi elemen)
    Input max   : <optional> float (batas atas distribusi elemen)
    Output      : Matrix of float
    """
    from random import randint
    T = [[0 for _ in range (n)] for _ in range (n)]
    for i in range (n):
        T[i][i] = randint(min, max)
        for j in range (i):
            T[i][j] = randint(min, max)
            T[j][i] = T[i][j]
    return T 


def test(size = 10):
    from pandas import DataFrame
    A = np.array(random_sim_matrix(size))
    eval, evec = eval_evec(A)
    print("Eigen-values from our numerical method :")
    print(DataFrame(eval))
    print("Eigen-vectors from our numerical method :")
    print(DataFrame(evec))
    print()
    print()
    evalnp, evecnp = np.linalg.eigh(A)
    print("Eigen-values from numpy :")
    print(DataFrame(evalnp))
    print("Eigen-vectors from numpy :")
    print(DataFrame(evecnp))


if __name__ == "__main__" :
    test(size = 64)
