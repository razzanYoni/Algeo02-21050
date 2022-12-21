from PIL import Image
import numpy as np
import cv2
import matplotlib.image as image
from skimage.color import rgb2gray
import os

def normalized_obj_img(image) :
    # Mengembalikan matrix dari image "name" yang sudah dinormalisasi
    # yaitu di crop di bagian muka dan berukuran 256 x 256

    # Membaca image dan mengubah dalam bentuk grayscale
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Mendeteksi wajah
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face = face_cascade.detectMultiScale(img, 1.1, 4)
    
    # Wajah tidak terdeteksi
    if face is ():
        # cv2.imshow("face", img)
        # cv2.waitKey()
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

def normalized_obj_img_None(image) :
    # Mengembalikan matrix dari image "name" yang sudah dinormalisasi
    # yaitu di crop di bagian muka dan berukuran 256 x 256

    # Membaca image dan mengubah dalam bentuk grayscale
    img = rgb2gray(image)

    # resize image
    img = Image.fromarray(img).resize((256,256))
    return np.array(img)

def normalizedNone(pathOfImage) :
    # I.S : pathOfImage adalah path dari image yang akan dinormalisasi
    # F.S : M   engembalikan matrix dari image "name" yang sudah dinormalisasi berukuran 256 x 256

    # Membaca image dan mengubah dalam bentuk grayscale
    img = image.imread(pathOfImage)
    img = rgb2gray(img)

    # resize image
    img = Image.fromarray(img).resize((256,256))
    return np.array(img)

def normalized(name) :
    # Mengembalikan matrix dari image "name" yang sudah dinormalisasi
    # yaitu di crop di bagian muka dan berukuran 256 x 256

    # Membaca image dan mengubah dalam bentuk grayscale
    img = cv2.imread(name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Mendeteksi wajah
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face = face_cascade.detectMultiScale(img, 1.1, 4)
    
    # Wajah tidak terdeteksi
    if face is ():
        # cv2.imshow("face", img)
        # cv2.waitKey()
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

    return np.array(face, dtype=np.uint32)

def load(dir) :
    # Mengembalikan array of normalized image dari directory yang dimasukkan
    T = []
    NoneType = []
    for i in range(len(os.listdir(dir))) :
        file = os.listdir(dir)[i]
        image = (dir + r'/' + file)
        array = normalized(image)
        if (array is not None) :
            T.append(array)
        else :
            NoneType.append(i)
        
    return T, NoneType

def loadWithoutCascade(dir) :
    # Mengembalikan array of normalized image dari directory yang dimasukkan
    T = []
    for file in os.listdir(dir) :
        image = (dir + r'/' + file)
        array = normalizedNone(image)
        T.append(array)
    return T