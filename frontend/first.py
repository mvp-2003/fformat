import customtkinter as ctk
from backend.man import select_file, action_here

app = ctk.CTk()
app.title("FFormat")
app.geometry("500x500")

ButtonSelect = ctk.CTkButton(app, text="Select", fg_color="blue", command=select_file)

ButtonUpload = ctk.CTkButton(app, text="Upload", fg_color="green", command=action_here)
ButtonUpload.pack()

app.mainloop()