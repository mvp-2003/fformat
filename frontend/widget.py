import customtkinter as ctk
from backend.light import addfile
from frontend.filedialog import selectfile
from backend.channel import convert
from frontend.savefile import choose_folder, savefile

app = ctk.CTk()
app.title("FFormat")
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}")

entry_field = ctk.CTkEntry(app, placeholder_text="Select a file to upload or type in the absolute path manually", width=600, height=30)
entry_field.pack(padx=25, pady=25)
entry_field.place(x=370, y=225)

button_to_select = ctk.CTkButton(app, text="Choose file", fg_color="blue", command=lambda: selectfile(entry_field))
button_to_select.pack(padx=25, pady=25)
button_to_select.place(x=995, y=225)

button_to_upload = ctk.CTkButton(app, text="Upload", fg_color="green", command=lambda: addfile(entry_field, file_name_label, extension_label, no_file_label))
button_to_upload.pack(padx=25, pady=25)
button_to_upload.place(x=710, y=280)

file_name_label = ctk.CTkLabel(app, text="File selected:", font=("Arial", 16), fg_color="gray", height=30, width=300)
file_name_label.pack(padx=25, pady=25)
file_name_label.place(x=510, y=350)

file_type_label = ctk.CTkLabel(app, text="File type:", font=("Arial", 16))
file_type_label.pack(padx=25, pady=25)
file_type_label.place(x=890, y=350)

extension_label = ctk.CTkLabel(app, text="", font=("Arial", 16), fg_color="gray", height=30, width=80)
extension_label.pack(padx=25, pady=25)
extension_label.place(x=970, y=350)

no_file_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
no_file_label.pack(padx=25, pady=25)
no_file_label.place(x=370, y=275)

type_selection_label = ctk.CTkLabel(app, text="Convert to:", font=("Arial", 16))
type_selection_label.pack(padx=25, pady=25)
type_selection_label.place(x=670, y=425)

types = [".jpg", ".jpeg", ".png", ".tif", ".tiff", ".svg"]
type_selection = ctk.CTkComboBox(app, values=types, width=100, height=30)
type_selection.pack(padx=25, pady=25)
type_selection.place(x=770, y=425)

convert_button = ctk.CTkButton(app, text="Convert", fg_color="green", command=lambda: convert(new_file_label, type_selection, file_name_label, extension_label))
convert_button.pack(padx=25, pady=25)
convert_button.place(x=895, y=425)

new_file_label = ctk.CTkLabel(app, text="New file:", font=("Arial", 16), fg_color="gray", height=30, width=500)
new_file_label.pack(padx=25, pady=25)
new_file_label.place(x=530, y=500)

saved_file_label = ctk.CTkLabel(app, text="", font=("Arial", 16), height=30, width=600)
saved_file_label.pack(padx=25, pady=25)
saved_file_label.place(x=530, y=575)

save_button = ctk.CTkButton(app, text="Save", fg_color="green", command=lambda: savefile(new_file_label, saved_file_label))
save_button.pack(padx=25, pady=25)
save_button.place(x=710, y=550)

app.mainloop()