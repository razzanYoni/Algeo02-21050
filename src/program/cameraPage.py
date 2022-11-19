import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageTk,Image
import cv2 as cv


def printImage():
    global inputDir
    global tesImage

    inputDir =filedialog.askopenfilename()
    imageTes = ImageTk.PhotoImage(Image.open(inputDir))
    # lbl = ctk.CTkLabel(master=showFrame, image=imageTes)
    # lbl.grid()
    tesImage.image = imageTes
    tesImage = ctk.CTkLabel(master=showFrame, image=imageTes)
    tesImage.grid(column=1, row=0, sticky="E", pady= 60, padx=50)

def capture():
    global tesImage

    vid = cv.VideoCapture(0)
    vid.set(3, 256)

    
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
    
    
    blue,green,red = cv.split(frame)
    frame = cv.merge((red,green,blue))
    color_converted = Image.fromarray(frame)
    imageTes = ImageTk.PhotoImage(image=color_converted)

    tesImage.image = imageTes
    tesImage = ctk.CTkLabel(master=showFrame, image=imageTes)
    tesImage.grid(column=1, row=0, sticky="E", pady= 60, padx=50)
    


root = tk.Tk()
root.title("BosenTuru") #title window
root.geometry("1280x720")
root.configure(bg="#ffefd6")


imageFrameMain = ctk.CTkFrame(master=root, width=1280, height=720, fg_color="#ffefd6", corner_radius=0)
imageFrameMain.grid()

#imageFrameMain.columnconfigure([0,1], weight=1)

# ShowFrame section

emptyImage = ImageTk.PhotoImage(Image.open("..\empty-256x256.png"))

showFrame = ctk.CTkFrame(master=imageFrameMain, fg_color="#3A8891", corner_radius=0)
showFrame.grid(column=0, row=0, sticky="")

tesShowTitle = ctk.CTkLabel(master=showFrame, text="Test Image", text_font=("Inter Bold", 15))
tesShowTitle.grid(column=0, row=0, sticky="E",padx=20)
tesImage = ctk.CTkLabel(master=showFrame, image=emptyImage)
tesImage.grid(column=1, row=0, sticky="E", pady= 60, padx=50)


resultShowTitle = ctk.CTkLabel(master=showFrame, text="Closest\n Result", text_font=("Inter Bold", 15))
resultShowTitle.grid(column=0,row=1, sticky="E",padx=20)
resultImage = ctk.CTkLabel(master=showFrame, image=emptyImage)
resultImage.grid(column=1, row=1, sticky="E",pady=50, padx=50)



# inputFrame section


inputFrame = ctk.CTkFrame(master=imageFrameMain ,fg_color="#ffefd6", corner_radius=0)
inputFrame.grid(column=1, row=0, sticky="W N", padx=170)

titlePage = ctk.CTkLabel(master=inputFrame, text="Input from Image", text_font=("Tahoma",18), text_color="#0E5E6F")
titlePage.grid(column=0, row=0, sticky="N", columnspan=2, pady=50, padx=100)
resultTitle = ctk.CTkLabel(master=inputFrame, text="Result", text_font=("Tahoma Bold", 30), text_color="#0E5E6F")
resultTitle.grid(column=0, row=1, sticky="N", columnspan=2)



result = ctk.CTkLabel(master=inputFrame, text="None", text_font=("Tahoma Bold", 20), text_color="#EB6440")
result.grid(column=0, row=2, sticky="N", columnspan=2, pady=30)

# fileFrame = ctk.CTkFrame(master=inputFrame, )


trainInput = ctk.CTkButton(master=inputFrame, text="Choose File", width=150, height=40, corner_radius=10)
trainInput.grid(column=1, row=3, sticky="N", pady=30)
trainTitle = ctk.CTkLabel(master=inputFrame, text="Training Dataset : ", text_font="Tahoma", text_color="#0E5E6F")
trainTitle.grid(column=0, row=3, sticky="N", pady=30)

tesInput = ctk.CTkButton(master=inputFrame, text="Open Camera", width=150, height=40, corner_radius=10, command=capture)
tesInput.grid(column=1, row=4, sticky="N")
tesTitle = ctk.CTkLabel(master=inputFrame, text="Capture Test Image : ", text_font="Tahoma", text_color="#0E5E6F")
tesTitle.grid(column=0, row=4, sticky="N")


root.mainloop()