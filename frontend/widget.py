import customtkinter as ctk
from backend.light import addfile


ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("FFormating")
app.geometry("1200x600")

Button_to_upload = ctk.CTkButton(app, text="Upload", fg_color="green", command=addfile)
Button_to_upload.pack(padx = 25, pady = 25)

app.mainloop()