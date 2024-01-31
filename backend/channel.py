from fileinput import filename
from backend.conversions.jpeg2jpg import jpeg_to_jpg
from backend.conversions.jpg2png import jpg_to_png
from backend.conversions.png2jpg import png_to_jpg
from backend.conversions.jpg2jpeg import jpg_to_jpeg
import os


def convert(new_file_label, type_selection, file_name_label, extension_label):
    if file_name_label.cget("text") == "" and extension_label() == "":
        new_file_label.configure(text="No file selected")
    newfile = ""
    new_file_label.configure(text = newfile)