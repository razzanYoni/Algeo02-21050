import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
# import PIL



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

showFrame = ctk.CTkFrame(master=imageFrameMain, width=500, height=720, fg_color="#3A8891", corner_radius=0)
showFrame.grid(column=0, row=0, sticky="")


# inputFrame section


inputFrame = ctk.CTkFrame(master=imageFrameMain, height=720, fg_color="blue", corner_radius=0)
inputFrame.grid(column=1, row=0, sticky="W N")

titlePage = ctk.CTkLabel(master=inputFrame, text="Input from Image")
titlePage.grid(column=0, row=0, sticky="N")

resultTitle = ctk.CTkLabel(master=inputFrame, text="Result")
resultTitle.grid(column=0, row=1, sticky="N")

result = ctk.CTkLabel(master=inputFrame, text="None", text_color="#EB6440")
result.grid(column=0, row=2, sticky="N")


trainInput = ctk.CTkButton(master=inputFrame, text="Choose File", command=askDirectory)
trainInput.grid(column=0, row=3, sticky="N")



root.mainloop()