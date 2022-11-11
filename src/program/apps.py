""" Program GUI Apps """
import tkinter as tk
import customtkinter as ctk

# from data_processing import *
# from eigen import *


root = tk.Tk()

"""" Configure Gridv"""
root.title("BosenTuru") #title window
root.geometry("1280x720") # window size
root.configure(bg="#ffefd6")

def home():
        
    """ Page """
    homeFrameMain = tk.Frame(root, width=1280, height=720,bg="#ffefd6" )
    homeFrameMain.pack()


    buttonFrame = tk.Frame(homeFrameMain, padx=100, pady=0, bg="#ffefd6")
    buttonFrame.grid(column=1, row=0, sticky="N", pady=450)

    """ Button """

    imageButton = ctk.CTkButton(master=buttonFrame, text="Image", text_font=("Tahoma", 17), width=200, height=50, corner_radius=10, fg_color="#3A8891") 
    cameraButton = ctk.CTkButton(master=buttonFrame, text="Camera", text_font=("Tahoma", 17), width=200, height=50, corner_radius=10, fg_color="#3A8891") 

    imageButton.grid(column=0, row=0, pady=30)
    cameraButton.grid(column=0, row=1)

    creditFrame = ctk.CTkFrame(master=homeFrameMain, width=100, height=200,fg_color="white" )
    creditFrame.grid(column=1, row=0, sticky="N", pady=100)

    """ Label """
    namaFrame = tk.Frame(homeFrameMain, padx=260,pady=310, bg="#3A8891")
    namaFrame.grid(column=0, row=0, sticky="W N")

    namaKel = tk.Label(namaFrame, text="BosenTuru", font=("Tahoma Bold", 50), bg="#3A8891", fg="#ffefd6")
    namaKel.grid(column=0, row=0, sticky="W")

    namaSoft = tk.Label(namaFrame, text="a face recognition program", font=("Tahoma", 20), bg="#3A8891", fg="#ffefd6")
    namaSoft.grid(column=0, row=1, sticky="W")



home()
""" Main Program """


root.mainloop()