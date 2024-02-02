from backend.conversions import *
import os

def convert(entry_field, file_name_label, type_selection, extension_label):
    if file_name_label.cget("text") == "File selected:":
        file_name_label.configure(text="No file selected", text_color="red")
    
    elif extension_label.cget("text") == type_selection.cget("text"):
        file_name_label.configure(text="File already in this format", text_color="red")