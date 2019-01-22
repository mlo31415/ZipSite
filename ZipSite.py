from tkinter import Tk
from tkinter.filedialog import askdirectory
import zipfile
import os

#---------------------------------------------------------------
# Main
# Ask for the root directory
root = Tk()
root.filename =  askdirectory(initialdir = ".",title = "Choose the Root Directory")
root.withdraw()
dirname=root.filename

if len(dirname) == 0:
    exit(0)

zip=zipfile.ZipFile("site.zip", "w", zipfile.ZIP_DEFLATED)

dirlist=os.listdir(dirname)
for file in dirlist:
    if os.path.isdir(file):
        continue

    zip.write(os.path.join(dirname, file))

