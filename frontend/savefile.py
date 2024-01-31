import os
from shutil import copyfile
from customtkinter import filedialog

def choose_folder(selected_folder_name):
    folder = filedialog.askdirectory()
    selected_folder_name.configure(text=folder)
    return folder

def savefile(selected_folder, filepath):
    """
    Save the file located at 'filepath' to the 'selected_folder'.
    
    Parameters:
        selected_folder (str): The path of the folder where the file should be saved.
        filepath (str): The path of the file to be saved.
    
    Returns:
        str: The path of the saved file if successful, None otherwise.
    """
    try:
        # Check if the selected folder exists, if not, create it
        if not os.path.exists(selected_folder):
            os.makedirs(selected_folder)
        
        # Get the filename from the filepath
        filename = os.path.basename(filepath)
        # Construct the destination filepath in the selected folder
        destination = os.path.join(selected_folder, filename)
        # Copy the file to the selected folder
        copyfile(filepath, destination)
        
        print(f"File saved to: {destination}")
        return destination
    except Exception as e:
        print(f"Error saving file: {e}")
        return None
