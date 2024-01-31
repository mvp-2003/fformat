from customtkinter import filedialog

def choose_folder(selected_folder_name):
    folder = filedialog.askdirectory()
    selected_folder_name.configure(text = folder)

def savefile():
    pass