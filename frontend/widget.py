import customtkinter as ctk
from backend.light import addfile
from frontend.filedialog import selectfile

app = ctk.CTk()
app.title("FFormat")
app.geometry("1250x650")

entry_field = ctk.CTkEntry(app, placeholder_text = "Select a file to upload", width = 600, height = 30)
entry_field.pack(padx = 25, pady = 25)
entry_field.place(x = 200, y = 300)

button_to_select = ctk.CTkButton(app, text = "Choose file", fg_color = "blue", command = selectfile)
button_to_select.pack(padx = 25, pady = 25)
button_to_select.place(x = 825, y = 300)

button_to_upload = ctk.CTkButton(app, text = "Upload", fg_color = "green", command = addfile)
button_to_upload.pack(padx = 25, pady = 25)
button_to_upload.place(x = 540, y = 375)

app.mainloop()