""" Program GUI Apps """
import tkinter as tk
import customtkinter as ctk
import cv2 as cv
import numpy as np    
import time 
from tkinter import filedialog
from PIL import ImageTk,Image
from loader import normalized_obj_img, normalized_obj_img_None
from eigenface import *

root = tk.Tk()

"""" Configure Gridv"""
root.title("BosenTuru") #title window
root.geometry("1280x720") # window size
root.configure(bg="#ffefd6")

def computeResult():
    global resultImage

    nama, pathRes = getResultEigenFaceFromImageFile(direc, boolFaceCascade, inputDir)
    
    img = Image.open(pathRes)
    imageSized = img.resize((256, 256))
    imageRes = ImageTk.PhotoImage(imageSized)

    resultImage.image = imageRes
    resultImage.configure(image=imageRes)
    
    result.configure(text=nama, text_color="green")

def TrueCascade():
    global boolFaceCascade

    boolFaceCascade = True

def FalseCascade():
    global boolFaceCascade

    boolFaceCascade = False

def capture():
    global resultImage
    global tesImage
    global framearr
    global result
    global direc
    global boolFaceCascade

    timeDummy = time.time()
    vid = cv.VideoCapture(0)

    # Create the haar cascade
    # face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while(direc is not None and boolFaceCascade is not None):
        # Capture the video frame by frame
        frame = vid.read()[1]

        # Cascade Bounding Box
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # faces = face_cascade.detectMultiScale(gray, 1.03, 3)
        # for (x,y,w,h) in faces:
        #     cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        # Resize the frame
        frame = Image.fromarray(frame).resize((256,256))

        # Display the frame
        imageTes = ImageTk.PhotoImage(image=frame)
        tesImage.image = imageTes
        tesImage.configure(image=imageTes)
        root.update()

        frame = np.array(frame)

        if cv.waitKey(1) and int(time.time() - timeDummy) % 10 == 0 and int(time.time() - timeDummy) != 0:
            if boolFaceCascade:
                mat = normalized_obj_img(frame)
                if mat is None:
                    mat = normalized_obj_img_None(frame)
            else:
                mat = normalized_obj_img_None(frame)

            nama, pathRes = getResultEigenFaceFromImageFile(direc, boolFaceCascade, mat)
            img = Image.open(pathRes)
            imageSized = img.resize((256, 256))
            imageRes = ImageTk.PhotoImage(imageSized)

            resultImage.image = imageRes
            resultImage.configure(image=imageRes)
            
            result.configure(text=nama, text_color="green")
            timeDummy = time.time()

        elif (cv.waitKey(1) & 0xFF == ord(' ')):
            vid.release()
            cv.destroyAllWindows()
            break

def askDirectory():
    global direc

    direc = filedialog.askdirectory()
    
def printImage():
    global inputDir
    global tesImage

    inputDir =filedialog.askopenfilename()
    img  = Image.open(inputDir)
    imageSized = img.resize((256, 256))
    imageTes = ImageTk.PhotoImage(imageSized)
    tesImage.image = imageTes
    tesImage = ctk.CTkLabel(master=showFrame, image=imageTes)
    tesImage.grid(column=1, row=0, sticky="E", pady= 60, padx=50)

