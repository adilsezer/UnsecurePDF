import pikepdf
import os
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
dirpath = filedialog.askdirectory()

for filename in os.listdir(dirpath):
    if filename.lower().endswith(".pdf"):
        os.rename(dirpath + "/" + filename, dirpath + "/Old-" + filename)
        with pikepdf.open(dirpath + "/Old-" + filename) as pdf:
            pdf.save(dirpath + "/" + filename)
        os.remove(dirpath + "/Old-" + filename)
