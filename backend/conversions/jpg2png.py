from PIL import Image

def jpg_to_png(entry_field):
    image = Image.open(entry_field)
    if image.mode != "RGB":
        image = image.convert("RGB")
    nfile = image.save(entry_field+".png", "PNG")