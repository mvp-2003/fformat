from cgitb import text
import os
import shutil
from tkinter import filedialog

def savefile(new_file_label, saved_file_label):
    file = new_file_label.cget("text")
    if file == "New file:":
        saved_file_label.configure(text="No file to save", text_color="red")
    else:
        folder = filedialog.askdirectory()
        print(f"File: {file}")
        print(f"Folder: {folder}")
        file = os.path.normpath(file)
        folder = os.path.normpath(folder)

        try:
            shutil.move(file, folder)
            saved_file_label.configure(text=f"File saved at {folder}")
        except Exception as e:
            print(f"An error occurred: {e}")
            saved_file_label.configure(text=f"An error occurred: {e}")