def page2():
    global showFrame
    global tesImage
    global result
    global resultImage

    homeFrameMain.destroy()

    imageFrameMain = ctk.CTkFrame(master=root, width=1280, height=720, fg_color="#ffefd6", corner_radius=0)
    imageFrameMain.grid()

    # ShowFrame section

    emptyImage = ImageTk.PhotoImage(Image.open(".\Data\empty-256x256.png"))

    showFrame = ctk.CTkFrame(master=imageFrameMain, fg_color="#3A8891", corner_radius=0)
    showFrame.grid(column=0, row=0, sticky="")

    tesShowTitle = ctk.CTkLabel(master=showFrame, text="Test Image", text_font=("Inter Bold", 15))
    tesShowTitle.grid(column=0, row=0, sticky="E",padx=20)

    #tesImage.image = emptyImage
    tesImage = ctk.CTkLabel(master=showFrame, image=emptyImage, fg_color="#cfcfcf")
    tesImage.grid(column=1, row=0, sticky="E", pady= 60, padx=50)

    resultShowTitle = ctk.CTkLabel(master=showFrame, text="Closest\n Result", text_font=("Inter Bold", 15))
    resultShowTitle.grid(column=0,row=1, sticky="E",padx=20)

   # resultImage.image = emptyImage
    resultImage = ctk.CTkLabel(master=showFrame, image=emptyImage, fg_color="#cfcfcf")
    resultImage.grid(column=1, row=1, sticky="E",pady=50, padx=50)

    # inputFrame section

    inputFrame = ctk.CTkFrame(master=imageFrameMain ,fg_color="#ffefd6", corner_radius=0)
    inputFrame.grid(column=1, row=0, sticky="W N", padx=170)

    titlePage = ctk.CTkLabel(master=inputFrame, text="Input from Image", text_font=("Tahoma",18), text_color="#0E5E6F")
    titlePage.grid(column=0, row=0, sticky="N", columnspan=2, pady=50, padx=100)
    resultTitle = ctk.CTkLabel(master=inputFrame, text="Result", text_font=("Tahoma Bold", 30), text_color="#0E5E6F")
    resultTitle.grid(column=0, row=1, sticky="N", columnspan=2, pady=20)

    result = ctk.CTkLabel(master=inputFrame, text="None", text_font=("Tahoma Bold", 20), text_color="#EB6440")
    result.grid(column=0, row=2, sticky="N", columnspan=2, pady=30)
    
    trainInput = ctk.CTkButton(master=inputFrame, text="Choose Folder", width=150, height=40, corner_radius=10, command=askDirectory)
    trainInput.grid(column=1, row=3, sticky="N", pady=50)
    trainTitle = ctk.CTkLabel(master=inputFrame, text="Training Dataset : ", text_font="Tahoma", text_color="#0E5E6F")
    trainTitle.grid(column=0, row=3, sticky="N", pady=50)

    tesInput = ctk.CTkButton(master=inputFrame, text="Choose File", width=150, height=40, corner_radius=10, command=printImage)
    tesInput.grid(column=1, row=4, sticky="N")
    tesTitle = ctk.CTkLabel(master=inputFrame, text="Test Image : ", text_font="Tahoma", text_color="#0E5E6F")
    tesTitle.grid(column=0, row=4, sticky="N")

    faceCascade = ctk.CTkLabel(master=inputFrame, text="Face Cascade : ", text_font="Tahoma", text_color="#0E5E6F")
    faceCascade.grid(column=0, row=6, sticky="N", pady = 50)
    TrueButton = ctk.CTkButton(master=inputFrame, text="Yes", width=40, height=35, text_font=("Tahoma", 8), corner_radius=10, command=TrueCascade)
    TrueButton.grid(column=1, row=6, sticky="N", pady = 50)
    FalseButton = ctk.CTkButton(master=inputFrame, text="No", width=40, height=35, text_font=("Tahoma", 8), corner_radius=10, command=FalseCascade)
    FalseButton.grid(column=2, row=6, sticky="N", pady = 50)

    computeButton = ctk.CTkButton(master=inputFrame, text="Compute", width=200, height=60, text_font=("Tahoma", 15), corner_radius=10, command=computeResult)
    computeButton.grid(column=0, row=7, columnspan=2, pady=10)

