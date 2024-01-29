from frontend.widget import extension_field, entry_field
from backend.light import addfile

def fill_box():
    message = addfile(entry_field)
    extension_field.insert(0, message)