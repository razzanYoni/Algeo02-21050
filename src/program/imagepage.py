import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from PIL import ImageTk,Image



def askDirectory(self):
    
    return filedialog.askdirectory(**self.dir_opt)


def print():
    l = tk.Label(inputFrame, text="Halo")
    l.grid()


root = tk.Tk()
root.title("BosenTuru") #title window
root.geometry("1280x720")
root.configure(bg="#ffefd6")

imageFrameMain = ctk.CTkFrame(master=root, width=1280, height=720, fg_color="#ffefd6", corner_radius=0)
imageFrameMain.grid()

# ShowFrame section

emptyImage = ImageTk.PhotoImage(Image.open("..\empty-256x256.png"))

showFrame = ctk.CTkFrame(master=imageFrameMain, width=500, height=720, fg_color="#3A8891", corner_radius=0)
showFrame.grid(column=0, row=0, sticky="")

tesShowTitle = ctk.CTkLabel(master=showFrame, text="Test Image")
tesShowTitle.grid(column=0, row=0, sticky="E")
tesImage = ctk.CTkLabel(master=showFrame, image=emptyImage)
tesImage.grid(column=1, row=0, sticky="E")


resultShowTitle = ctk.CTkLabel(master=showFrame, text="Closest Result")
resultShowTitle.grid(column=0,row=1, sticky="E")
resultImage = ctk.CTkLabel(master=showFrame, image=emptyImage)
resultImage.grid(column=1, row=1, sticky="E")



# inputFrame section


inputFrame = ctk.CTkFrame(master=imageFrameMain, height=720, fg_color="blue", corner_radius=0)
inputFrame.grid(column=1, row=0, sticky="W N")

titlePage = ctk.CTkLabel(master=inputFrame, text="Input from Image")
titlePage.grid(column=0, row=0, sticky="N", columnspan=2)

resultTitle = ctk.CTkLabel(master=inputFrame, text="Result")
resultTitle.grid(column=0, row=1, sticky="N", columnspan=2)

result = ctk.CTkLabel(master=inputFrame, text="None", text_color="#EB6440")
result.grid(column=0, row=2, sticky="N", columnspan=2)




trainInput = ctk.CTkButton(master=inputFrame, text="Choose File")
trainInput.grid(column=1, row=3, sticky="N", pady=30)
trainTitle = ctk.CTkLabel(master=inputFrame, text="Training Dataset : ")
trainTitle.grid(column=0, row=3, sticky="N", pady=30)

tesInput = ctk.CTkButton(master=inputFrame, text="Choose File")
tesInput.grid(column=1, row=4, sticky="N")
tesTitle = ctk.CTkLabel(master=inputFrame, text="Test Image : ")
tesTitle.grid(column=0, row=4, sticky="N")





root.mainloop()