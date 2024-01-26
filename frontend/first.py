import customtkinter as ctk
from backend.man import action_here
app = ctk.CTk()
app.title("FFormat")
app.geometry("500x500")

button = ctk.CTkButton(app, text="Click me", command=action_here)
button.pack()

app.mainloop()