""" Program GUI Apps """
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageTk,Image
import cv2 as cv
import numpy as np

# from data_processing import *
from eigen import *


root = tk.Tk()

"""" Configure Gridv"""
root.title("BosenTuru") #title window
root.geometry("1280x720") # window size
root.configure(bg="#ffefd6")

def computeResult():
    global resultImage

    nama, pathRes = getResultEigenFaceFromImageFile(direc, inputDir)
    
    # blue,green,red = cv.split(photo)
    # photo = cv.merge((red,green,blue))
    # colorConv = Image.fromarray(photo)
    img = Image.open(pathRes)
    imageSized = img.resize((256, 256))
    imageRes = ImageTk.PhotoImage(imageSized)
    resultImage.image = imageRes
    resultImage.configure(image=imageRes)
    # resultImage = ctk.CTkLabel(master=showFrame, image=resultImage)
    # resultImage.grid(column=1, row=1, sticky="E",pady=50, padx=50)
    
    result.configure(text=nama, text_color="green")

def computeCamera():
    global resultImage

    photo, nama, pathRes = getEigenFaceFromCamera(direc, framearr)
    
    # blue,green,red = cv.split(photo)
    # photo = cv.merge((red,green,blue))
    # colorConv = Image.fromarray(photo)
    img = Image.open(pathRes)
    imageSized = img.resize((256, 256))
    imageRes = ImageTk.PhotoImage(imageSized)
    resultImage.image = imageRes
    resultImage.configure(image=imageRes)
    # resultImage = ctk.CTkLabel(master=showFrame, image=resultImage)
    # resultImage.grid(column=1, row=1, sticky="E",pady=50, padx=50)
    
    result.configure(text=nama, text_color="green")

def capture():
    global tesImage
    global framearr

    vid = cv.VideoCapture(0)
    #vid.set(3, 256)

    
    while(True):
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
    
        # Display the resulting frame
        cv.imshow('frame', frame)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv.waitKey(1) & 0xFF == ord(' '):
            vid.release()
            cv.destroyAllWindows()
            cv.imshow('image', frame)
            cv.waitKey(0)
            break


    framearr = np.array(frame)

    blue,green,red = cv.split(frame)
    frame_split = cv.merge((red,green,blue))
    color_converted = Image.fromarray(frame_split)

    image_resized = color_converted.resize((256,256))

    imageTes = ImageTk.PhotoImage(image=image_resized)
    tesImage.image = imageTes
    tesImage = ctk.CTkLabel(master=showFrame, image=imageTes)
    tesImage.grid(column=1, row=0, sticky="E", pady= 60, padx=50)

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
    # lbl = ctk.CTkLabel(master=showFrame, image=imageTes)
    # lbl.grid()
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

    #imageFrameMain.columnconfigure([0,1], weight=1)

    # ShowFrame section

    emptyImage = ImageTk.PhotoImage(Image.open("..\empty-256x256.png"))

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

    # fileFrame = ctk.CTkFrame(master=inputFrame, )


    trainInput = ctk.CTkButton(master=inputFrame, text="Choose Folder", width=150, height=40, corner_radius=10, command=askDirectory)
    trainInput.grid(column=1, row=3, sticky="N", pady=50)
    trainTitle = ctk.CTkLabel(master=inputFrame, text="Training Dataset : ", text_font="Tahoma", text_color="#0E5E6F")
    trainTitle.grid(column=0, row=3, sticky="N", pady=50)

    tesInput = ctk.CTkButton(master=inputFrame, text="Choose File", width=150, height=40, corner_radius=10, command=printImage)
    tesInput.grid(column=1, row=4, sticky="N")
    tesTitle = ctk.CTkLabel(master=inputFrame, text="Test Image : ", text_font="Tahoma", text_color="#0E5E6F")
    tesTitle.grid(column=0, row=4, sticky="N")

    computeButton = ctk.CTkButton(master=inputFrame, text="Compute", width=200, height=60, text_font=("Tahoma", 15), corner_radius=10, command=computeResult)
    computeButton.grid(column=0, row=5, columnspan=2, pady=80)

def page3():
    global showFrame
    global tesImage
    global result
    global resultImage

    homeFrameMain.destroy()

    imageFrameMain = ctk.CTkFrame(master=root, width=1280, height=720, fg_color="#ffefd6", corner_radius=0)
    imageFrameMain.grid()

    #imageFrameMain.columnconfigure([0,1], weight=1)

    # ShowFrame section

    emptyImage = ImageTk.PhotoImage(Image.open("..\empty-256x256.png"))

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

    titlePage = ctk.CTkLabel(master=inputFrame, text="Input from Image", text_font=("Tahoma",18), text_color="#0E5E6F")
    titlePage.grid(column=0, row=0, sticky="N", columnspan=2, pady=50, padx=100)
    resultTitle = ctk.CTkLabel(master=inputFrame, text="Result", text_font=("Tahoma Bold", 30), text_color="#0E5E6F")
    resultTitle.grid(column=0, row=1, sticky="N", columnspan=2, pady=30)



    result = ctk.CTkLabel(master=inputFrame, text="None", text_font=("Tahoma Bold", 20), text_color="#EB6440")
    result.grid(column=0, row=2, sticky="N", columnspan=2, pady=30)

    # fileFrame = ctk.CTkFrame(master=inputFrame, )

    # ________________ BUTTON ________________

    trainInput = ctk.CTkButton(master=inputFrame, text="Choose Folder", width=150, height=40, corner_radius=10, command=askDirectory)
    trainInput.grid(column=1, row=3, sticky="N", pady=50)
    trainTitle = ctk.CTkLabel(master=inputFrame, text="Training Dataset : ", text_font="Tahoma", text_color="#0E5E6F")
    trainTitle.grid(column=0, row=3, sticky="N", pady=50)

    tesInput = ctk.CTkButton(master=inputFrame, text="Open Camera", width=150, height=40, corner_radius=10, command=capture)
    tesInput.grid(column=1, row=4, sticky="N")
    tesTitle = ctk.CTkLabel(master=inputFrame, text="Capture Test Image : ", text_font="Tahoma", text_color="#0E5E6F")
    tesTitle.grid(column=0, row=4, sticky="N")

    tipText = ctk.CTkLabel(master=inputFrame, text="Place your head in the middle dan press SPACE to capture. Do not use mask.", text_color="black")
    tipText.grid(column=0, row=5, columnspan=2, pady=30)

    computeButton = ctk.CTkButton(master=inputFrame, text="Compute", width=200, height=60, text_font=("Tahoma", 15), corner_radius=10, command=computeCamera)
    computeButton.grid(column=0, row=6, columnspan=2, pady=0)



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