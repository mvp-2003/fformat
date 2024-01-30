'''from backend.conversions.jpeg2jpg import jpeg_to_jpg
from backend.conversions.jpg2png import jpg_to_png
from backend.conversions.png2jpg import png_to_jpg
from backend.conversions.jpg2jpeg import jpg_to_jpeg'''
import os

def convert(entry_field, type_selection):
    filepath = entry_field.get()
    typec = type_selection.get()
    name = os.path.splitext(filepath)[0]

    if typec == ".jpg":
        # jpeg_to_jpg()
        pass