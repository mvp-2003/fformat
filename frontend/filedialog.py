from tkinter import filedialog

def selectfile():
    filename = filedialog.askopenfilename()
    print(filename)