from customtkinter import filedialog

def selectfile(entry_field):
    filename = filedialog.askopenfilename()
    entry_field.delete(0, 'end')
    entry_field.insert(0, filename)