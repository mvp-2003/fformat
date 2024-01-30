import customtkinter as ctk
from backend.light import addfile
from frontend.filedialog import selectfile
from backend.channel import convert

app = ctk.CTk()
app.title("FFormat")
app.geometry("1250x650")

entry_field = ctk.CTkEntry(app, placeholder_text = "Select a file to upload or type in the absolute path manually", width = 600, height = 30)
entry_field.pack(padx = 25, pady = 25)
entry_field.place(x = 200, y = 175)

button_to_select = ctk.CTkButton(app, text = "Choose file", fg_color = "blue", command = lambda: selectfile(entry_field))
button_to_select.pack(padx = 25, pady = 25)
button_to_select.place(x = 825, y = 175)

button_to_upload = ctk.CTkButton(app, text = "Upload", fg_color = "green", command = lambda: addfile(entry_field, file_name_label, extension_label, no_file_label))
button_to_upload.pack(padx = 25, pady = 25)
button_to_upload.place(x = 540, y = 250)

file_name_label = ctk.CTkLabel(app, text = "File selected:", font=("Arial", 16), fg_color="gray", height=30, width=300)
file_name_label.pack(padx = 25, pady = 25)
file_name_label.place(x = 360, y = 315)

file_type_label = ctk.CTkLabel(app, text = "File type:", font=("Arial", 16))
file_type_label.pack(padx = 25, pady = 25)
file_type_label.place(x = 720, y = 315)

no_file_label = ctk.CTkLabel(app, text = "", font=("Arial", 16))
no_file_label.pack(padx = 25, pady = 25)
no_file_label.place(x = 200, y = 225)

extension_label = ctk.CTkLabel(app, text = "", font=("Arial", 16), fg_color="gray", height=30, width=80)
extension_label.pack(padx = 25, pady = 25)
extension_label.place(x = 800, y = 315)

type_selection_label = ctk.CTkLabel(app, text = "Convert to:", font=("Arial", 16))
type_selection_label.pack(padx = 25, pady = 25)
type_selection_label.place(x = 500, y = 375)

types = [".jpg", ".jpeg", ".png", ".tif", ".tiff", ".svg"]
type_selection = ctk.CTkComboBox(app, values = types, width = 100, height = 30)
type_selection.pack(padx = 25, pady = 25)
type_selection.place(x = 600, y = 375)

convert_button = ctk.CTkButton(app, text = "Convert", fg_color = "green", command = lambda: convert(entry_field, type_selection))
convert_button.pack(padx = 25, pady = 25)
convert_button.place(x = 725, y = 375)

app.mainloop()