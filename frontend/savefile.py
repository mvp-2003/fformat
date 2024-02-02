import os
import shutil
from customtkinter import filedialog

def choose_folder(selected_folder_name):
    folder = filedialog.askdirectory()
    selected_folder_name.configure(text=folder)

def savefile(new_file_label, saved_file_label, type_selection):
    filex = filedialog.asksaveasfilename(defaultextension = type_selection.get())