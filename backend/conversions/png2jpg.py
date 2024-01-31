from PIL import Image

def png_to_jpg(entry_field, filename, new_file_label):
    image = Image.open(entry_field.get())
    image = image.convert('RGB')
    image.save(filename + ".jpg")
    new_file_label.configure(text = filename + ".jpg")
