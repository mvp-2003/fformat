import customtkinter as ctk
import os
import sys

sys.path.insert(1, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'backend'))

from light import addfile
from upload import selectfile

app = ctk.CTk()
app.title("FFormating")
app.geometry("1250x650")

entry_field = ctk.CTkEntry(app, placeholder_text = "Select a file to upload", width = 600, height = 30)
entry_field.pack(padx = 25, pady = 25)
entry_field.place(x = 200, y = 300)

button_to_select = ctk.CTkButton(app, text = "Choose file", fg_color = "blue", command = selectfile)

button_to_upload = ctk.CTkButton(app, text = "Upload", fg_color = "green", command = addfile)
button_to_upload.pack(padx = 25, pady = 25)
button_to_upload.place(x = 540, y = 375)
app.mainloop()