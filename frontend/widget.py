import customtkinter as ctk
import fetch

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("FFormating")
app.geometry("1200x600")

Button_to_upload = ctk.CTkButton(app, text="Upload", fg_color="green", command=fetch.getinput)
Button_to_upload.pack(padx = 25, pady = 25)

app.mainloop()