import os

def addfile(entry_field, extension_label):
    filepath = entry_field.get()
    entry_field.delete(0, 'end')
    extension = os.path.splitext(filepath)[1]
    extension_label.configure(text = extension)