import customtkinter as ctk
from backend.man import action_here, select_file

app = ctk.CTk()
app.title("FFormat")
app.geometry("500x500")

ButtonSelect = ctk.CTkButton(app, text="Select", command=select_file)

ButtonUpload = ctk.CTkButton(app, text="Upload", command=action_here, fg_color="green")
ButtonUpload.pack()

app.mainloop()