def page3():
    global showFrame
    global tesImage
    global result
    global resultImage

    homeFrameMain.destroy()

    imageFrameMain = ctk.CTkFrame(master=root, width=1280, height=720, fg_color="#ffefd6", corner_radius=0)
    imageFrameMain.grid()

    # ShowFrame section

    emptyImage = ImageTk.PhotoImage(Image.open(".\Data\empty-256x256.png"))

    showFrame = ctk.CTkFrame(master=imageFrameMain, fg_color="#3A8891", corner_radius=0)
    showFrame.grid(column=0, row=0, sticky="")

    tesShowTitle = ctk.CTkLabel(master=showFrame, text="Test Image", text_font=("Inter Bold", 15))
    tesShowTitle.grid(column=0, row=0, sticky="E",padx=20)
    tesImage = ctk.CTkLabel(master=showFrame, image=emptyImage, fg_color="#cfcfcf")
    tesImage.grid(column=1, row=0, sticky="E", pady= 60, padx=50)

    resultShowTitle = ctk.CTkLabel(master=showFrame, text="Closest\n Result", text_font=("Inter Bold", 15))
    resultShowTitle.grid(column=0,row=1, sticky="E",padx=20)
    resultImage = ctk.CTkLabel(master=showFrame, image=emptyImage, fg_color="#cfcfcf")
    resultImage.grid(column=1, row=1, sticky="E",pady=50, padx=50)

    # inputFrame section

    inputFrame = ctk.CTkFrame(master=imageFrameMain ,fg_color="#ffefd6", corner_radius=0)
    inputFrame.grid(column=1, row=0, sticky="W N", padx=170)

    titlePage = ctk.CTkLabel(master=inputFrame, text="Input from Camera", text_font=("Tahoma",18), text_color="#0E5E6F")
    titlePage.grid(column=0, row=0, sticky="N", columnspan=2, pady=50, padx=100)
    resultTitle = ctk.CTkLabel(master=inputFrame, text="Result", text_font=("Tahoma Bold", 30), text_color="#0E5E6F")
    resultTitle.grid(column=0, row=1, sticky="N", columnspan=2, pady=30)

    result = ctk.CTkLabel(master=inputFrame, text="None", text_font=("Tahoma Bold", 20), text_color="#EB6440")
    result.grid(column=0, row=2, sticky="N", columnspan=2, pady=30)

    # ________________ BUTTON ________________

    trainInput = ctk.CTkButton(master=inputFrame, text="Choose Folder", width=150, height=40, corner_radius=10, command=askDirectory)
    trainInput.grid(column=1, row=3, sticky="N", pady=50)
    trainTitle = ctk.CTkLabel(master=inputFrame, text="Training Dataset : ", text_font="Tahoma", text_color="#0E5E6F")
    trainTitle.grid(column=0, row=3, sticky="N", pady=50)

    tesInput = ctk.CTkButton(master=inputFrame, text="Open Camera", width=150, height=40, corner_radius=10, command=capture)
    tesInput.grid(column=1, row=4, sticky="N")
    tesTitle = ctk.CTkLabel(master=inputFrame, text="Capture Test Image : ", text_font="Tahoma", text_color="#0E5E6F")
    tesTitle.grid(column=0, row=4, sticky="N")

    tipText = ctk.CTkLabel(master=inputFrame, text="The camera takes the picture every 10 seconds. Do not use mask.", text_color="black")
    tipText.grid(column=0, row=5, columnspan=2, pady=30)

    faceCascade = ctk.CTkLabel(master=inputFrame, text="Face Cascade : ", text_font="Tahoma", text_color="#0E5E6F")
    faceCascade.grid(column=0, row=6, sticky="N", pady = 5)
    TrueButton = ctk.CTkButton(master=inputFrame, text="Yes", width=40, height=35, text_font=("Tahoma", 8), corner_radius=10, command=TrueCascade)
    TrueButton.grid(column=1, row=6, sticky="N", pady = 5)
    FalseButton = ctk.CTkButton(master=inputFrame, text="No", width=40, height=35, text_font=("Tahoma", 8), corner_radius=10, command=FalseCascade)
    FalseButton.grid(column=2, row=6, sticky="N", pady = 5)

def home():
    global homeFrameMain
        
    """ Page """
    homeFrameMain = tk.Frame(root, width=1280, height=720,bg="#ffefd6" )
    homeFrameMain.pack()

    buttonFrame = tk.Frame(homeFrameMain, padx=100, pady=0, bg="#ffefd6")
    buttonFrame.grid(column=1, row=0, sticky="N", pady=450)

    """ Button """

    imageButton = ctk.CTkButton(master=buttonFrame, text="Image", text_font=("Tahoma", 17), width=200, height=50, corner_radius=10, fg_color="#3A8891", command=page2) 
    cameraButton = ctk.CTkButton(master=buttonFrame, text="Camera", text_font=("Tahoma", 17), width=200, height=50, corner_radius=10, fg_color="#3A8891", command=page3) 

    imageButton.grid(column=0, row=0, pady=30)
    cameraButton.grid(column=0, row=1)

    creditFrame = ctk.CTkFrame(master=homeFrameMain, fg_color="#ffefd6")
    creditFrame.grid(column=1, row=0, sticky="N", pady=100)

    """ Label """
    namaFrame = tk.Frame(homeFrameMain, padx=260,pady=310, bg="#3A8891")
    namaFrame.grid(column=0, row=0, sticky="W N")

    namaKel = tk.Label(namaFrame, text="BosenTuru", font=("Tahoma Bold", 50), bg="#3A8891", fg="#ffefd6")
    namaKel.grid(column=0, row=0, sticky="W")

    namaSoft = tk.Label(namaFrame, text="a face recognition program", font=("Tahoma", 20), bg="#3A8891", fg="#ffefd6")
    namaSoft.grid(column=0, row=1, sticky="W")

    creditTitle = ctk.CTkLabel(master=creditFrame,corner_radius=10, fg_color="white", text_color="grey", text="\n This face recognition sofware is made for    \nfullfiling the linear algebra and geometry   \n course grand assignment. Credit due to BosenTuru\ngroup of Bandung Institue of Technology \n \n- Naufal Syifa Firdaus (13521050) \n- Daniel Egiant Sitanggang (13521056)\n- Razzan Daksana Yoni (13521087)\n", text_font=("Arial", 10))
    creditTitle.grid(column=0, row=0)
    
home()
""" Main Program """

root.mainloop()