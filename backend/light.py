import os

def addfile(entry_field, file_name_label, extension_label, no_file_label):
    filepath = entry_field.get()
    if(filepath == ""):
        no_file_label.configure(text = "No file selected", text_color = "red", font=("Ariel", 16))
    else:
        file_name_with_extension = os.path.basename(filepath)
        file_name, extension = os.path.splitext(file_name_with_extension)
        file_name_label.configure(text = file_name)
        extension_label.configure(text = extension)
        entry_field.delete(0, "end")
        no_file_label.configure(text = "")