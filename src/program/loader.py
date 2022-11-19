from PIL import Image
import numpy as np
from iseng_matriks import *
import cv2
import os

from numpy import linalg
def normalized(name) :
    # Mengembalikan matrix dari image "name" yang sudah dinormalisasi
    # yaitu di crop di bagian muka dan berukuran 256 x 256


    # Membaca image dan mengubah dalam bentuk grayscale
    img = cv2.imread(name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Mendeteksi wajah
    face_cascade = face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face = face_cascade.detectMultiScale(img, 1.1, 4)
    
    # Wajah tidak terdeteksi
    if face is ():
        cv2.imshow("face", img)
        cv2.waitKey()
        return None

    # Wajah terdeteksi
    for (x, y, w, h) in face:
        # Crop Face
        # w adalah lebar muka
        # h adalah tinggi muka
        if (w >= h) :
            face = img[y:y+w, x:x+w]
        else :
            face = img[y:y+h, x:x+h]
    face = Image.fromarray(face).resize((256,256))

    return np.array(face)

def load(dir) :
    # Mengembalikan array of normalized image dari directory yang dimasukkan
    T = []
    for file in os.listdir(dir) :
        image = (dir + r'/' + file)
        array = normalized(image)
        if (array is not None) :
            T.append(array)
        else :
            continue
    return T

# for image in T:  
# arr = normalized(r"./Data/pins_Adriana Lima/Adriana Lima0_0.jpg")
# printMatrix(arr)
# cv2.imshow("face", arr)
# cv2.waitKey()

# print(len(normalized(r"./Data/pins_Adriana Lima/Adriana Lima0_0.jpg")))
# def load(repository) :

# // matrix harus selalu kotak
# // uniform 256 x 256
# image = normalized(r"./Data/pins_Adriana Lima/Adriana Lima0_0.jpg")
# cv2.imshow("face", image)
# cv2.waitKey()