import os
from tkinter import font

def addfile(entry_field, extension_label, no_file_label):
    filepath = entry_field.get()
    if(filepath == ""):
        no_file_label.configure(text = "No file selected", text_color = "red", font=("Ariel", 16))
    entry_field.delete(0, 'end')
    extension = os.path.splitext(filepath)[1]
    extension_label.configure(text = extension)