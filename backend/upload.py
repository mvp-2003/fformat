import os
import sys
from tkinter import filedialog

sys.path.insert(1, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend'))
from widget import entry_field

def selectfile():
    # This function is called when the user clicks the "Choose file" button
    pass