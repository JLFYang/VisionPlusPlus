# Group 3: Daniel Gertz, Jacob Yang, Patrick Marsh, Mikey Plaut, Zach Hillman
# Vision++ : Simple Video Editing Software

from moviepy.editor import *
import tkinter as tk
from tkinter import filedialog
from tkinter import Menu

from moviepy.config import change_settings
change_settings({"IMAGEMAGIC_BINARY": r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\\magick.exe"})

class GUI(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.gui = self.configure_gui()
        self.bar = self.configure_bar()
        self.importedFiles = []

    def configure_gui(self):
        self.master.geometry("1280x760")
        self.master.minsize(1280,760)
        self.master.maxsize(1280,760)

    def configure_bar(self):
        menuBar = Menu(self.master, foreground='black')
        fileMenu = Menu(menuBar, tearoff=False)
        fileMenu.add_command(label="Import", command=self.importFile)
        fileMenu.add_command(label="Export")
        menuBar.add_cascade(label="File",menu=fileMenu)

        functionMenu = Menu(menuBar, tearoff=False)
        functionMenu.add_command(label="Trim")
        functionMenu.add_command(label="Cut")
        menuBar.add_cascade(label="Functions", menu=functionMenu)

        self.master.config(menu=menuBar)

    def importFile(self):
        self.master.filename = filedialog.askopenfilename(initialdir = "/", title = "Select your Files", filetypes = [('All files', '*.mp4')])
        # if self.master.filename is not None:
        #     file = VideoFile(self.master.filename)
        #     self.importedFiles.append(file)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Vision++")

    app = GUI(root)
    root.mainloop()