from hmac import new
import customtkinter as ctk
from backend.light import addfile
from frontend.filedialog import selectfile
from backend.channel import convert
from frontend.savefile import choose_folder, savefile

app = ctk.CTk()
app.title("FFormat")
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 800
window_height = 600
position_top = int((screen_height - window_height) / 2)
position_right = int((screen_width - window_width) / 2)
app.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

entry_field = ctk.CTkEntry(app, placeholder_text="Select a file to upload or type in the absolute path manually", width=600, height=30)
entry_field.pack(padx=25, pady=25)
entry_field.place(x=370, y=125)

button_to_select = ctk.CTkButton(app, text="Choose file", fg_color="blue", command=lambda: selectfile(entry_field))
button_to_select.pack(padx=25, pady=25)
button_to_select.place(x=995, y=125)

button_to_upload = ctk.CTkButton(app, text="Upload", fg_color="green", command=lambda: addfile(entry_field, file_name_label, extension_label, no_file_label))
button_to_upload.pack(padx=25, pady=25)
button_to_upload.place(x=710, y=180)

file_name_label = ctk.CTkLabel(app, text="File selected:", font=("Arial", 16), fg_color="gray", height=30, width=300)
file_name_label.pack(padx=25, pady=25)
file_name_label.place(x=510, y=250)

file_type_label = ctk.CTkLabel(app, text="File type:", font=("Arial", 16))
file_type_label.pack(padx=25, pady=25)
file_type_label.place(x=890, y=250)

extension_label = ctk.CTkLabel(app, text="", font=("Arial", 16), fg_color="gray", height=30, width=80)
extension_label.pack(padx=25, pady=25)
extension_label.place(x=970, y=250)

no_file_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
no_file_label.pack(padx=25, pady=25)
no_file_label.place(x=370, y=175)

type_selection_label = ctk.CTkLabel(app, text="Convert to:", font=("Arial", 16))
type_selection_label.pack(padx=25, pady=25)
type_selection_label.place(x=670, y=325)

types = [".jpg", ".jpeg", ".png", ".tif", ".tiff", ".svg"]
type_selection = ctk.CTkComboBox(app, values=types, width=100, height=30)
type_selection.pack(padx=25, pady=25)
type_selection.place(x=770, y=325)

convert_button = ctk.CTkButton(app, text="Convert", fg_color="green", command=lambda: convert(new_file_label, type_selection, file_name_label, extension_label))
convert_button.pack(padx=25, pady=25)
convert_button.place(x=895, y=325)

new_file_label = ctk.CTkLabel(app, text="New file:", font=("Arial", 16), fg_color="gray", height=30, width=500)
new_file_label.pack(padx=25, pady=25)
new_file_label.place(x=530, y=400)

saved_file_label = ctk.CTkLabel(app, text="", font=("Arial", 16), height=30, width=600)
saved_file_label.pack(padx=25, pady=25)
saved_file_label.place(x=530, y=650)

choose_folder_button = ctk.CTkButton(app, text="Choose folder ", fg_color="blue", command=lambda: choose_folder(selected_folder_name))
choose_folder_button.pack(padx=25, pady=25)
choose_folder_button.place(x=745, y=465)

folder_select = ctk.CTkLabel(app, text="Selected folder: ", font=("Arial", 16))
folder_select.pack(padx=25, pady=25)
folder_select.place(x=320, y=525)

selected_folder_name = ctk.CTkLabel(app, text="", font=("Arial", 16), fg_color="gray", height=30, width=700)
selected_folder_name.pack(padx=25, pady=25)
selected_folder_name.place(x=450, y=525)

save_button = ctk.CTkButton(app, text="Save", fg_color="green", command=lambda: savefile(selected_folder_name.cget("text"), new_file_label.cget("text"), saved_file_label.cget("text")))
save_button.pack(padx=25, pady=25)
save_button.place(x=745, y=600)

upload_to_label = ctk.CTkLabel(app, text="Upload to:", font=("Arial", 16))
upload_to_label.pack(padx=25, pady=25)
upload_to_label.place(x=655, y=465)

app.mainloop()