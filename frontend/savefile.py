import os
import shutil
from customtkinter import filedialog

def choose_folder(selected_folder_name):
    folder = filedialog.askdirectory()
    selected_folder_name.configure(text=folder)

def savefile(selected_folder, new_file_label, saved_file_label):
    filename = new_file_label.cget("text")
    folder = selected_folder.cget("text")
    source_path = os.path.join(folder, filename)
    destination_path = os.path.join(os.getcwd(), filename)
    shutil.copyfile(source_path, destination_path)
    saved_file_label.configure(text=f"File saved to {destination_path}", text_color="green")