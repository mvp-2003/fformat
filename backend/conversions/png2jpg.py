from PIL import Image

def png_to_jpg(file_name_label):
    image = Image.open(file_name_label)
    if image.mode != "RGB":
        image = image.convert("RGB")

    nfile = image.save(file_name_label+".jpg", "JPEG")
    return nfile