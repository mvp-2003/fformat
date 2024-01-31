from backend.conversions.jpeg2jpg import jpeg_to_jpg
from backend.conversions.jpg2png import jpg_to_png
from backend.conversions.png2jpg import png_to_jpg
from backend.conversions.jpg2jpeg import jpg_to_jpeg
import os


def convert(entry_field, type_selection, new_file_label):
    filepath = entry_field.get()
    typec = type_selection.get()
    filename, extension = os.path.splitext(os.path.basename(filepath))
    newfile = ""

    if typec == ".jpg" and extension == ".jpeg":
        newfile = jpeg_to_jpg(entry_field)

    elif typec == ".jpeg" and extension == ".jpg":
        newfile = jpg_to_jpeg(entry_field)

    elif typec == ".jpg" and extension == ".png":
        newfile = jpg_to_png(entry_field)

    elif typec == ".png" and extension == ".jpg":
        newfile = png_to_jpg(entry_field, filename, new_file_label)

    '''elif typec == ".jpeg" and extension == ".png":
        newfile = jpeg_to_png(filename, extension)'''


    new_file_label.configure(text = newfile)