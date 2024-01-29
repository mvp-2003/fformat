from customtkinter import filedialog

def selectfile():
    filename = filedialog.askopenfilename()
    print(filename)