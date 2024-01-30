from customtkinter import filedialog

def savefile(entry_field, file_name_label, extension_label, no_file_label):
    folder = filedialog.askdirectory()
    