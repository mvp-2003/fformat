from fileinput import filename
from backend.conversions.jpeg2jpg import jpeg_to_jpg
from backend.conversions.jpg2png import jpg_to_png
from backend.conversions.png2jpg import png_to_jpg
from backend.conversions.jpg2jpeg import jpg_to_jpeg
import os

def convert(new_file_label, type_selection, file_name_label, extension_label, entry_field):
    newfile = ""
    if file_name_label.cget("text") == "" or extension_label.cget("text") == "":
        new_file_label.configure(text="No file selected / uploaded", text_color="red")

    elif extension_label.cget("text") == type_selection.get():
            new_file_label.configure(text="File already in this format", text_color="red")
    else:
        if extension_label.cget("text") == ".jpg" and type_selection.get() == ".jpeg":
            newfile = jpg_to_jpeg(file_name_label)

        elif extension_label.cget("text") == ".jpeg" and type_selection.get() == ".jpg":
            newfile = jpeg_to_jpg(file_name_label)

        elif extension_label.cget("text") == ".jpg" and type_selection.get() == ".png":
            newfile = jpg_to_png(entry_field)
        new_file_label.configure(text=newfile, text_color="black")