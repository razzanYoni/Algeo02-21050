import tkinter as tk
import cv2 as cv
import os
from pathlib import Path

""" Baca Path melalui input """
# path_to_directory = Path(input("enter the path to the folder : "))

# extension_of_interest = ".jpg"
# filepaths_of_interest = []

# for entry in path_to_directory.iterdir():
#     if entry.is_file() and entry.name.endswith(extension_of_interest):
#         print("match: " + str(entry))
#         filepaths_of_interest.append(entry)
#     else:
#         print("ignored: " + str(entry))

# print("now opening ...")
# for filepath_of_interest in filepaths_of_interest:
#     os.startfile(filepath_of_interest, "open")


""" Baca Path melalui GUI/File Explorer """
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

files = filedialog.askopenfilenames() # baca file dari file explorer

import sys
path = r'Dummy aja'
sys.path.append(path)
print(sys.path)

# import subprocess
# subprocess.Popen('explorer "C:\temp"')

print(files)
img = cv.imread(files[0])

cv.imshow('image', img)

cv.waitKey(0)
  
""" Video Secara Realtime tinggal tambahin fitur capture untuk moto """
# define a video capture object
vid = cv.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv.waitKey(1) & 0xFF == ord('q'):
        vid.release()
        cv.destroyAllWindows()
        cv.imshow('image', frame)
        cv.waitKey(0)
        break
# After the loop release the cap object

# Destroy all the windows

filename = input("Masukkan nama file: ")
cv.imwrite(f'./Photo/{filename}.jpg', frame) # save gambar berarti perlu count gambar di folder biar ga overwrite

