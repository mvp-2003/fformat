import os
import shutil
from tkinter import filedialog

def savefile(new_file_label, saved_file_label, extension_label):
    file = new_file_label.cget("text")
    if file == "New file:":
        saved_file_label.configure(text="No file to save", text_color="red")
    else:
        new_file_path = filedialog.asksaveasfilename(defaultextension=extension_label.cget("text"), filetypes=[("All Files", "*.*")])
        if new_file_path:
            file = os.path.normpath(file)
            new_file_path = os.path.normpath(new_file_path)
            try:
                shutil.move(file, new_file_path)
                saved_file_label.configure(text=f"File saved at {new_file_path}")
            except Exception as e:
                print(f"An error occurred: {e}")
                saved_file_label.configure(text=f"An error occurred: {e}", fg="red")