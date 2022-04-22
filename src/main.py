# Group 3: Daniel Gertz, Jacob Yang, Patrick Marsh, Mikey Plaut, Zach Hillman
# Vision++ : Simple Video Editing Software

from moviepy.editor import *
import tkinter as tk
from tkinter import filedialog

from moviepy.config import change_settings
change_settings({"IMAGEMAGIC_BINARY": r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\\magick.exe"})

def open_dialog():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select your Files", filetypes = [('All files', '*.mp4')])
    print(filename) #This will be where we will add functionality, after importing a file

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Vision++")
    root.geometry("1280x760")
    root.minsize(1280,760)
    root.maxsize(1280,760)

    #Import Button
    importButton = tk.Button(root, text = "Import", font=("Arial", 18), padx = 10, pady = 10, fg = "#FFF", bg = "#3528e8", command = open_dialog)
    importButton.grid(sticky = "W", column = 0, row = 0, padx = 10, pady = 10)

    root.mainloop()