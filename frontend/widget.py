import customtkinter as ctk

import os
import sys
sys.path.insert(1, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'backend'))
from light import *

app = ctk.CTk()
app.title("FFormating")
app.geometry("1200x600")

Button_to_upload = ctk.CTkButton(app, text="Upload", fg_color="green", command=addfile)
Button_to_upload.pack(padx = 25, pady = 25)

app.mainloop()