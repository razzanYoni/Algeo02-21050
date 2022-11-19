import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image


root = tk.Tk()
root.title("BosenTuru") #title window
root.geometry("1280x720")
root.configure(bg="#ffefd6")

def printImage():
    global inputDir

    inputDir =filedialog.askopenfilename()
    imageTes = ImageTk.PhotoImage(Image.open(inputDir))
    # lbl = ctk.CTkLabel(master=showFrame, image=imageTes)
    # lbl.grid()
    tesImage.image = imageTes
    tesImage.configure(image=imageTes)


imageFrameMain = tk.Frame(master=root, width=1280, height=720, bg="#ffefd6")
imageFrameMain.grid()

#imageFrameMain.columnconfigure([0,1], weight=1)

# ShowFrame section

emptyImage = ImageTk.PhotoImage(Image.open("..\empty-256x256.png"))

showFrame = tk.Frame(master=imageFrameMain, bg="#3A8891")
showFrame.grid(column=0, row=0, sticky="")

tesShowTitle = tk.Label(master=showFrame, text="Test Image", font=("Inter Bold", 15))
tesShowTitle.grid(column=0, row=0, sticky="E",padx=20)
tesImage = tk.Label(master=showFrame, image=emptyImage)
tesImage.grid(column=1, row=0, sticky="E", pady= 60, padx=50)


resultShowTitle = tk.Label(master=showFrame, text="Closest\n Result", font=("Inter Bold", 15))
resultShowTitle.grid(column=0,row=1, sticky="E",padx=20)
resultImage = tk.Label(master=showFrame, image=emptyImage)
resultImage.grid(column=1, row=1, sticky="E",pady=50, padx=50)



# inputFrame section


inputFrame = tk.Frame(master=imageFrameMain ,bg="#ffefd6")
inputFrame.grid(column=1, row=0, sticky="W N", padx=170)

titlePage = tk.Label(master=inputFrame, text="Input from Image", font=("Tahoma",18), fg="#0E5E6F")
titlePage.grid(column=0, row=0, sticky="N", columnspan=2, pady=50, padx=100)
resultTitle = tk.Label(master=inputFrame, text="Result", font=("Tahoma Bold", 30), fg="#0E5E6F")
resultTitle.grid(column=0, row=1, sticky="N", columnspan=2)



result = tk.Label(master=inputFrame, text="None", font=("Tahoma Bold", 20), fg="#EB6440")
result.grid(column=0, row=2, sticky="N", columnspan=2, pady=30)

# fileFrame = tk.Frame(master=inputFrame, )


trainInput = tk.Button(master=inputFrame, text="Choose File")
trainInput.grid(column=1, row=3, sticky="N", pady=30)
trainTitle = tk.Label(master=inputFrame, text="Training Dataset : ", font="Tahoma", fg="#0E5E6F")
trainTitle.grid(column=0, row=3, sticky="N", pady=30)

tesInput = tk.Button(master=inputFrame, text="Choose File", command=printImage)
tesInput.grid(column=1, row=4, sticky="N")
tesTitle = tk.Label(master=inputFrame, text="Test Image : ", font="Tahoma", fg="#0E5E6F")
tesTitle.grid(column=0, row=4, sticky="N")


root.mainloop()