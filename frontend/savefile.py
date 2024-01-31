import os
from shutil import copyfile
from customtkinter import filedialog

def choose_folder(selected_folder_name):
    folder = filedialog.askdirectory()
    selected_folder_name.configure(text=folder)

def savefile(selected_folder, filename, saved_file_label):
    """
    Save the file with the given filename in the selected folder.
    
    Parameters:
        selected_folder (str): The path of the folder where the file should be saved.
        filename (str): The name of the file to be saved.
        saved_file_label (tkinter.Label): The label widget to display the saved file path.
    
    Returns:
        str: The path of the saved file if successful, None otherwise.
    """
    try:
        # Construct the destination filepath in the selected folder
        destination = os.path.join(selected_folder, filename)
        # Copy the file to the selected folder
        copyfile(filename, destination)
        
        saved_file_label.config(text=f"File saved to: {destination}")
        return destination
    except Exception as e:
        print(f"Error saving file: {e}")
        return None
